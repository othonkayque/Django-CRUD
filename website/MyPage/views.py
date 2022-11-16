from django.shortcuts import render, redirect
from .models import MyUsers
# Create your views here.
def MyPagess(request):
    data = {}
    data['myusers'] = MyUsers.objects.all()
    return render(request, 'MyPage/index.html', data)

def back(request):
    return redirect(MyPagess)

def create(request):
    data = {}
    myusers = request.POST.get('name')
    MyUsers.objects.create(name=myusers)
    data['userdb'] = MyUsers.objects.all()
    return redirect(MyPagess)

def editar(request, id):  
    myid = MyUsers.objects.get(id=id)
    return render(request, 'Editar/index.html', {'myid':myid})

def update(request, id):
    myid = MyUsers.objects.get(id=id)
    newname = request.POST.get('name')
    myid.name = newname
    myid.save()
    return redirect(MyPagess)

def delete(request, id):
    myid = MyUsers.objects.get(id=id)
    myid.delete()
    return redirect(MyPagess)