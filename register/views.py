# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from pymongo import MongoClient
client = MongoClient();
mydb = client["finance"]
mycol = mydb["register"]
fn=''
ln=''
s=''
em=''
pwd=''
# Create your views here.
def signaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        
        d=request.POST
        for key,value in d.items():
            if key=="name":
                fn=value

            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        mydict = { "name": fn, "email": em,"passw": pwd }

        x = mycol.insert_one(mydict)

    return render(request,'signup_page.html')