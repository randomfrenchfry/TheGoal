from django.shortcuts import render

from .logInForm import LogInForm
# Create your views here.

def home(request):
    return render(request, 'TheGoalApp/theGoalMainPg.html')
def login(request):
    if request.method =='POST':#if we get form data from POST
        form = LogInForm(request.POST)
        if form.is_valid():
            context = {
                'form': form,
                'userN': form.cleaned_data['userName'],
                'passW': form.cleaned_data['password'],
            }
        else:#if the form data from POST is bad
            context = {
                'form': form,
                'userN': '',
                'passW': '',
            }
    else:#if no form data from POST
        form = LogInForm()
        context = {
            'form': form,
            'userN': '',
            'passW': '',
        }
    return render(request, 'TheGoalApp/logInPg.html', context)

def signup(request):
    return render(request, 'TheGoalApp/SignUpPg.html')
def profile(request):
    return render(request, 'TheGoalApp/profile.html')
