from django.contrib.auth import logout,authenticate,login

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password

from django.shortcuts import render,redirect
from django.http import HttpResponse
from customcase.models import Cases,UserAccount
# Create your views here.
def custom(request):
    case= Cases.objects.all()

    user = None
    if 'user_id' in request.session:
        try:
            user = UserAccount.objects.get(id=request.session['user_id'])
        except UserAccount.DoesNotExist:
            pass

    return render(request, "custom.html",{'case':case})

def customiser_view(request):
    return render(request, 'customizer.html')

def signup(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname', '')
        username = request.POST['username']
        password = request.POST['password']

        # Hash the password before saving
        hashed_password = make_password(password)

        UserAccount.objects.create(
            nickname=nickname,
            username=username,
            password=hashed_password
        )
        return redirect('login_view')  

    return render(request, "signup.html")

def log(request):
    return render(request, "login.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        try:
            # Try to fetch the user from UserAccount
            user = UserAccount.objects.get(username=username)
            
            # Compare the provided password with the hashed one
            if check_password(password, user.password):
                # Save user ID in session to mark them as logged in
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                return redirect('custom')
            else:
                return render(request, 'login.html', {'error': 'Invalid password'})
        
        except UserAccount.DoesNotExist:
            return render(request, 'login.html', {'error': 'User does not exist'})
        
        except Exception as e:
            # Log any unexpected errors for debugging
            print(f"Login error: {e}")  # For development, you can print the error
            return render(request, 'login.html', {'error': 'Something went wrong'})

    return render(request, "login.html")

def logout_view(request):
    logout(request)  # Logs out the user
    return redirect('login_view') 