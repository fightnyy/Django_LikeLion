from django.shortcuts import render


def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')


def counter(request):
    full_text=request.GET['fulltext']
    word_list=full_text.split()
    wordDict={}
    for word in word_list:
        if word in wordDict:
            wordDict[word]+=1
        else:
            wordDict[word]=1
    return render(request,'count.html',{'fulltext':full_text,'total':len(word_list),'wordDict':wordDict.items(),'length':wordDict[word]})
# Create your views here.
