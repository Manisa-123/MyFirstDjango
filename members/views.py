from json import load
from re import M, template
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Members

# def index(request):
#     return HttpResponse("Hello world!")
    

# def index(request):
#       template = loader.get_template('myfirst.html')
#       return HttpResponse(template.render())

# def index(request):
#   mymembers = Members.objects.all().values()
#   output = ""
#   for x in mymembers:
#     output += x["firstname"]+ " " + x["lastname"]
#   return HttpResponse(output)

# def index(request):
#     mymembers = Members.objects.all().values()
#     output = []
#     for x in mymembers:
#         output.append(x["firstname"])
#         output.append(" ")
#         output.append(x["lastname"])
#         output.append("\n")

    # return HttpResponse(output)
def index(request):
    mymembers = Members.objects.all().order_by('-firstname').values()
    template = loader.get_template('index.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  member = Members(firstname=x, lastname=y)
  member.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request,id):
    member = Members.objects.all().get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
    'mymember': mymember,
  }
    return HttpResponse(template.render(context, request))



def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  member = Members.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('index'))

# def testing(request):
#     template= loader.get_template("testing.html")
#     context ={
#           "firstname" : "Bujii",
#           "greeting" : 5,
#           "day" : "Frday"
#       }
#     return HttpResponse(template.render(context, request))



# def testing(request):
#     mymembers = Members.objects.all().values()
#     template = loader.get_template('testing.html')
#     context = {
#     'mymembers': mymembers,
#     }
#     return HttpResponse(template.render(context, request))
 