from django.shortcuts import render,redirect
from django.views.generic import View,FormView,TemplateView,CreateView,ListView,UpdateView
from HR.forms import LoginForm,Categoryform,Jobform
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from Myapp.models import Category,Job
# Create your views here.

class Loginview(FormView):
    template_name="login.html"
    form_class = LoginForm

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_obj=authenticate(request,username=u_name,password=pwd)
            if user_obj:
                login(request,user_obj)
                print("success")
                if request.user.is_superuser:
                    return redirect("index")
                else:
                    return redirect("seekerindex")
            else:
                print("failed")
            return render(request,"login.html",{"form":form})


class Dashboard(TemplateView):
    template_name = "index.html"

class Signout(View):
    def get(self,request):
        logout(request)
        return redirect("signin")
    
class Addcategory(CreateView,ListView):
    template_name = "category.html"
    form_class = Categoryform
    success_url = reverse_lazy("category")
    context_object_name = "data"
    model = Category

class Categoryremove(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        Category.objects.get(id=id).delete()
        return redirect("category")

class Addjob(CreateView):
    template_name = 'job_add.html'
    form_class = Jobform
    success_url = reverse_lazy("joblist")
    # context_object_name = ("qs")
    model = Job

class Deljob(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Job.objects.get(id=id).delete()
        return redirect("joblist")

class Joblist(ListView):
    template_name ="job_list.html"
    model = Job
    context_object_name = "jobs"
    

class Jobupdate(UpdateView):
    template_name ="jobupdate.html"
    form_class = Jobform
    model = Job
    success_url = reverse_lazy('joblist')

class Jobview(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        qs = Job.objects.filter(id = id)
        return render(request,"jobview.html",{"qs":qs})