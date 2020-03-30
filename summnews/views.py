from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles
from newspaper import Article
from newspaper import Config
# Create your views here.
import requests

def home(request):
    main_url="http://newsapi.org/v2/top-headlines?country=in&pageSize=17&apiKey=813ecab326254348a7d1e8ef73d2838f"
    
	# fetching data in json format 
    open_news_page = requests.get(main_url).json() 
	# getting all articles in a string article 
    article = open_news_page["articles"] 
    results = [] 
   
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    config = Config()
    config.browser_user_agent = user_agent
    for ar in article:
        article=Articles()

        intl = []
        intl.append(ar["title"])
        intl.append(ar["description"])
        intl.append(ar["urlToImage"])
        
        intl.append(ar["url"])
        toi_article = Article(intl[3], language="en",config=config)
        toi_article.download() 
  
        #To parse the article 
        toi_article.parse() 
  
        #To perform natural language processing ie..nlp 
        toi_article.nlp() 
        summ=toi_article.summary
        intl.append(summ)
        results.append(intl)
    content={'article':results}
    return render(request,'summnews/index.html',content)
def summarize(request,value1):
    #print('--------------------------',value2)
    #return HttpResponse('<h1>abcd</h1>')
    content={'links':[value1]}
    return render(request,'summnews/summtext.html',content)

def sports(request):
    main_url="http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=813ecab326254348a7d1e8ef73d2838f"
    
	# fetching data in json format 
    open_news_page = requests.get(main_url).json() 
	# getting all articles in a string article 
    article = open_news_page["articles"] 
    results = [] 
    
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    config = Config()
    config.browser_user_agent = user_agent
    for ar in article:
        article=Articles()
        intl = []
        intl.append(ar["title"])
        intl.append("abcd")
        intl.append(ar["urlToImage"])
        #print("imglink",intl[2])
        intl.append(ar["url"])
        toi_article = Article(intl[3], language="en",config=config)
       
        toi_article.download() 
         
        #To parse the article 
        toi_article.parse() 
  
        #To perform natural language processing ie..nlp 
        toi_article.nlp() 
        summ=toi_article.summary
        intl.append(summ)
        results.append(intl)
   
    content={'article':results}
    return render(request,'summnews/sports2.html',content)

def health(request):
    main_url="http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=813ecab326254348a7d1e8ef73d2838f"
	# fetching data in json format 
    open_news_page = requests.get(main_url).json() 
	# getting all articles in a string article 
    article = open_news_page["articles"] 
    results = [] 
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    config = Config()
    config.browser_user_agent = user_agent
    for ar in article:
        article=Articles()
        intl = []
        intl.append(ar["title"])
        intl.append("abcd")
        intl.append(ar["urlToImage"])
        intl.append(ar["url"])
        toi_article = Article(intl[3], language="en",config=config)
        toi_article.download() 
        #To parse the article 
        toi_article.parse() 
        #To perform natural language processing ie..nlp 
        toi_article.nlp() 
        summ=toi_article.summary
        intl.append(summ)
        results.append(intl)
    content={'article':results}
    return render(request,'summnews/health.html',content)
def science(request):
    main_url="http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=813ecab326254348a7d1e8ef73d2838f"
	# fetching data in json format 
    open_news_page = requests.get(main_url).json() 
	# getting all articles in a string article 
    article = open_news_page["articles"] 
    results = [] 
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    config = Config()
    config.browser_user_agent = user_agent
    for ar in article:
        article=Articles()
        intl = []
        intl.append(ar["title"])
        intl.append("abcd")
        intl.append(ar["urlToImage"])
        intl.append(ar["url"])
        toi_article = Article(intl[3], language="en",config=config)
        toi_article.download() 
        #To parse the article 
        toi_article.parse() 
        #To perform natural language processing ie..nlp 
        toi_article.nlp() 
        summ=toi_article.summary
        intl.append(summ)
        results.append(intl)
    content={'article':results}
    return render(request,'summnews/science.html',content)
def business(request):
    main_url="http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=813ecab326254348a7d1e8ef73d2838f"
	# fetching data in json format 
    open_news_page = requests.get(main_url).json() 
	# getting all articles in a string article 
    article = open_news_page["articles"] 
    results = [] 
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    config = Config()
    config.browser_user_agent = user_agent
    for ar in article:
        article=Articles()
        intl = []
        intl.append(ar["title"])
        intl.append("abcd")
        intl.append(ar["urlToImage"])
        intl.append(ar["url"])
        toi_article = Article(intl[3], language="en",config=config)
        toi_article.download() 
        #To parse the article 
        toi_article.parse() 
        #To perform natural language processing ie..nlp 
        toi_article.nlp() 
        summ=toi_article.summary
        intl.append(summ)
        results.append(intl)
    content={'article':results}
    return render(request,'summnews/business.html',content)
def technology(request):
    main_url="http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=813ecab326254348a7d1e8ef73d2838f"
	# fetching data in json format 
    open_news_page = requests.get(main_url).json() 
	# getting all articles in a string article 
    article = open_news_page["articles"] 
    results = [] 
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    config = Config()
    config.browser_user_agent = user_agent
    for ar in article:
        article=Articles()
        intl = []
        intl.append(ar["title"])
        intl.append("abcd")
        intl.append(ar["urlToImage"])
        intl.append(ar["url"])
        toi_article = Article(intl[3], language="en",config=config)
        toi_article.download() 
        #To parse the article 
        toi_article.parse() 
        #To perform natural language processing ie..nlp 
        toi_article.nlp() 
        summ=toi_article.summary
        intl.append(summ)
        results.append(intl)
    content={'article':results}
    return render(request,'summnews/technology.html',content)
