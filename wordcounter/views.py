from django.shortcuts import render
from django.http import HttpResponse
import operator


def homepage(request):

    return render(request,'homepage.html', {'name':'jaswant singh'} )

def counted(request):
    data = request.GET['fulltext']
    text_list = data.split()
    length = len(text_list)

    worddict = {}

    for word in text_list:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

    sort = sorted(worddict.items(), key=operator.itemgetter(1), reverse=1)
    return render(request,'counted.html',{'text':data,'length':length,'worddict': sort})






def aboutpage(request):

    return render(request, 'aboutpage.html',{"name":"jaswant bisht","profession":"web developer"})