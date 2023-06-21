from django.shortcuts import render
import pickle
# Create your views here.
from django.shortcuts import render
from pymongo import MongoClient
F=''
# Create your views here.

path='dss_loan.pkl'
model = pickle.load(open(path, 'rb'))


def back(request):
    return render(request, 'welcome.html')

def back2(request):
    return render(request, 'welcome2.html')
def welcome(request):
    return render(request, 'welcome.html')
def welcome2(request):
    return render(request, 'welcome2.html')
def home2(request):
    return render(request, 'home2.html')

def loanpage(request):
    if request.method=="POST":
        print("1")
        d=request.POST
        for key,value in d.items():
            if key=="gender":
                gender=int(value)
        
            if key=="dependents":
                d=int(value)
            if key=="education":
                e=int(value)
            if key=="selfemployed":
                se=int(value)
            if key=="applicantIncome":
                income=int(value)
            if key=="coapplicantIncome":
                cincome=int(value)
            if key=="loanAmount":
                amount=int(value)
            if key=="loanterm":
                loanterm=int(value)
            if key=="credit_history":
                chis=int(value)
            if key=="propertyarea":
                pa=int(value)
            if key=="custom_select":
                marriage=int(value)
        msg=''
        prediction=model.predict([[gender ,0, d, e, se, income,cincome,amount,loanterm, chis, pa ]])
        F = prediction[0]
        if int(F)==1:
            msg = 'Loan will be approved'
        if int(F)==0:
            msg = 'Loan will not be approved'

        return render(request,'loan.html',{'msg':msg}) 

    return render(request, 'loan.html')

def PPFaction(request):
    
    if request.method=="POST":
       
        d=request.POST
        for key,value in d.items():
            if key=="amount":
                P=float(value)
            if key=="time":
                n=float(value)
        
        i = 7.1
        i = i / 100
            
        F = P * (((1+i)**n)-1)/i
        F = round(F,2)
        A=P*n
        msg= "Maturity Amount = "+str(F)+",   Invested Amout = "+str(A)
        return render(request,'PPF.html',{'r':msg})    
    return render(request,'PPF.html')
    
def APYaction(request):
    if request.method=="POST":
       
        d=request.POST
        for key,value in d.items():
            if key=="amount":
                P=int(value)
            if key=="time":
                n=int(value)
        
        i = 1
        F = P * (1 + (i/100))**n
        
        A=P
        F = round(F,2)+A
        msg= "Maturity Amount = "+str(F)+",   Invested Amout = "+str(A)
        return render(request,'APY.html',{'r':msg})    
    return render(request,'APY.html')

def PMVYYaction(request):
    if request.method=="POST":
       
        d=request.POST
        for key,value in d.items():
            if key=="amount":
                P=int(value)
            if key=="time":
                n=int(value)
            if key=="pension":
                p=int(value)
        
        i = 8
        payments = int(p * n)
        mi = i / 1200
        pension_amount = float(P * mi * ((1 + mi) * payments)) / (((1 + mi) * payments) - 1)
        pension_amount = round(pension_amount,2)
        msg= "Pension amount = "+str(pension_amount)
        return render(request,'PMVYY.html',{'r':msg})  
    return render(request,'PMVYY.html')

def SSYaction(request):
    if request.method=="POST":
       
        d=request.POST
        for key,value in d.items():
            if key=="amount":
                P=float(value)
            
        
        i = 7.6
        i = i / 100
        n = 21    
        P=P*14
        F = P*((1 + i/1) ** (1*n))
        F = round(F,2)
        
        msg= "Maturity Amount = "+str(F)+",   Invested Amout = "+str(P)
        return render(request,'SSY.html',{'r':msg}) 
    return render(request,'SSY.html')


def homeloanaction(request):
    if request.method=="POST":
       
        d=request.POST
        for key,value in d.items():
            if key=="amount":
                P=float(value)
            if key=="interest":
                inter=float(value)
            if key=="time":
                n=float(value)
            
        
        i = inter/100/12
        loan_term_months = n * 12
        monthly_payment = (P * i * (1 + i) * loan_term_months) / ((1 + i) * loan_term_months - 1)
        monthly_payment = round(monthly_payment,2)
        
        msg= "Monthly EMI payment = "+str(monthly_payment)
        return render(request,'homeloan.html',{'r':msg}) 
    return render(request,'homeloan.html')

def eduloanaction(request):
    if request.method=="POST":
       
        d=request.POST
        for key,value in d.items():
            if key=="amount":
                P=float(value)
            if key=="interest":
                inter=float(value)
            if key=="time":
                n=float(value)
            
        
        i = inter/100/12
        loan_term_months = n * 12
        monthly_payment = (P * i * (1 + i) * loan_term_months) / ((1 + i) * loan_term_months - 1)
        monthly_payment = round(monthly_payment,2)
        
        msg= "Monthly EMI payment = "+str(monthly_payment)
        return render(request,'eduloan.html',{'r':msg}) 
    return render(request,'eduloan.html')
    
