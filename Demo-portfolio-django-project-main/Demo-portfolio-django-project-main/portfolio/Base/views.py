from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from Base.models import Contact

def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == "POST":
        print('post')
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        content = request.POST.get('content')
        print(name, email, number, content)

        if not (2 <= len(name or '') <= 30):
            messages.error(request, 'Length of name should be greater than 2 and less than 30 characters')
            return render(request, 'home.html')
        
        if not (2 <= len(email or '') <= 30):
            messages.error(request, 'Invalid email, try again')
            return render(request, 'home.html')
        
        if not (9 <= len(number or '') <= 13):
            messages.error(request, 'Invalid number, please try again')
            return render(request, 'home.html')
        
        ins = Contact(name=name, email=email, content=content, number=number)
        ins.save()
        messages.success(request, 'Thank You for contacting me!! Your message has been saved')
        print('data has been saved to database')
        print('The request is now processed')
    
    return render(request, 'home.html')
