from django.shortcuts import render, HttpResponseRedirect, HttpResponse, resolve_url
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.views.generic import TemplateView
from boards.models import BoardButton
from google.cloud import texttospeech
import json, uuid


class IndexView(TemplateView):
    template_name = "boards/index.html"

    def get(self, request):
        if request.user.is_authenticated:
            buttons = BoardButton.objects.filter(
                author = User.objects.get(id=request.user.id)
            )
            return render(request, self.template_name, {
                'buttons': buttons
            })
        else:
            return HttpResponseRedirect(resolve_url('/accounts/login'))
        
class ListBoardView(TemplateView):

    def get(self, request):
        if request.user.is_authenticated:
            template_name = "boards/list_board.html"
            buttons = BoardButton.objects.filter(
                author = User.objects.get(id=request.user.id)
            )
            return render(request, template_name, {
                'buttons': buttons
            })
        else:
            return HttpResponseRedirect(resolve_url('/accounts/login'))
        
    def delete(self, request):
        if request.user.is_authenticated:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            buttons = BoardButton.objects.filter(
                author = User.objects.get(id=request.user.id),
                identifier = body['identifier']
            )

            buttons.delete()

            return HttpResponse(json.dumps({ 'success': True }), content_type='application/json')

class CreatedBoardView(TemplateView):
    def get(self, request):
        template_name = "boards/create_board.html"
        if request.user.is_authenticated:
            return render(request, template_name, None)
        else:
            return HttpResponseRedirect(resolve_url('/accounts/login'))
        
    def post(self, request):
        template_name = "boards/created_board.html"

        if request.user.is_authenticated:
            params = request.POST.dict()



            # Gerar audio do botao
            gclient = texttospeech.TextToSpeechClient()

            # Set the text input to be synthesized
            synthesis_input = texttospeech.SynthesisInput(text=params.get('text'))

            # Build the voice request, select the language code ("en-US") and the ssml
            # voice gender ("neutral")
            voice = texttospeech.VoiceSelectionParams(
                language_code="pt-BR", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
            )

            # Select the type of audio file you want returned
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3
            )

            # Perform the text-to-speech request on the text input with the selected
            # voice parameters and audio file type
            response = gclient.synthesize_speech(
                input=synthesis_input, voice=voice, audio_config=audio_config
            )
            
            button = BoardButton(
                identifier = uuid.uuid4().hex,
                button_text = params.get('text'),
                button_label = params.get('label'),
                button_image = request.FILES.get('image'),
                button_audio = ContentFile(response.audio_content, "audio.mp3"),
                author = User.objects.get(id=request.user.id)
            )

            button.save()

            if request.headers['Accept'] == 'application/json':
                data = {
                    'success': True,
                    'identifier': button.identifier,
                    'text': button.button_text,
                    'image': "image url",
                    'label': button.button_label,
                }
                return HttpResponse(json.dumps(data), content_type='application/json')
            else:
                return render(request, template_name, None)
        else:
            return HttpResponseRedirect(resolve_url('/accounts/login'))