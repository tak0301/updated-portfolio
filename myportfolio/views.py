from django.shortcuts import get_object_or_404, render

from .models import Project

import smtplib

def index(request):
    latest_project_list = Project.objects.order_by('-pub_date')[:5]
    context = {
        'latest_project_list': latest_project_list,
    }
    if request.method == 'POST':
        content = """
            From: %s
            Subject: "From Portfolio"

            %s
            """ % (request.POST['user_email'], request.POST['user_message'])
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('tak0301@gmail.com', 'phbsjcaolkjijfcp')
        mail.sendmail('tak0301@gmail.com', 'tak0301@gmail.com', content)
        mail.close()
        return render(request, 'projects/index.html', context)
    return render(request, 'projects/index.html', context)

def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        content = """
            From: %s
            Subject: "From Portfolio"

            %s
            """ % (request.POST['user_email'], request.POST['user_message'])
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('tak0301@gmail.com', 'phbsjcaolkjijfcp')
        mail.sendmail('tak0301@gmail.com', 'tak0301@gmail.com', content)
        mail.close()
        return render(request, 'projects/detail.html', {'project': project})
    return render(request, 'projects/detail.html', {'project': project})
