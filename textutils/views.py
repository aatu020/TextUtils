#I have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request,'index.html')
    # return HttpResponse("<h1>home</h1>")

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')


    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[] . {};:'" \ ,<>  /?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'changed to upper case','analyzed_text':analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose':'new line removerd','analyzed_text':analyzed}
        djtext = analyzed
    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index]==' ':
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose':'extra space removed','analyzed_text':analyzed}
        djtext = analyzed

    if charcounter == "on":
        analyzed = ""
        counter = 0
        for char in djtext:
            if char != ' ':
                counter=counter+1
            analyzed = counter
        params = {'purpose': 'number of character', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request,'analyze.html',params)



