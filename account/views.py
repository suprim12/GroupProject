from django.shortcuts import render,redirect
from .admin import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import User
from employeeprofile.models import EmployeeProfile,Experience,Skill,Degree,Project,Cv
from random import randint
from .forms import EmployeeProfileForm,ExperienceForm,SkillForm,DegreeForm,ProjectForm,CVForm,JobForm,CompaProfileForm
from companyprofile.models import Company,Jobs
# Create your views here.
def register(request):
    name = ["Ava","Fatima","Shankar","Daniel","Lucia","Mohan","Nepali"]
    if request.method=='GET':
        context={
        'form':UserCreationForm()
        }
        return render(request,'register.html',context)
    else:
        form=UserCreationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                who = request.POST.get('is_employee')
                email=request.POST.get('email')
                password=request.POST.get('password1')
                user = User.objects.latest('id');
                print(who)
                if who is not None:
                    myname = name[randint(0,len(name)-1)]
                    about  = "your account setup is completed please change your details, your name, about you and your details are randomly generated please go through the <i class='fa fa-pencil'></i> icon at the left side"
                    address = "Kirtipur Kathmandu Nepal"
                    contact = "+977 984xxxxxxx"
                    employee = EmployeeProfile(name=myname,about=about,address=address,contact=contact,user=user)
                    employee.save()
                else:
                    cname = "Company Name Here"
                    ad = "Kathmandu"
                    con = "9841xxxxx"
                    co = Company(company_name=cname,address=ad,contact=con,user=user)
                    co.save()
                return redirect('login')
            except:
                return render(request,'register.html',{'form':form})
        else:
            context={
            'form':form
            }
            return render(request,'register.html',context)
def company_profile(request):
    if request.method=='GET':
        company = Company.objects.get(user_id=request.user.id)
        print(request.user.id)
        context = {
        'vacancy':Jobs.objects.filter(company_id=company.id),
        }
        return render(request,'list_vacancy.html',context)
    else:
        pass
def companyprofile(request):
    cmp = Company.objects.get(user_id=request.user.id)
    form = CompaProfileForm(request.POST or None,request.FILES or None,instance=cmp)
    context={
            'company':cmp,
            'company_form':form,
        }
    if form.is_valid():
        myform = form.save(commit=False)
        myform.user= User.objects.get(id=request.user.id)
        myform.save()

    return render(request,'company_profile_update.html',context)

@login_required
def add_vacancy(request):
    if request.method=='GET':
        context = {
        'form':JobForm(),
        }
        return render(request,'add_vacancy.html',context)
    else:
        id = request.user.id
        user = User.objects.get(id=id)
        if user.is_employee:
            return redirect('login')
        else:
            company = Company.objects.get(user_id = user)
            form = JobForm(request.POST)
            if form.is_valid():
                vacancy = form.save(commit=False)
                vacancy.company = company
                vacancy.save()
                return redirect('company_profile')


@login_required
def profile(request):
    id = request.user.id;
    if isemployee(id) == False:
        return redirect('company_profile')
    employee = EmployeeProfile.objects.get(user_id=id)
    empform = EmployeeProfileForm(request.POST or None,request.FILES or None,instance=employee)
    experience = Experience.objects.filter(user_id=request.user.id)
    skill = Skill.objects.filter(user_id=request.user.id)[:7]
    degree = Degree.objects.filter(user_id=request.user.id)[:7]
    pro = Project.objects.filter(user_id=request.user.id)[:7]
    cv = Cv.objects.filter(user_id=request.user.id)[:7]
    if empform.is_valid():
        emp = empform.save(commit=False)
        emp.user = User.objects.get(id=request.user.id)
        emp.save()
    return render(request,'profile.html',{'emp':employee,'empform':empform,
    'experienceform':ExperienceForm(),'exp':experience,'skillform':SkillForm,'skill':skill,
    'degreeform':DegreeForm(),'degree':degree,'projectform':ProjectForm(),
    'project':pro,
    'cvForm':CVForm,
    'cv':cv,
    })

@login_required
def add_experience(request):
    if request.method=='POST':
        experience = ExperienceForm(request.POST)
        if experience.is_valid():
            exp = experience.save(commit=False)
            exp.user = User.objects.get(id=request.user.id)
            exp.save()
        return redirect('profile')
    else:
        return redirect('profile')
@login_required
def add_project(request):
    if request.method=='POST':
        project = ProjectForm(request.POST)
        if project.is_valid():
            pro = project.save(commit=False)
            pro.user = User.objects.get(id=request.user.id)
            pro.save()
        return redirect('profile')
    else:
        return redirect('profile')
@login_required
def add_skill(request):
    if request.method=='POST':
        skill = SkillForm(request.POST)
        if skill.is_valid():
            skill = skill.save(commit=False)
            skill.user = User.objects.get(id=request.user.id)
            skill.save()
        return redirect('profile')
    else:
        return redirect('profile')
@login_required
def add_degree(request):
    if request.method=='POST':
        degree = DegreeForm(request.POST)
        if degree.is_valid():
            degree = degree.save(commit=False)
            degree.user = User.objects.get(id=request.user.id)
            degree.save()
        return redirect('profile')
    else:
        return redirect('profile')

@login_required
def add_cv(request):
    if request.method=='POST':
        cv = CVForm(request.POST or None,request.FILES)
        if cv.is_valid():
            cv_ = cv.save(commit=False)
            cv_.user = User.objects.get(id=request.user.id)
            cv_.save()
        return redirect('profile')
    else:
        return redirect('profile')

def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        pass


def job_details(request,id):
    context={
    'job':Jobs.objects.get(id=id),
    }
    return render(request,'job_details.html',context)

def job_update(request,id):
    job = Jobs.objects.get(id=id)
    form = JobForm(request.POST or None,instance=job)
    if form.is_valid():
        company = Company.objects.get(user_id=request.user.id)
        myform = form.save(commit=False)
        myform.company=company
        myform.save()
    context = {
    'job':job,
    'form':form,
    }
    return render(request,'job_update.html',context)
@login_required
def job_delete(request,id):
    job = Jobs.objects.get(id=id)
    job.delete()
    return redirect('company_profile')

def isemployee(id):
    user = User.objects.get(id=id)
    return user.is_employee
