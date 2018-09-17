from django.shortcuts import render
from general.models import Slider,Testimonial,Blog
from companyprofile.models import Company,Jobs
from django.contrib.auth.models import User
from employeeprofile.models import EmployeeProfile,Skill
import re, math
import numpy as np
import pandas as pd
from collections import Counter
WORD = re.compile(r'\w+')

def home(request):
    try:
        if request.user.is_authenticated():
            employee= EmployeeProfile.objects.get(user_id=request.user.id)
            myskill = Skill.objects.filter(user_id=request.user.id)
            myjob = Jobs.objects.all()
            myid = myfilterid(myskill,myjob)
            myjob = Jobs.objects.filter(id__in=myid)
        else:
            print("not login")
            myjob = Jobs.objects.all()
    except:
        print("error occ")
        myjob = Jobs.objects.all()
    context={
        'Slider':Slider.objects.all(),
        'testimonial':Testimonial.objects.all()[:4],
        'vacancy':myjob,
    }
    return render(request,'home.html',context)

def contact_us(request):
    return render(request,'contactus.html')

def blog(request):
    context = {
    'blog':Blog.objects.all(),
    'blogf':Blog.objects.all()[:3],
    }
    return render(request,'blog-rightside-bar.html',context)
def blog_details(request,id):
    context = {
    'blog':Blog.objects.get(id=id),
    }
    return render(request,'blog_rightside_bar_details.html',context)
def search(request):
    if request.method=='POST':
        context={
        'vacancy':Jobs.objects.filter(job_title__contains=request.POST.get('key'))
        }
        return render(request,'search_result.html',context)
    else:
        return redirect('home')
def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def myfilterid(myskill,myjob):
    m=""
    joblist_id=[]
    cosine_value =[]
    for s in myskill:
        m=s.skill+" "+m
    vector1 = text_to_vector(m)
    for x in myjob:
        joblist_id.append(x.id)
        a = text_to_vector(x.job_title.split()[0]+","+x.skills)
        cosine_value.append(get_cosine(vector1,a))
    print(cosine_value)
    index = list(range(0,len(joblist_id)))
    df = pd.DataFrame({'id':joblist_id,'cosine':cosine_value},index=index)
    df = df[(df['cosine']>0.1)]
    myid = df['id'].values
    myid=myid.tolist()
    return myid
