from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')  # ตรวจสอบว่า path ตรงกับ template

def second_view(request):
    return render(request, 'second.html')  # ตรวจสอบว่า path ตรงกับ template
