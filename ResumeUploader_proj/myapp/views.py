from django.shortcuts import render
from myapp.forms import ResumeForm
from myapp.models import Resume
from django.views import View
# Create your views here.

class HomeView(View):
    def get(self,request):
        form=ResumeForm()
        candidate=Resume.objects.all() 
        return render(request,'myapp/home.html',{'candidate':candidate,'form':form})
    def post(self,request):
        form=ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'myapp/home.html',{'form':form})
         
class CandidateView(View):
    def get(self,request,pk):
        #print(pk)
        candidate=Resume.objects.get(pk=pk)  
        return render(request,'myapp/candidate.html',{'candidate':candidate })
