from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from pymongo import MongoClient
client = MongoClient();
mydb = client["finance"]
mycol = mydb["register"]
em=''
pwd=''
# Create your views here.
def loginaction(request):
    global em,pwd
    if request.method=="POST":
       
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        rec = mycol.find({'email':em, 'passw':pwd},{'email':1, 'passw':1, 'name':1})
        t = mycol.find({'email':em, 'passw':pwd},{'email':1, 'passw':1, 'name':1}).count()
        print(rec[0]['name'])
        if t:
            return render(request,'home2.html',{'msg':rec[0]['name']})
        else:
            return render(request,"error.html")

    return render(request,'login_page.html')