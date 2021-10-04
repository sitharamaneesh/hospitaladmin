from datetime import date, datetime
from functools import reduce
from django import http
from django.db.models.fields import DecimalField
from decimal import Decimal
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import  InpatientForm,MedicineForms
from .models import Inpatient,discharge, Outpatient,doctor, medicine, pharmacy,stafflogin,nurse,medicalrecord,covid
def home(request):
    return render(request,'home.html')

def staffloginpage(request):  
    return render(request,"stafflogin.html")

def staffhomepage(request):
    try:
        errormsg={}
        name=request.POST['name']
        pwd=request.POST['pwd']
        auth=stafflogin.objects.get(name=name,password=pwd)
        if auth:
            return render(request,'staffhomepage.html',{'user':name})
        else:
            errormsg['msg']="Invalid login"
            return render(request,'stafflogin.html',errormsg)
    except Exception as e:
        print(e)
        errormsg['msg']="Error"
        return render(request,'stafflogin.html',errormsg)

def addIn(request):
    formobj=InpatientForm()
    return render(request,'addInpatient.html',{'form':formobj})

def addOut(request):
    return render(request,'addOutpatient.html')

def saveIn(request):
    try:
        errormsg={}
        form=InpatientForm(request.POST)
        print(form['number'].value())
        num=form['number'].value()
        obj=Inpatient.objects.filter(number=num)
        print(obj)
        num1=Inpatient.objects.filter(number=num)
        print(num1)
        if num1.exists():
            msg="Number Exist"
            return redirect('addInpatient.html',{"msg":msg,"form":form})
        elif form.is_valid():
                form.save()
                msg="Data Added"
                return redirect('addInpatient')
        else:
            msg="Data Not Added"
            return render(request,'addInpatient.html',{"msg":msg,"form":form})
    except Exception as e:
        print(e)
        return HttpResponse("Error")

def viewdoc(request):
    try:
        obj=doctor.objects.all()
        print(obj)
        return render(request,'doctorview.html',{'doc':obj})
    except Exception as e:
        print(e)
        return HttpResponse("error")

def saveOut(request):
    try:
        errormsg={}
        name=request.POST['name']
        address=request.POST['address']
        email=request.POST['email']
        number=request.POST['number']
        doctor=request.POST['doctorname']
        age=request.POST['age']
        gender=request.POST['gender']
        obj=Outpatient.objects.filter(number=number)
        obj1=Inpatient.objects.filter(number=number)
        if obj and obj1:
            print("hello")
            errormsg["msg"]="Contact exist"
            return render(request,'addOutpatient.html',errormsg)
        else:
            print("else")
            obj=Outpatient(name=name,address=address,email=email,number=number,doctorname=doctor,age=age,gender=gender)
            obj.save()
            print("save")
            obj3=Outpatient.objects.filter(name=name)
            print(obj3)
            for i in obj3.values():
                print("for")
                tok=i['id']+i['token']
            obj3.update(token=tok)
            print("update")
            errormsg['msg']="Token number:"+str(tok)
            return render(request,'addOutpatient.html',errormsg)
    except Exception as e:
        print(e)
        return HttpResponse("Error")


def drloginpage(request):
    return render(request,"drlogin.html")


   

def drhomepage(request):
    try:
        print("loginvalidate")
        errormsg={}
        drname=request.POST['name']
        drpwd=request.POST['pwd']
        auth=doctor.objects.filter(name=drname,password=drpwd)
        dep=doctor.objects.filter(name=drname).values('department')[0]
        nur=nurse.objects.filter(department=dep['department']).values('name')[0]
        global dname
        def dname():
            return drname
        if auth:
            return render(request,'drpage.html',{'user':drname,'dr':auth,'nurse':nur['name']})
        else:
            errormsg['msg']="Invalid login"
            return render(request,'drlogin.html',errormsg)
    except Exception as e:
        print(e)
        errormsg['msg']="Error"
        return render(request,'drlogin.html',errormsg)

n=''
idno=0


def pharmapage(request):
    obj=pharmacy.objects.filter(paid=False)
    dis=discharge.objects.all()
    return render(request,'pharmacy.html',{'obj':obj,'dis':dis})

def pharmbill(request):
    val=request.POST['bill']
    pat=Outpatient.objects.filter(token=val)
    phar=pharmacy.objects.filter(token=val).values()
    medi=medicine.objects.all()
    cnt=phar.count()
    med=[]
    pri=[]
    tot=[]
    qty=[]
    for i in phar:
        name=i['name']
        qnty=i['qty']
        qty.append(qnty)
        medi=medicine.objects.filter(medname=i['medname'])
        m=medi.values('medname')[0]['medname']
        p=medi.values('price')[0]['price']
        pri.append(p)
        med.append(m)
        total=qnty*p
        tot.append(total)
    totbill=sum(tot)
    print("totalbill",totbill)
    print("total",tot)
    print("medicine",med)
    print("price",pri)
    print("qty",qty)
    pharmacy.objects.filter(token=val).update(paid=True)
    return render(request,'bill.html',{'pat':pat,'cnt':cnt,'tot':tot,'med':med,'pri':pri,'qty':qty,'totbill':totbill})

