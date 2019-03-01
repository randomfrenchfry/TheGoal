from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'TheGoalApp/theGoalMainPg.html')
def login(request):
    return render(request, 'TheGoalApp/logInPg.html')
def signup(request):
    return render(request, 'TheGoalApp/SignUpPg.html')
