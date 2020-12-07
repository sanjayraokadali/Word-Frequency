from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def BasePage(request):

    return render(request,'freqApp/BasePage.html')

def FrequencyPage(request):


    return render(request,'freqApp/FrequencyPage.html')

def ResultsPage(request):
    url =''

    if request.method == 'POST':

        url = request.POST.get('url')

        print(url)

    return render(request,'freqApp/ResultsPage.html',{'url':url})
