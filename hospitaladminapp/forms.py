from django import forms
from hospitaladminapp.models import Inpatient,doctor,medicine
class InpatientForm(forms.ModelForm):
 
    CHOICES= [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other','Other')
    ]

    gender= forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))
   #dep=doctor.objects.values_list('id','department')
    #dept=forms.CharField(label="Department",widget=forms.Select(choices=dep))
    doc=list(doctor.objects.values_list('name','name'))
    print(doc)
    email=forms.EmailField(required=False)
    doctorname=forms.CharField(label='doctorname',widget=forms.Select(choices=doc))
    class Meta:
        model=Inpatient
        fields="__all__"
        widgets = {
               'gender': forms.RadioSelect(),
               'doctorname':forms.Select(),
               'name': forms.TextInput(attrs={'class': 'form-control'}),
               'address': forms.TextInput(attrs={'class': 'form-control'}),
               'email':forms.EmailInput(attrs={'class':'form-control'}),
               'age':forms.NumberInput(attrs={'class':'form-control'}),
               'number':forms.NumberInput(attrs={'class':'form-control'}),
               'roomno':forms.NumberInput(attrs={'class':'form-control'}),
               'gender':forms.TextInput(attrs={'class':'form-control'}),
               
           }   
        exclude=['date','discharged']
           
class MedicineForms(forms.ModelForm):
    med=list(medicine.objects.values_list('medname','medname'))
    print(med)
    medname=forms.CharField(label='Medicine',widget=forms.Select(choices=med))
    class Meta:
            model=medicine
            fields="__all__"
            widgets = {
                
                'medname':forms.Select()
            }   
        
            exclude=['price','type']
