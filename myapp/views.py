from django.shortcuts import render, HttpResponseRedirect
from . forms import StudentRegistrationForm
from django.contrib import messages
from . models import User

#This is For Add new Item ans Show The new item on Frontin
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistrationForm()
            messages.success(request, 'Form submission successful')
    else:
        fm = StudentRegistrationForm()
    stu = User.objects.all()
    return render(request, 'myapp/addandshow.html', {'form': fm, 'stu':stu})

#This Function is For Update/Edit Data
def update_data(request, id):
    if request.method == 'POST':
        up = User.objects.get(pk=id)
        fm = StudentRegistrationForm(request.POST, instance=up)
        if fm.is_valid():
            fm.save()
    else:
        up = User.objects.get(pk=id)
        fm = StudentRegistrationForm(instance=up)
    return render(request, 'myapp/update.html', {'form':fm})

#This Function is For Detele Item
def delete_data(request, id):
    if request.method == 'POST':
        de = User.objects.get(pk=id)
        de.delete()
        return HttpResponseRedirect('/')

