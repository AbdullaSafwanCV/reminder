from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 


from .forms import ReminderForm
from .models import Reminder

@login_required(
    login_url='login'
)
def index(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            Reminder.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                date=form.cleaned_data['date']
            )
            return redirect('index')
    else:
        form = ReminderForm()
    reminders = Reminder.objects.filter(is_completed=False)
    completed_cards = Reminder.objects.filter(is_completed=True)
    return render(request, 'index.html', {
        'reminders': reminders,
        "completed_cards": completed_cards,
        "form": form,
        'reminder': form
    })

def completed(request,id):
    completed = Reminder.objects.get(id=id)
    completed.is_completed = not completed.is_completed
    completed.save()
    return redirect('index')

def delete(request,id):
    reminder = Reminder.objects.get(id=id)
    reminder.delete()
    return redirect('index')

def addReminder(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        Reminder.objects.create(title=title, description=description, date=date)
        return redirect('index')
    return redirect('index')

def edit_reminder(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk)

    if request.method == 'POST':
        form = ReminderForm(request.POST, instance=reminder)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ReminderForm(instance=reminder)

    return render(request, 'edit_reminder.html', {'form': form, 'reminder': reminder})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index') 
        else:
            return render(request, 'registration_page.html', {'error': 'Invalid credentials'})
    return render(request, 'registration_page.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login')
    return render(request, 'registration_page.html')


def logout_view(request):
    logout(request)
    return redirect('login')
