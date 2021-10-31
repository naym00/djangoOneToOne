from django.shortcuts import render, redirect
from .models import Student, RegistrationID
from  .forms import StudentForm, RegistrationIDForm

# Create your views here.
def home(request):
    text= "Student Portal"
    context = { "headLine" : text }
    return render(request, 'Home/home.html', context)

def studentList(request):
    text = "Student List"
    allStudent = RegistrationID.objects.all()
    context = { "headLine" : text, "allStudent" : allStudent }
    return render(request, 'Student/studentlist.html', context)

def insertStudent(request):
    data = StudentForm()
    text = "Fillup with your information."

    if request.method == "POST":
        text = "Not Successful!"
        data = StudentForm(request.POST)

        if data.is_valid():
            text = "Successful!"
            data.save()
            return redirect('insertstudentregistrationid')

    context = { "text" : text, "data" : data }
    return render(request, 'Student/insertStudent.html', context)

def insertStudentRegistrationID(request):
    data = RegistrationIDForm()
    text = "Fillup with your information."

    if request.method == "POST":
        text = "Not Successful!"
        data = RegistrationIDForm(request.POST)

        if data.is_valid():
            text = "Successful!"
            data.save()
            return redirect('studentlist')

    context = { "text" : text, "data" : data }
    return render(request, 'Student/insertStudentRegistrationID.html', context)