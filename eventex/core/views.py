# coding: utf-8
# from django.http import HttpResponse
# from django.template import loader, Context
# from django.shortcuts import render_to_response
# from django.conf import settings
# from django.template import RequestContext
from django.shortcuts import render
from eventex.core.models import Speaker
from django.shortcuts import get_object_or_404

def homepage(request):
  # 1
  # return HttpResponse('Bem-vindo ao Eventex!')

  # 2
  # t = loader.get_template('index.html')
  # c = Context()

  # content = t.render(c)

  # return HttpResponse(content)

  # 3
  # context = {'STATIC_URL':settings.STATIC_URL}
  # context = RequestContext(request)
  # return render_to_response('index.html', context)

  return render(request, 'index.html')


def speaker_detail(request, slug):
  speaker = get_object_or_404(Speaker, slug=slug)
  context = {'speaker': speaker }
  return render(request, 'core/speaker_detail.html', context)