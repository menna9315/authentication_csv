import csv
from django.shortcuts import render ,HttpResponse
from django.contrib.auth import authenticate, login


# Create your views here.
def home(request):
  return render(request, "home.html")



def login(request):
    if request.method == "POST":
        with open('/home/menna/django_task/auth_csv/login/data.csv') as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            next(csvReader, None)

            names=[]
            passwords=[]
            for row in csvReader:
                name=row[0]
                passw=row[1]
                names.append(name)
                passwords.append(passw)
            for index, value in enumerate(names):
                if names[index] ==request.POST['username']:
                    for idx, val in enumerate(passwords):
                        if passwords[idx] == request.POST['password']:
                            if idx == index:
                                return render(request, "home.html")

    return render(request, "login.html")


            
       
       
























        

       
    
     

            
            


       
   


    
 
  


       


    
