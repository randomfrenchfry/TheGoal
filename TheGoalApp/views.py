from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'TheGoalApp/theGoalMainPg.html')
def login(request):
    return render(request, 'TheGoalApp/logInPg.html')
<<<<<<< HEAD
def signup(request):
    return render(request, 'TheGoalApp/SignUpPg.html')
=======
def profile(request):
    return render(request, 'TheGoalApp/profile.html')
>>>>>>> 3cdd1154f54887111a427815c9cbe9e97d8f3240
