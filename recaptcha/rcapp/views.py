from django.shortcuts import render, redirect
from .models import user_data
import requests


def home(request):
    if request.method == "POST":
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': '6LfZZY8rAAAAAA_ZiHRGsQNgIWU_OJFXaYq-3019',  # You can also use settings.RECAPTCHA_SECRET_KEY
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        if result.get('success'):
            # reCAPTCHA passed
            # return render(request, 'dashboard.html')
            return redirect(dashboard)
        else:
            # reCAPTCHA failed
            return render(request, 'index.html', {'error': 'Invalid reCAPTCHA. Please try again.'})

    return render(request, 'index.html')


def success(request):
    return render(request, 'success.html')


# Create your views here.

def register(request):
    if request.method == 'POST':
        NAME = request.POST['NAME']
        EMAIL = request.POST['EMAIL']
        PASSWORD = request.POST['PASSWORD']

        s = user_data(name=NAME, email=EMAIL, password=PASSWORD)
        s.save()

        return redirect(home)
    return render(request, 'register.html')


def dashboard(request):
    user = user_data.objects.all()
    return render(request, "dashboard.html", {'users': user})




def login(req):
    if req.method == 'POST':
        email = req.POST.get('username')
        password = req.POST.get('password')
        try:
            user = user_data.objects.get(email=email, password=password)
            return redirect('dashboard')  # Use name if you have it in urls.py
        except user_data.DoesNotExist:
            return render(req, 'index.html', {'error': 'Invalid email or password'})

    return render(req, 'index.html')
