# coding: utf-8
# from django.http import HttpResponse
# from django.template import loader, Context
# from django.shortcuts import render_to_response
# from django.conf import settings
# from django.template import RequestContext
from django.shortcuts import render
from eventex.core.models import Speaker, Talk
from django.shortcuts import get_object_or_404
# from datetime import time

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

def talk_list(request):
  # midday = time(12)
  # context = {
  #   'morning_talks' : Talk.objects.filter(start_time__lt=midday),
  #   'afternoon_talks' : Talk.objects.filter(start_time__gte=midday)
  # }
  context = {
    'morning_talks' : Talk.objects.at_morning(),
    'afternoon_talks' : Talk.objects.at_afternoon(),
  }
  return render(request, 'core/talk_list.html', context)

def talk_detail(request, pk):
  talk = get_object_or_404(Talk, pk=pk)
  context = {
    'talk' : talk,
    # 'slides' : talk.media_set.filter(kind='SL'),
    # 'videos' : talk.media_set.filter(kind='YT'),
  }
  return render(request, 'core/talk_detail.html', context)