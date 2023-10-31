from django.shortcuts import render,redirect
from secapp.models import student
from secapp.forms import studform

# Create your views here.
def display(request):
    stud=student.objects.all()
    k={'stud':stud}
    return render(request,'secapp/index.html',context=k)

def create(request):
    form=studform()
    if request.method =='POST':
        form=studform(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('/check')   
        
    return render(request,'secapp/create.html',{'form':form})
def delete(request,id):
    stud=student.objects.get(id=id)
    stud.delete()
    return redirect('/check')

def update(request,id):
    stud=student.objects.get(id=id)
    if request.method =='POST':
        form=studform(request.POST,instance=stud)
        if form.is_valid():
            form.save() 
            return redirect('/check')

    return render(request,'secapp/update.html',{'stud' : stud})