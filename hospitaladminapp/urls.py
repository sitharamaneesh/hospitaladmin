from django.urls import path ,include
from. import views
from django.conf.urls.static import static
from hospitaladmin import settings
urlpatterns=[
    path('',views.home,name='home'),
    path('staffloginpage',views.staffloginpage,name='staffloginpage'),
    path('staffhomepage',views.staffhomepage,name='staffhomepage'),
    path('addInpatient',views.addIn,name="addInpatient"),
    path('saveInpatient',views.saveIn,name='saveInpatient'),
    path('doctorview',views.viewdoc,name='doctorview'),
    path('addOutpatient',views.addOut,name='addOutpatient'),
    path('saveOut',views.saveOut,name='saveOut'),
    path('drloginpage',views.drloginpage,name='drloginpage'),
    path('drhomepage',views.drhomepage,name='drhomepage'),
    path('addprescription',views.addprescription,name='addprescription'),
    path('pharmacy',views.pharmapage,name='pharmacy'),
    path('bill',views.pharmbill,name='bill'),
    path('discharge',views.dischargepat,name='discharge'),
    path('dischargebill',views.disbill,name='dischargebill'),
    path('inpatientbill',views.patbill,name='inpatientbill'),
    path('inpat',views.inpat,name='inpat'),
    path('addrecordpage',views.addrecordpage,name='addrecordpage'),
    path('saverecord',views.addrecord,name='saverecord'),
    path('outpat',views.outpat,name='outpat'),
    path('addprescriptionpage',views.addprescriptionpage,name='addprescriptionpage'),
    path('covid',views.covidinfo,name='covid')

]+static(settings.STATIC_URL)