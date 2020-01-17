
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps', 'off')
    if  removepunc=='on':
        punctuation='''!()-[]{};:'"\,<>./'''
        analyzed =''
        for i in djtext:
            if i not in punctuation:
                analyzed=analyzed+i
        parmas={'purpose':'removed punctuation','analyzed_text':analyzed}

        return render(request,'analyze.html', parmas)
    elif(fullcaps=='on'):
        analyzed=''
        for i in djtext:
            analyzed=analyzed+i.upper()
        parmas = {'purpose': 'New Text is here ', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', parmas)

    else:
        return HttpResponse('error')

