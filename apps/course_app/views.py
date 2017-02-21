from django.shortcuts import render,redirect
from .models import Course

def index(request):
    context = {
        "courses": Course.objects.all() # select * from Course
    }
    return render(request,"course_app/index.html", context)

def add_course(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    print ( Course.objects.all() )
    print ( Course.objects.all() )
    return redirect('/')

def remove_course(request,id):
    context = {
        "courses": Course.objects.get(id=id)
    }
    print Course.objects.get(id=id).name
    print Course.objects.get(id=id).description
    return render(request,"course_app/remove.html", context)

def delete_course(request):
    print "DELETING"
    Course.objects.get(id=request.POST['id']).delete()
    # course = Course.objects.get(id=request.POST['id'])
    # Entry.objects.filter(course).delete()
    return redirect('/')
