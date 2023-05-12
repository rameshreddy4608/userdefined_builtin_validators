from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

from app.models import *

from app.forms import *
def insert_student_Details(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFOD=StudentForm(request.POST)
        if SFOD.is_valid():
            SFOD.save()

             # SQS=Student.objects.all()
             # d1={'SQS':SQS}
             # return render(request,'Display_Student_Details.html',d1)

            return HttpResponse(str(SFOD.cleaned_data))
        # else:
        #     return HttpResponse("data is invalid input")

    return render(request,'insert_student_Details.html',d)



def insert_course_Details(request):
    CFO=CourseForm()
    d={'CFO':CFO}
    if request.method=='POST':
        CFOD=CourseForm(request.POST)
        if CFOD.is_valid():
            CFOD.save()


            # cid=CFOD.cleaned_data['cid']
            # sid=CFOD.cleaned_data['sid']
            # cname=CFOD.cleaned_data['cname']
            # cTrainer=CFOD.cleaned_data['cTrainer']
            # SO=Student.objects.get_or_create(sid=sid)[0]
            # CO=Course.objects.get_or_create(sid=SO,cid=cid,cname=cname,cTrainer=cTrainer)[0]
            # CO.save()
            return HttpResponse(str(CFOD.cleaned_data))


            return HttpResponse("data insrted sucessfullY")
    return render(request,'insert_course_Details.html',d)