from django.http import HttpResponse
from django.shortcuts import render
from .forms import FeedbackForm
from . import canteenbot, sssbot ,clginfobot, librarybot, placementbot, sportsbot, stringerrorforgiver
import sqlite3

# Create your views here.

def index(request):
    context = {}
    return render(request, "index.html")


def services(request):
    context = {}
    return render(request, "services.html")


def about(request):
    context = {}
    return render(request, "about.html")


def contact(request):
    context = {}
    return render(request, "contact.html")


def gallery(request):
    context = {}
    return render(request, "gallery.html")

def college(request):
    context = {}
    def chat(msg):
        # print("Start chatting with the bot (type quit to stop)!")
        rresponse, contextimg = clginfobot.response(msg) 
        return rresponse
    def img():
        rresponse, contextimg = clginfobot.response(msg)
        return contextimg
    if request.method == 'POST':
        msg = request.POST.get('input', '')
        context['query'] = msg
        context['chatresponse'] = chat(msg)
        context['imgresponse'] = img()
        # return HttpResponse(chatresponse, content_type='text/plain')
    return render(request, "clginfobot.html",context)

def placement(request):
    context = {}
    def chat(msg):
        # print("Start chatting with the bot (type quit to stop)!")
        rresponse, contextimg = placementbot.response(msg) 
        return rresponse
    def img():
        rresponse, contextimg = placementbot.response(msg)
        return contextimg
    if request.method == 'POST':
        msg = request.POST.get('input', '')
        context['query'] = msg
        context['chatresponse'] = chat(msg)
        context['imgresponse'] = img()
        # return HttpResponse(chatresponse, content_type='text/plain')
    return render(request, "placementbot.html",context)

def library(request):
    context = {}
    def chat(msg):
        # print("Start chatting with the bot (type quit to stop)!")
        rresponse, contextimg = librarybot.response(msg) 
        return rresponse
        return contextimg
    if request.method == 'POST':
        msg = request.POST.get('input', '')
        context['query'] = msg
        context['chatresponse'] = chat(msg)
    return render(request, "librarybot.html",context)

def booksearch(request):
    context = {}
    def findingbook(inp):
        query = f"SELECT books,author,year,book_availability FROM library WHERE books ='{inp}'" 
        conn = sqlite3.connect("db.sqlite3")
        c = conn.cursor()
        c.execute(query)
        results = c.fetchall()
        
        conn.close()
        return results

    if request.method == 'POST':
        book = request.POST.get('input', '')
        correct_string = stringerrorforgiver.forgive_bookname(book)
        context['query'] = book
        context['details'] = findingbook(correct_string)
      
    return render(request, "booksearch.html",context)

def authorsearch(request):
    context = {}
    def findingbook(inp):
        query = f"SELECT books,author,year,book_availability FROM library WHERE author ='{inp}'" 
        conn = sqlite3.connect("db.sqlite3")
        c = conn.cursor()
        c.execute(query)
        results = c.fetchall()
        conn.close()
        return results

    if request.method == 'POST':
        author = request.POST.get('input', '')
        correct_string = stringerrorforgiver.forgive_authorname(author)
        context['query'] = author
        context['details'] = findingbook(correct_string)

    return render(request, "authorsearch.html",context)


def sss(request):
    context = {}

    def chat(msg):
        # print("Start chatting with the bot (type quit to stop)!")
        rresponse = sssbot.response(msg) 
        return rresponse
        
    if request.method == 'POST':
        msg = request.POST.get('input', '')
        context['query'] = msg
        context['chatresponse'] = chat(msg)



        # return HttpResponse(chatresponse, content_type='text/plain')
    return render(request, "sssbot.html",context)

def canteen(request):
    context = {}

    def chat(msg):
        # print("Start chatting with the bot (type quit to stop)!")
        rresponse, contextimg = canteenbot.response(msg) 
        return rresponse

    def img():
        rresponse, contextimg = canteenbot.response(msg)
        return contextimg
        
    if request.method == 'POST':
        msg = request.POST.get('input', '')
        context['query'] = msg
        context['chatresponse'] = chat(msg)
        context['imgresponse'] = img()
        # return HttpResponse(chatresponse, content_type='text/plain')
    return render(request, "canteenbot.html",context)

def sports(request):
    context = {}

    def query_data(inp):
        query = f"SELECT time_of_game,game_list,captain_of_game,staff,grounds,tournament_timing,overview FROM sports_details WHERE game_details ='{inp}'" 
        conn = sqlite3.connect("db.sqlite3")
        c = conn.cursor()
        c.execute(query)
        results = c.fetchall()
        conn.close()

    
        return results[0]


    def chat(msg):
        rresponse, contextimg = sportsbot.response(msg) 
        return rresponse

    def img():
        rresponse, contextimg = sportsbot.response(msg)
        return contextimg
        
    if request.method == 'POST':
        msg = request.POST.get('input', '')
        context['query'] = msg
        context['chatresponse'] = chat(msg)
        context['imgresponse'] = img()

        tag = sportsbot.response.tagg

        context['dataresponse'] = query_data(tag)

    return render(request, "sportsbot.html",context)


def feedback_form(request):

    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'form/thanks.html')
    else:
        form = FeedbackForm()
    context = {'form': form}
    return render(request, 'form/feedback_form.html', {'form': form})


def chatbot(request):
    if request.method == 'POST':
        msg = request.POST.get('input', '')
        if msg == 'eric':
            return HttpResponse("eric is alive")
        else:
            return HttpResponse("eric is not alive")
    return render(request, 'chatbot.html')
