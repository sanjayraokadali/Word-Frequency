from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import trafilatura
from collections import Counter
from operator import itemgetter
from freqApp.models import UsedURL



# Create your views here.
def BasePage(request):

    return render(request,'freqApp/BasePage.html')

def FrequencyPage(request):


    return render(request,'freqApp/FrequencyPage.html')

def ResultsPage(request):
    url =''

    word_pair=[]

    used_url = UsedURL()

    if request.method == 'POST':
        used_url = UsedURL()
        url = request.POST.get('url')

        if UsedURL.objects.filter(url = url).count() <= 0 and (UsedURL.objects.count() >= 0):

            print(UsedURL.objects.filter(url = url).count())
            down = trafilatura.fetch_url(url)
            text = trafilatura.extract(down)

            text = text.split(' ')
            unique_words = sorted(set(text))


            for word in unique_words:

                word_pair.append((word,text.count(word)))

            word_pair = sorted(word_pair,key=itemgetter(1), reverse=True)

            used_url = UsedURL.objects.create(url = url, result = word_pair[:10])

            used_url.save()


        else:

            return HttpResponse('URL USED Already!')

    return render(request,'freqApp/ResultsPage.html',{'url':used_url})
