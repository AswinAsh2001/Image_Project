from django.shortcuts import render,redirect
from .models import emp_details

# Create your views here.

def base(request):
    return render(request,'base.html')

def add_emp(request):
    if request.method == 'POST':
        a = request.POST['emp_name']
        b = request.POST['emp_num']
        c = request.POST['emp_add']
        d = request.FILES.get('file')
        details = emp_details(emp_name=a,emp_num=b,address=c,image=d)
        details.save()
    return redirect('show_emp')

def show_emp(request):
    det = emp_details.objects.all()
    return render(request,'show.html',{'det':det})

def editpage(request,pk):
    det = emp_details.objects.get(id=pk)
    return render(request,'edit.html',{'det':det})

def edit_emp(request,pk):
    if request.method == 'POST':
        details = emp_details.objects.get(id=pk)
        details.emp_name = request.POST.get('emp_name')
        details.emp_num = request.POST.get('emp_num')
        details.address = request.POST.get('emp_add')
        details.image = request.FILES.get('file')
        details.save()
        return redirect('show_emp')
    else:
        return render(request,'edit.html')
