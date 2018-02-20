from django.conf.urls import url

from . import views

app_name = 'polls'
#Our URLconf to map a view to a URL so that we can call a view. 
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    #When somebody requests a page from your website say, '/polls/34/', Django will load the
    # mysite.urls Python module because it's pointed to by the 'ROOT_URLCONF' setting. It finds the 
    #variable named urlpatterns and traverses the regular expressions in order. After finding the
    # match at '^polls/', it strips off the matching text ("polls/") and sends the remaining 
    #text - "34/" - to the 'polls.urls' URLconf for further processing. There it matches
    # r'^(?P<question_id>[0-9]+)/$', resulting in a call to the detail() view like so:
    
    #    detail(request=<HttpRequest object>, question_id='34')
    
    #The question_id='34' part comes from (?P<question_id>[0-9]+). Using parentheses around a pattern
    # 'captures' the text matched by that pattern and sends it as an argument to the view function;
    # ?P<question_id> defines the name that will be used to identify the matched pattern; and [0-9]+ is
    # a regular expression to match a sequence of digits (i.e., a number). Because the URL
    # patterns are regular expressions, there really is no limit on what you can do with them. 
 
    
    # the 'name' value as called by the {% url %} template tag
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # added the word 'specifics'
    #url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
