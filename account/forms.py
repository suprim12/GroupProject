from django.forms import ModelForm
from django import forms
from employeeprofile.models import EmployeeProfile,Experience,Skill,Degree,Project,Cv
from companyprofile.models import Jobs,Company

class EmployeeProfileForm(ModelForm):
    name = forms.CharField(label='Your Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    job_title = forms.CharField(label='JOb You Want to work ?',widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(label='Address',widget=forms.TextInput(attrs={'class':'form-control'}))
    contact = forms.CharField(label='Contact',widget=forms.TextInput(attrs={'class':'form-control'}))
    portfolio = forms.CharField(label='Portfolio if any',required=False,widget=forms.URLInput(attrs={'class':'form-control'}))
    about = forms.CharField(label='About Youself',widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = EmployeeProfile
        fields =['name','job_title','image','address','contact','portfolio','about']

class CompaProfileForm(ModelForm):
    company_name = forms.CharField(label='Company Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(label='Address',widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(label='email',widget=forms.TextInput(attrs={'class':'form-control'}))
    contact = forms.CharField(label='Contact',widget=forms.TextInput(attrs={'class':'form-control'}))
    about = forms.CharField(label='About company',widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = Company
        fields =['company_name','address','email','profile','contact','about']


class ExperienceForm(ModelForm):
    position = forms.CharField(label='Position',widget=forms.TextInput(attrs={'class':'form-control'}))
    company = forms.CharField(label='Company',widget=forms.TextInput(attrs={'class':'form-control'}))
    start_date = forms.CharField(label='Start Year',widget=forms.TextInput(attrs={'class':'form-control'}))
    end_date = forms.CharField(label='End Year(leave blank if you work currently)',required=False,widget=forms.TextInput(attrs={'class':'form-control'}))


    class Meta:
        model = Experience
        fields =['position','company','start_date','end_date']

class SkillForm(ModelForm):
    skill = forms.CharField(label='Your Skill',widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Skill
        fields =['skill']

class DegreeForm(ModelForm):
    degree_name = forms.CharField(label='Degree',widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Degree
        fields =['degree_name']

class ProjectForm(ModelForm):
    project_name = forms.CharField(label='Project Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    project_link = forms.CharField(label='Project Link',required=False,widget=forms.URLInput(attrs={'class':'form-control'}))
    class Meta:
        model = Project
        fields =['project_name','project_link']

class CVForm(ModelForm):
    cv_name = forms.CharField(label='CV Title',widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Cv
        fields =['cv_name','cv_file']

class JobForm(ModelForm):
    job_title = forms.CharField(label='Job Title',widget=forms.TextInput(attrs={'class':'form-control'}))
    skills = forms.CharField(label='skill',widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(label='Description',widget=forms.Textarea(attrs={'class':'form-control'}))


    class Meta:
        model = Jobs
        fields =['job_title','skills','description']
