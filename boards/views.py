from django.shortcuts import render, HttpResponseRedirect, HttpResponse, resolve_url
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from boards.models import BoardButton
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
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            button = BoardButton(
                identifier = uuid.uuid4().hex,
                button_text = body['text'],
                button_label = body['label'],
                author = User.objects.get(id=request.user.id)
            )

            button.save()

            if request.headers['Accept'] == 'application/json':
                data = {
                    'success': True,
                    'identifier': button.identifier,
                    'text': button.button_text,
                    'label': button.button_label,
                }
                return HttpResponse(json.dumps(data), content_type='application/json')
            else:
                return render(request, template_name, None)
        else:
            return HttpResponseRedirect(resolve_url('/accounts/login'))