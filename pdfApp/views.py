from django.shortcuts import render, HttpResponse
import re
import pdfplumber
import pandas as pd
from collections import namedtuple

# Create your views here.
def home(request):
    if request.method =="POST":
        file = request.FILES["myFile"]

        name_regex = re.compile(r'\n[A-Z]+(?:\s+[A-Z]+)*\b')

        phoneNumber_regex = re.compile(r'^Mobile :[\s\d{11}]+$')

        dob_regex = re.compile(r'^Date of Birth:[\s\d+/[a-zA-z+]/\d{4}]+$')

        email_regex = re.compile(r'''(
            [._%+-a-zA-z0-9]+
            @
            [a-zA-z0-9.-]+
            \.[a-zA-Z]{2,4}
            )''', re.VERBOSE)

        phone_list = []
        name_list = []
        email_list = []

        total_check = 0

        with pdfplumber.open(file) as pdf:
            pages = pdf.pages
            for page in pdf.pages:
                text = page.extract_text()

                # matches = re.findall(r'\n[A-Z]+(?:\s+[A-Z]+)*\b', text)

                name = name_regex.findall(text)
                if name != None :
                    name_list.append(name)
                
                for line in text.split('\n'):

                    phone = phoneNumber_regex.search(line)
                    if phone != None :
                        phone_list.append(phone.string)

                    for email in email_regex.findall(line):
                        if email != None :
                            email_list.append(email)
        # print(phone_list)
        # print(name_list[0][0])
        # print(email_list)
        # csv = pd.read_csv(file)
        # print(csv.head())
        # arr = csv["sum"]
        # sumation = sum(arr)
        
        return render(request, "index.html", {"something": True, "phone": phone_list[0], "name":name_list[0][0], "email":email_list[0]})
    else:
        return render(request, "index.html")

def upload(request):
    return render(request, "fileupload.html")