from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from .forms import UploadFileForm
from django.http import JsonResponse

def handle_uploaded_file(f):
    print("String 3: " + f.name)
    with open("success.html", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    #UploadedFile.read(f)

def index(request):
    return render(request, 'loadingpage.html', {'name': "David"})

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
        handle_uploaded_file(request.FILES["file"])
        if form.is_valid():
            print("Second: " + request.FILES['file'].name)
            handle_uploaded_file(request.FILES["file"])
            return HttpResponseRedirect("/success/url/")
    else:
        form = UploadFileForm()
    return render(request, "loadingpage.html", {"form": form})

#def detail(request, question_id):
#    return HttpResponse("You're looking at question %s." % question_id)
#
#
#def results(request, question_id):
#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % question_id)
#
#
#def vote(request, question_id):
#    return HttpResponse("You're voting on question %s." % question_id)