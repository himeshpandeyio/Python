from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def home(request):
    page = {
        'page_title' : 'Home Page',
        'user_name' : 'Developer'
    }
    
    people = [
        {'name':'Himesh', 'age':'21'},
        {'name':'Pandey', 'age':'25'},
        {'name':'Shekhar', 'age':'24'},
        {'name':'Sandeep', 'age':'23'},
        {'name':'Aaditya', 'age':'22'},
    ]
    
    return render(request, 'core/index.html', context = {'people':people,'page' : page})    

def success_page(request):
    return HttpResponse("<h1>Hey I'm Django server and you will do it!!</h1>")