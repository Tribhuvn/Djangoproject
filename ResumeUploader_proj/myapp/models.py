from django.db import models

# Create your models here.

STATE_CHOICE=(
    ("Andhra Pradesh","Andhra Pradesh"), 
    ("Arunachal Pradesh","Arunachal Pradesh"),
    ("Assam","Assam"),
    ( "Bihar", "Bihar"),
    ("Chhattisgarh","Chhattisgarh"),
    ( "Goa", "Goa"),
    ("Gujarat","Gujarat"),
    ("Haryana","Haryana"),
    ( "Himachal Pradesh", "Himachal Pradesh"),
    ("Jammu and Kashmir","Jammu and Kashmir"),
    ("Jharkhand","Jharkhand"),
    ("Karnataka","Karnataka"),
    ("Kerala","Kerala"),
    ("Madhya Pradesh","Madhya Pradesh"),
    ("Maharashtra","Maharashtra"),
    ("Manipur","Manipur"),
    ("Meghalaya","Meghalaya"),
    ("Mizoram","Mizoram"),
    ("Nagaland","Nagaland"),
    ("Odisha","Odisha"),
    ("Punjab","Punjab"),
    ("Rajasthan","Rajasthan"),
    ("Sikkim","Sikkim"),
    ("Tamil Nadu","Tamil Nadu"),
    ("Telangana","Telangana"),
    ("Tripura","Tripura"),
    ("Uttarakhand","Uttarakhand"),
    ("Uttar Pradesh","Uttar Pradesh"),
    ("West Bengal","West Bengal"),
    ("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
    ( "Chandigarh", "Chandigarh"),
    ("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),
    ("Daman and Diu","Daman and Diu"),
    ("Delhi","Delhi"),
    ("Lakshadweep","Lakshadweep"),
    ( "Puducherry", "Puducherry")
)

class Resume(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(auto_now=False,auto_now_add=False)
    gender=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=20)
    pin=models.PositiveIntegerField()
    state=models.CharField(choices=STATE_CHOICE, max_length=50)
    mobile=models.PositiveIntegerField()
    email=models.EmailField()
    job_city=models.CharField(max_length=50)
    profile_image=models.ImageField(upload_to='profileimg',blank=True)
    my_file=models.FileField(upload_to='document',blank=True)

