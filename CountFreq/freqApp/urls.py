from django.conf.urls import url
from freqApp import views

app_name = 'freqApp'

urlpatterns =[

    url('^$',views.FrequencyPage,name='frequencypage'),
    url('^results/$',views.ResultsPage,name='resultspage'),

]
