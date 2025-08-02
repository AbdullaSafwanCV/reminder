from django import forms
from django.shortcuts import get_object_or_404, redirect, render
from .models import Reminder

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'description', 'date']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description', 'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

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
