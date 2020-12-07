from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import trafilatura
from collections import Counter
from operator import itemgetter
from freqApp.models import UsedURL
import string



# Create your views here.
def BasePage(request):

    return render(request,'freqApp/BasePage.html')

def FrequencyPage(request):

    return render(request,'freqApp/FrequencyPage.html')

def ResultsPage(request):

    cond = False

    url =''
    text=''

    word_pair=[]

    blacklist = []

    used_url = UsedURL()

    if request.method == 'POST':
        used_url = UsedURL()
        url = request.POST.get('url')

        if UsedURL.objects.filter(url = url).count() <= 0 and (UsedURL.objects.count() >= 0):

            down = trafilatura.fetch_url(url)
            temp_text = trafilatura.extract(down)

            punc = string.punctuation

            punc = list(punc)

            punc.append('')
            punc.append('--')

            for alpha in temp_text:

                if alpha in punc:
                    pass
                else:
                    text += alpha

            text = text.split(' ')
            unique_words = sorted(set(text))

            unique_words = [x.lower() for x in unique_words]

            unique_words = sorted(set(unique_words))

            fp = open('1-1000.txt','r')

            for line in fp:

                blacklist.append(line[:len(line)-1])

            fp.close()

            for word in unique_words:

                if word not in blacklist:
                    word_pair.append((word,text.count(word)))

            word_pair = sorted(word_pair,key=itemgetter(1), reverse=True)


            used_url = UsedURL.objects.create(url = url,

            word1 = word_pair[0][0],
            word1count = word_pair[0][1],
            word2 = word_pair[1][0],
            word2count = word_pair[1][1],
            word3 = word_pair[2][0],
            word3count = word_pair[2][1],
            word4 = word_pair[3][0],
            word4count = word_pair[3][1],
            word5 = word_pair[4][0],
            word5count = word_pair[4][1],
            word6 = word_pair[5][0],
            word6count = word_pair[5][1],
            word7 = word_pair[6][0],
            word7count = word_pair[6][1],
            word8 = word_pair[7][0],
            word8count = word_pair[7][1],
            word9 = word_pair[8][0],
            word9count = word_pair[8][1],
            word10 = word_pair[9][0],
            word10count = word_pair[9][1],


            )

            used_url.save()

        else:
            cond = True
            for obj in UsedURL.objects.all():

                if obj.url == url:
                    print(obj.url)
                    break

            return render(request,'freqApp/ResultsPage.html',{'url':obj,'message':'Hi There! You have already checked this URL'})

    return render(request,'freqApp/ResultsPage.html',{'url':used_url,'message':'Thank you for using this App!'})
