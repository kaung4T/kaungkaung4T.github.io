from django.shortcuts import render, redirect
from django.http import HttpResponse
from display.models import About
from display.models import Skill, Project, SchoolProject, Education, Education_tran
from display.models import Project
from display.models import SchoolProject
from display.models import Education
from matplotlib import pyplot
import io
import urllib, base64
from django.core.mail import EmailMessage, send_mail
from django.contrib import messages
from django.http import JsonResponse
from display.models import Education_tran

# Create your views here.


def work(request):

    context = {
        "name": "kaung",
        "age" : 22
    }

    return render(request, "work.html",
                    {"context":context})


def home(request):
    about = About.objects.all()
    if request.method == "POST":
        email = request.POST["email"]
        title = request.POST["title"]
        text = request.POST["text"]

        e = EmailMessage(subject=title, body=text, from_email=email, to=["mrkaungminnkhant@gmail.com"], cc=[email])
        try:
            e.send()
        except Exception as e:
            messages.info(request, "Sry, message didnt send.")
            return redirect("/")

        messages.success(request, "Message has been sent")
        return redirect("/")

    return render(request, "index.html",
                 {"About":about})


def profile(request):
    return render(request, "profile.html")


def skill(request):
    s = Skill.objects.all()
    return render(request, "skill.html",
                  {"skill":s})

def project(request):
    p = Project.objects.all()
    s = SchoolProject.objects.all()
    return render(request, "project.html",
                  {"project":p, "school":s})



def project2(request, pk):
    p = Project.objects.get(id=pk)
    return render(request, "project2.html",
                  {"project": p})


def education(request):

    e = Education.objects.all()
    edu = Education_tran.objects.all()
    # a = ["Level 3", "Level 4", "Level 5", "Level 6"]
    # year1 = [1, 4, 7, 9]
    # year2 = [2, 5, 8, 13]
    # year3 = [3, 6, 9, 14]
    # year4 = [4, 11, 15, 20]
    # p = pyplot
    # color = {
    #     "xtick.color": "#0d6efd",
    #     "ytick.color": "#0d6efd"
    # }
    # p.rcParams.update(color)
    #
    #
    # answer1 = p.plot(a, year1)
    # answer2 = p.plot(a, year2)
    # answer3 = p.plot(a, year3)
    # answer4 = p.plot(a, year4)
    #
    # change = p.gcf()
    #
    # byte = io.BytesIO()
    # change.savefig(byte, format="png", transparent=True)
    # byte.seek(0)
    # text = base64.b64encode(byte.read())
    # uri = urllib.parse.quote(text)

    return render(request, "education.html",
                  {"education":e, "edu":edu})


