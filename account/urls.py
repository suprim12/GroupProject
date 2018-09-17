from django.conf.urls import url
from .views import login, register, profile, add_skill, add_experience, add_degree, add_project, add_cv, company_profile, job_details, job_update, job_delete, add_vacancy, companyprofile
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    # url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^experience/submit', add_experience, name='add_experience'),
    url(r'^skill/submit', add_skill, name='add_skill'),
    url(r'^degree/submit', add_degree, name='add_degree'),
    url(r'^project/submit', add_project, name='add_project'),
    url(r'^cv/submit',  add_cv, name='add_cv'),
    url(r'^companyprofile/$', company_profile, name='company_profile'),
    url(r'^company/profile/$', companyprofile, name='companyprofile'),
    url(r'^job/(?P<id>[0-9]+)/$', job_details, name='job_details'),
    url(r'^job/(?P<id>[0-9]+)/update/$', job_update, name='job_update'),
    url(r'^job/(?P<id>[0-9]+)/delete/$', job_delete, name='job_delete'),
    url(r'^companyprofile/add-vacancy', add_vacancy, name='add_vacancy'),
    url(r'^login/', login,
        {'template_name': 'login.html'}, name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
