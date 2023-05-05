from django.shortcuts import render,redirect
import requests
# Create your views here.
def home(request):
    if request.method=="POST":
        id=request.POST['id']
        d=requests.get("https://tanveerpp.pythonanywhere.com/emps/"+id)
        data=[d.json()]
        return render(request,'search.html',{'data':data})
    else:
        res=requests.get("https://tanveerpp.pythonanywhere.com/emps/")
        data=res.json()
        return render(request,'index.html',{'data':data})
    
def addapi(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        password=request.POST['password']
        requests.post("https://tanveerpp.pythonanywhere.com/emps/",{
            'name':name,
            'email':email,
            'address':address,
            'password':password
        })
        res=requests.get("https://tanveerpp.pythonanywhere.com/emps/")
        data=res.json()
        return render(request,'index.html',{'data':data})
    else:
        return render(request,'addapi.html')
    
def delete(request):
    id=request.GET['id']
    requests.delete("https://tanveerpp.pythonanywhere.com/emps/"+id)
    res=requests.get("https://tanveerpp.pythonanywhere.com/emps/")
    data=res.json()
    return render(request,'index.html',{'data':data})

def update(request):
    id=request.POST['id']
    name=request.POST['name']
    email=request.POST['email']
    address=request.POST['address']
    password=request.POST['password']
    requests.put("https://tanveerpp.pythonanywhere.com/emps/"+id+"/",{
            'name':name,
            'email':email,
            'address':address,
            'password':password
    })
    res=requests.get("https://tanveerpp.pythonanywhere.com/emps/")
    data=res.json()
    return render(request,'index.html',{'data':data})