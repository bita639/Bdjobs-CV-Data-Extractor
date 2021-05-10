from django.shortcuts import render, HttpResponse
import pandas as pd
# Create your views here.
def home(request):
    if request.method =="POST":
        file = request.FILES["myFile"]
        csv = pd.read_csv(file)
        print(csv.head())
        arr = csv["sum"]
        sumation = sum(arr)
        return render(request, "index.html", {"something": True, "sum": sumation})
    else:
        return render(request, "index.html")

def upload(request):
    return render(request, "fileupload.html")