from django.shortcuts import render
from django.shortcuts import redirect

# Here you would typically authenticate the user
# For example, using Django's built-in authentication system
from django.contrib.auth import authenticate, login
from django.urls import reverse, NoReverseMatch

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        # Process the login form submission
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next')
            if next_url:
                try:
                    # Try to reverse if it's a named URL
                    next_url = reverse(next_url)
                except NoReverseMatch:
                    # If it's not a named URL, use as is (could be a path)
                    pass
                return redirect(next_url)
            return redirect('home')
        else:
            # Handle invalid login
            return render(request, 'usuarios/login.html', {"error": "Invalid credentials", "next": request.POST.get('next', None)})
    if request.user.is_authenticated:
        return redirect('home')
    
    next = request.GET.get('next',None)

    
    return render(request, 'usuarios/login.html',{"next":next})