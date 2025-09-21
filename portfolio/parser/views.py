from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm
import json
from django.http import JsonResponse

def handle_uploaded_file(f):
    print("String 3: " + f.name)
    #print(json.loads(str(f.read())))
   #works# print(f.read().decode().splitlines())
    print("#########################")
    #data_file = json.load(f, "r")
    #print(data_file)
    #data_file.close()
    dataString = str(f.read().decode().splitlines())
    #print(dataString)
    dataDict = json.loads(dataString)
    print(dataDict)
    #with open("example.json", "r") as my_file:
    #    dataFile = json.load(my_file)
    
    #print("LLLLLL " + dataFile)
    #print(json.load("example.json"))

    with open("success.html", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def index(request):
    return render(request, 'loadingpage.html', {'page': "Index"})

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         file = request.FILES['file']
#         return HttpResponse("Name of file: ") #+ str(file))
#     else:
#         form = UploadFileForm()
#     return render(request, 'loadingpage.html', {'from': form})
 
def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        print("First: " + request.FILES['file'].name)
        file = request.FILES["file"]
        #print(file.read()) 

        #file.open()
        handle_uploaded_file(file)
        #with open(file.open(), "r") as my_file:
        #    dataFile = json.load(my_file)
        #    print(dataFile)
#

        if form.is_valid():
            print("Second: " + request.FILES['file'].name)
            handle_uploaded_file(request.FILES["file"])
            return HttpResponseRedirect("/success/url/")
    else:
        form = UploadFileForm()
    return render(request, "loadingpage.html", {"form": form})

def analyze_file(request, form):
    return render(request, 'success.html', {'file': form})
