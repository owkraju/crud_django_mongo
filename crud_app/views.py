from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import EmployeeData
def home(request):
	data=EmployeeData.objects.all()
	return render(request,'index.html',{'data':data})
	
def addd(request):
	
	if request.method=="POST":
		data=EmployeeData(name=request.POST['name'])
		data.save()
		return redirect("crud_app:home")
		
	else:
			
		return render(request,'add.html')
	

	
def update(request,pk):
	data=EmployeeData.objects.get(name=pk)
	if request.method=="POST":
		n=request.POST['name']
		print (n)
		data.name=n
		data.save()
		return redirect('crud_app:home')
	else: 
		
		return render(request,'update.html',{'data':data})
def delete(request,pk):
	data=EmployeeData.objects.get(name=pk)
	data.delete()
	return redirect('crud_app:home')
	

