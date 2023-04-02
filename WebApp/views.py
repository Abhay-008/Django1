from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .forms import NameForm,Employeeform,Students
from .models import Employee, Movie
from django.core.paginator import Paginator
from rest_framework.views import APIView
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

def index(request):
    return HttpResponse("My First Webpage from Django")

def about(request):
    return HttpResponse( "about.html")

def abhay(request):
    return render(request,"home2.html")    

def index(request):
    return render(request,"detail-page.html")  

# def showdata(request):
#     #name=["Abhay","Dharmendra","Rahul","Ajay","Golu"]
#     data=[{'name':'Abhay','phone':'1233445'},{'name':'Dhr','phone':'1233445'},{'name':'Rahul','phone':'1233445'}, 
#           {'name':'Golu','phone':'1233445'}]
    
#     return render(request,"showdata.html"{'data':data})

def getdata(request,id):
    if id==1:
        return HttpResponse("Abhay")
    elif id==2:
        return HttpResponse("Dhr") 
    elif id==3:
        return HttpResponse("Golr") 
    else:
        return HttpResponse("unknown data")          


def getformdata(request):
    result=0
    if request.method=="POST":
        number_1=request.POST['n1']
        number_2=request.POST['n2']
        operation=request.POST['Operation']

        if operation=='+':
            result=int(number_1)+int(number_2)
        elif operation=='-':
            result=int(number_1)-int(number_2)
        elif operation=='*':
            result=int(number_1)*int(number_2)
        elif operation=='/':
            result=int(number_1)/int(number_2)
        #return HttpResponseRedirect("/result/?res=%s"%str(result))
               
        
        print(number_1,number_2,operation)

    return render(request,"forms.html")
    
def getdata_form(request):
    form=NameForm()
    return render(request,"pyform.html",{'form':form})    

def result(request):
    result=0
    if request.method=="POST":
        number_1=request.POST['n1']
        number_2=request.POST['n2']
        operation=request.POST['Operation']

        if operation=='+':
            result=int(number_1)+int(number_2)
        elif operation=='-':
            result=int(number_1)-int(number_2)
        elif operation=='*':
            result=int(number_1)*int(number_2)
        elif operation=='/':
            result=int(number_1)/int(number_2)



    return render(request,'result.html',{'result':result})    

    #return HttpResponse("RESULT:"+res)       

def getdata_db(request):
    emp=Employee.objects.get(name="Abhay")
    print(emp.name)
    print(emp.age)
    print(emp.sal)
    return HttpResponse("Done")


def getdata_db(request):
    emp=Employee.objects.all()
    return render(request,"showdata_db.html",{'data':emp})


def getdetail(request,id):
    emp=Employee.objects.get(id=id)
    name=emp.name
    age=emp.age
    sal=emp.sal
    print(sal)
    data={'name':name,'age':age,'sal':sal}
    return render(request,'showdetail.html',data)


def create(request):
    if request.method=="POST":
        form= Employeeform(request.POST)
        if form.is_valid():
            form.save()
    else:
            form=Employeeform() 


    return render(request,"signup.html",{'form':form})       


def update(request,id):
    emp=Employee.objects.get(id=id)
    form=Employeeform(instance=emp)
    if request.method=="POST":
        form=Employeeform(request.POST,instance=emp)
        if form.is_valid():
            form.save()
    else:
        form=Employeeform(instance=emp)

    return render(request,"update.html",{'form':form})        




def delete(request,id):
    emp=Employee.objects.get(id=id)
    if request.method=="POST":
        emp.delete()
    return render(request,"delete.html")    



def movies(request):
    movies=Movie.objects.all()
    paginator=Paginator(movies,4)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request=request, template_name="movies.html", context={'movies':page_obj})



def set_cookie(request):  
    response = HttpResponse("Cookie Set")  
    response.set_cookie('Name', 'Ducat')  
    return response

def get_cookie(request):  
    try:
        data=request.COOKIES["Name"] 
        return HttpResponse("Name:"+data)
    except:
        return HttpResponse("Data not Found")


def del_cookie(request):  
    
    response=HttpResponse("Cookies Deleted")
    response.delete_cookie("Name")
    return response


class StudentView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = Students.objects.all()  
        serializers = StudentSerializer(result, many=True)  
        return Response({'status': 'success', "students":serializers.data}, status=200)  
  
    def post(self, request):  
        serializer = StudentSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)