from django.shortcuts import render
from . forms import StudentRegistrationForm
from django.contrib import messages


def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Form submission successful')
            fm = StudentRegistrationForm()
    else:
        fm = StudentRegistrationForm()
    return render(request, 'myapp/addandshow.html', {'form': fm})
