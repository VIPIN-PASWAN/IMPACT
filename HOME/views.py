from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from HOME.models import Contact
from BLOG.models import Post

# Create your views here.


def home(request):
    return render(request, 'home/home.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "Please fill the form correctly !")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")

    return render(request, 'home/contact.html')


def about(request):
    return render(request, 'home/about.html')


def search(request):
    query = request.GET['search']
    searchTitle = Post.objects.filter(title__icontains=query)
    searchAuth = Post.objects.filter(author__icontains=query)
    searchCont = Post.objects.filter(content__icontains=query)

    searchPost = searchTitle.union(searchAuth, searchCont)
    context = {"searchPost": searchPost, "query": query}
    return render(request, "blog/search.html", context)