def dischargepat(request):
    try:
        id=request.POST['discharge']
        print(id)
        obj=Inpatient.objects.filter(id=id,discharged=False).values()
        name=obj.values('name')[0]['name']
        ins=obj.values('medicalcard')[0]['medicalcard']
        print(ins)
        dt=obj.values('date')[0]['date']
        nw=date.today()
        day=(dt-nw).days
        totalrent=abs(day)*500
        medrec=medicalrecord.objects.filter(no=id).values()
        medi=medicine.objects.all()
        med=[]
        pri=[]
        tot=[]
        qty=[]
        for i in medrec:
            qnty=i['qty']
            qty.append(qnty)
            medi=medicine.objects.filter(medname=i['medname'])
            m=medi.values('medname')[0]['medname']
            p=medi.values('price')[0]['price']
            pri.append(p)
            med.append(m)
            total=qnty*p
            tot.append(total)
        totbill=sum(tot)
        if ins:
            print(totbill)
            totbill=totbill*Decimal(.7)
        dis=discharge(patid=id,name=name,roomrent=totalrent,pharmbill=totbill)
        dis.save()
        Inpatient.objects.filter(id=id).update(discharged=True)
        return redirect('inpat')
    except Exception as e:
        return HttpResponse(e)

def result(request):
    return render(request,'result.html',{'msg':"Added"})

def disbill(request):
    try:
        id=request.POST['bill']
        disobj=discharge.objects.filter(patid=id).values()
        total1=disobj.values('roomrent')[0]['roomrent']+disobj.values('pharmbill')[0]['pharmbill']
        obj=Inpatient.objects.filter(id=id,discharged=True).values()
        room=Inpatient.objects.filter(id=id,discharged=True).values('roomno')
        roomno=room[0]['roomno']
        flag=False
        total2=0
        if obj.values('medicalcard')[0]['medicalcard']:
            flag=True
            total2=total1*Decimal(.7)
        discharge.objects.filter(patid=id).update(paid=True)
        return render(request,'inpatbill.html',{'dis':disobj,'tot':total1,'total':float(total2),'roomno':roomno,'flag':flag})
    except Exception as e:
        print(e)
        return HttpResponse("error")   

def patbill(request):
    try:
        dis=discharge.objects.filter(paid=False)
        return render(request,'inpatientbill.html',{'dis':dis})
    except Exception as e:
        print(e)
        return HttpResponse("Error")
    
def inpat(request):
    print("Inpat")
    dr=dname()
    print(dr)
    print("doctorname",dr)
    patin=Inpatient.objects.filter(doctorname=dr,discharged=False)
    print("patients",patin)
    return render(request,'inpatview.html',{'patients':patin})

def outpat(request):
    print("outpat")
    dr=dname()
    print("dr",dr)
    patout=Outpatient.objects.filter(doctorname=dr,date=datetime.today(),presc=False)
    print("pat",patout)
    return render(request,'outpatview.html',{'patients':patout})

def addrecordpage(request):
    print("in add record page")
    id=request.POST['addrecord']
    print(id)
    obj=Inpatient.objects.filter(id=id,discharged=False)
    print(obj)
    for i in obj.values('id'):    
        idn=i['id']
        print(idn)
    idno=idn
    obj1=medicalrecord.objects.filter(no=id)
    patient=Inpatient.objects.filter(id=id,discharged=False)
    form=MedicineForms()
    return render(request,'addrecord.html',{'records':obj1,'name':n,'id':idno,'form':form,'patient':patient})

def addrecord(request):
    try:
        if request.POST:
            print("after save button")
            p=request.POST['prescription']
            qty=request.POST['qty']
            idno=request.POST['save']
            rec=request.POST['record']
            print(idno)
            print(rec)
            print("AddPres")
            form=MedicineForms(request.POST)
            print(form['medname'].value())
            obj=Inpatient.objects.filter(id=idno,discharged=False)
            print(obj)
            p=request.POST['prescription']
            qty=request.POST['qty']
            print(p)
            for i in obj:
                pre=medicalrecord(no=idno,records=rec,name=i.name,pres=p,medname=form['medname'].value(),qty=qty)
                pre.save()
            return redirect('inpat')
    except Exception  as e:
        print(e)
        return HttpResponse("error")
        
token=0

def addprescriptionpage(request):
    try:
        val=request.POST["action"]
        print(val)
        if val!="Add prescription":
            print("prescriptionpage")
            global token
            token=request.POST['action']
            print(token)
            obj=Outpatient.objects.filter(token=token)
            med=medicine.objects.all()
            form=MedicineForms()
            print(form)
            return render(request,"prescription.html",{'patient':obj,'med':med,'form':form})
    except Exception as e:
        print(e)
        return render(request,'drhomepage.html',{'msg':"Not Added"})

def addprescription(request):
    try:
            print("AddPres")
            print(token)
            form=MedicineForms(request.POST)
            print(form['medname'].value())
            obj=Outpatient.objects.filter(token=token)
            print(obj)
            p=request.POST['prescription']
            qty=request.POST['qty']
            print(p)
            Outpatient.objects.filter(token=token).update(presc=True)
            for i in obj:
                pre=pharmacy(token=token,name=i.name,pres=p,contact=i.number,medname=form['medname'].value(),qty=qty)
                pre.save()
            
            return redirect('outpat')
    except Exception as e:
        print(e)
        return render(request,'drpage.html',{'msg':"Not Added"})

def covidinfo(request):
    obj=covid.objects.all().values()
    return render(request,'covidcare.html',{'covid':obj})
