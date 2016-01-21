from django.shortcuts import render
from django.http import HttpResponse
import feedparser, json
from bs4 import BeautifulSoup

def parser(url):
    feed = feedparser.parse(url)
    #list to push dict objects
    news = list()

    for item in feed['entries']:
        data = dict()
        data['title'] = item.title
        data['link'] = item.link
        #start index for finding image url
        start = item.description.find('http')
        #end index for finding the image extension
        end = item.description.find('jpg')
        #constructing a image url form start and end
        data['thumbnail'] = item.description[start:end+3] or None
        #extracting summary
        soup = BeautifulSoup(item.description, 'html5lib')
        data['summary'] = soup.content
        news.append(data)

    #creating a json data 
    return json.dumps(news)


def index(request):
    return render(request, 'nagariknews/base_nagariknews.html', {})

def politics(request):
    news = parser('http://www.nagariknews.com/politics.feed')
    return HttpResponse(news, content_type='application/json')

def economy(request):
    news = parser('http://www.nagariknews.com/economy.feed')
    return HttpResponse(news, content_type='application/json')

  
def sport(request):
    news = parser('http://www.nagariknews.com/sports.feed')
    return HttpResponse(news, content_type='application/json')

def abroad(request):
    news = parser('http://www.nagariknews.com/dispora.feed')
    return HttpResponse(news, content_type='application/json')

def technology(request):
    news = parser('http://www.nagariknews.com/technology.feed')
    return HttpResponse(news, content_type='application/json')

def art(request):
    news = parser('http://www.nagariknews.com/entertainment.feed')
    return HttpResponse(news, content_type='application/json')

def metropolitan(request):
    news = parser('http://www.nagariknews.com/metropolitan.feed')
    return HttpResponse(news, content_type='application/json')

def interview(request):
    news = parser('http://www.nagariknews.com/interview.feed')
    return HttpResponse(news, content_type='application/json')
    

def foreignemployment(request):
    news = parser('http://www.nagariknews.com/human-resource.feed')
    return HttpResponse(news, content_type='application/json')
    

def opinion(request):
    news = parser('http://www.nagariknews.com/opinion.feed')
    return HttpResponse(news, content_type='application/json')
    

def blog(request):
    news = parser('http://www.nagariknews.com/blog.feed')
    return HttpResponse(news, content_type='application/json')
    

def health(request):
    news = parser('http://www.nagariknews.com/health.feed')
    return HttpResponse(news, content_type='application/json')
    
def education(request):
    news = parser('http://www.nagariknews.com/education.feed')
    return HttpResponse(news, content_type='application/json')
    
def society(request):
    news = parser('http://www.nagariknews.com/social.feed')
    return HttpResponse(news, content_type='application/json')   

def videos(request):
    news = parser('http://www.nagariknews.com/video.feed')
    return HttpResponse(news, content_type='application/json')
    
def lifestyle(request):
    news = parser('http://www.nagariknews.com/life-style.feed')
    return HttpResponse(news, content_type='application/json')
    
def friday(request):
    news = parser('http://www.nagariknews.com/friday.feed')
    return HttpResponse(news, content_type='application/json')
    
def saturday(request):
    news = parser('http://www.nagariknews.com/nagarik-sanibar.feed')
    return HttpResponse(news, content_type='application/json')
    
def junkiri(request):
    news = parser('http://www.nagariknews.com/feeds/section/34/junkiri.feed')
    return HttpResponse(news, content_type='application/json')
    