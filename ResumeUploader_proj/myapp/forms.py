from socket import fromshare
from django import forms
from myapp.models import Resume


GENDER_CHOICES=[
    ('Male','Male'),
    ('Female','Female'),
]

JOB_CITY_CHOICE=[
    ('Delhi','Delhi'),
    ('Mumbai','Mumbai'),
    ('Pune','Pune'),
    ('Bengluru','Bengluru'),
    ('Hyderabad','Hyderabad'),
    ('Noida','Noida'),
    ('Chennai','Chennai'),
]

class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    job_city=forms.MultipleChoiceField(label='City Preference',choices=JOB_CITY_CHOICE,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=Resume
        fields=['name','dob','gender','address','city','pin','state','mobile',
                'email','job_city','profile_image','my_file',]
        labels={'name':'Full Name','dob':'Date of Birth','gender':'Gender','address':'Address',
                'city':'City','pin':'Pin','state':'State','mobile':'Mobile No.','email':'Email Id','job_city':'City Preference',
                'profile_image':' Profile Image','my_file':'Document',}
        widgets= {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
