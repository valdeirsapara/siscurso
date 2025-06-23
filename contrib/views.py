from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.POST.get('next')
            if next_url:
                return redirect(next_url)  # usa o valor direto
            return redirect('home')
        else:
            return render(request, 'usuarios/login.html', {
                "error": "Credenciais inválidas",
                "next": request.POST.get('next', '')
            })

    if request.user.is_authenticated:
        return redirect('home')

    next = request.GET.get('next', '')
    return render(request, 'usuarios/login.html', {"next": next})

def create_user_view(request):
    if  request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if not form.is_valid():
            return render(request, 'usuarios/cadastro.html', {
                    "form": form,
                    "next": request.POST.get('next', ''),
                    "messages":form.error_messages
                    }
                )

        if form.is_valid():
            user = form.save(commit=False)

            user.save()
            login(request, user)
            next_url = request.POST.get('next', 'home')
            if next_url:
                return redirect(next_url)

    return render(request, 'usuarios/cadastro.html',context={
        "form":CustomUserCreationForm(),
        "next": request.GET.get('next', '')
    })