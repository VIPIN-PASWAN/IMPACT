from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
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


def signupUser(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous input
        if 10 < len(username) < 4:
            messages.error(request, " Your user name must be between 4 to 10 characters")
            return redirect('home')
        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if pass1 != pass2:
            messages.error(request, " Passwords do not match")
            return redirect('home')

        if User.objects.filter(username=username).first():
            messages.error(request, "This username is already taken")
            return redirect('home')
        if User.objects.filter(email=email).first():
            messages.error(request, "This email is already taken")
            return redirect('home')

        user = User.objects.create_user(username, email, pass1)
        user.first_name = fname
        user.last_name = lname
        user.save()
        messages.success(request, "Your account has been created successfully.")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")


def loginUser(request):
    username = request.POST['username']
    password = request.POST['pass1']
    user = authenticate(request, username=username, password=password)
    # path = request.get_full_path()
    if user is not None:
        login(request, user)
        messages.success(request, "Login successfully.")
        return redirect('home')
    else:
        messages.error(request, "Login failed !")
        return redirect('home')


def logoutUser(request):
    logout(request)
    messages.success(request, "Logout successfully!")
    return redirect('home')
