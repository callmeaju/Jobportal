from django.shortcuts import render,redirect
from jobseeker.forms import Registration,Studentprofile
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import View,CreateView,TemplateView,DetailView,UpdateView,ListView
from django.contrib.auth import authenticate,login,logout
from Myapp.models import Student,Job,Applications
from django.forms.models import BaseModelForm
from django.utils.decorators import method_decorator
# Create your views here.

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

class Register(CreateView):
    template_name ='jobseeker/register.html'
    form_class  = Registration
    model = User
    success_url = reverse_lazy("reg")

class Signout(View):
    def get(self,request):
        logout(request)
        return redirect("signin")

# class Signin(View):
#     def get(self,request,*args,**kwargs):
#         form = LoginForm()
#         return render(request,"jobseeker/login.html",{"form":form})
    
#     def post(self,request,*args,**kwargs):
#         form =  LoginForm(request.POST)
#         if form.is_valid():
#             u_name = form.cleaned_data.get("Username")
#             pwd = form.cleaned_data.get("Password")
#             user_obj = authenticate(username = u_name,password = pwd)
#             if user_obj:
#                 login(request,user_obj)
#                 print("User logged in")

#             else:
#                 print("False Credentials")

#         return redirect("reg")


# class Student_home(TemplateView):
#     template_name = "jobseeker/index.html"

@method_decorator(signin_required,name = "dispatch")
class Student_home(ListView):
    template_name = "jobseeker/index.html"
    context_object_name = "job"
    model = Job


@method_decorator(signin_required,name = "dispatch")
class Profile(CreateView):
    template_name = "jobseeker/seekerprofile.html"
    form_class = Studentprofile
    model = Student
    success_url = reverse_lazy("reg")

    # def post(self,request,*args,**kwargs):
    #     form = Studentprofile(request.POST,files=request.FILES)
    #     if form.is_valid():
    #         form.instance.user = request.user
    #         form.save()
    #         return redirect("seekerindex")
    #     else:
    #         print("invalid user")
    #     return redirect("reg")
    def form_valid(self,form:BaseModelForm):
        form.instance.user = self.request.user
        return super().form_valid(form)

@method_decorator(signin_required,name = "dispatch")
class Profileview(DetailView):
    template_name  = "jobseeker/profileview.html"
    context_object_name = "data"
    model = Student
    success_url = reverse_lazy("p_view")


# class Profileview(DetailView):
    # template_name = "jobseeker/profileview.html"
    # def get(self,request,*args,**kwargs):
    #     id = kwargs.get("pk")
    #     data = Student.objects.filter(id = id)
    #     return render(request,self.template_name,{"data":data})

@method_decorator(signin_required,name = "dispatch")
class update_profile(UpdateView):
    template_name = "jobseeker/profile_edit.html"
    form_class = Studentprofile
    model  = Student
    success_url =reverse_lazy("seekerindex")
    
# class Joblist(ListView):
#     template_name = "jobseeker/index.html"
#     model = Job
#     context_object_name = "jobs"
    

@method_decorator(signin_required,name = "dispatch")
class jobdetail(DetailView):
    template_name = "jobseeker/jobdetail.html"
    model = Job
    context_object_name = "jobview"

@method_decorator(signin_required,name = "dispatch")
class job_apply(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        data = Job.objects.get(id =id)
        Applications.objects.create(jobs=data,student=request.user)
        return redirect("seekerindex")

@method_decorator(signin_required,name = "dispatch")
class Applied_job(View):
    def get(self,request,*args,**kwargs):
        data=Applications.objects.filter(student = request.user)
        return render(request,"jobseeker/jobapplied.html",{"data":data})

class Delete_job(View):
    def get(self,request,*args,**kwargs):
        id =kwargs.get("pk")
        Applications.objects.get(id=id).delete()
        return redirect("applied")
    