from django.shortcuts import render
from Base_App .models import *
# Create your views here.

def HomeView(request):
    return render(request, 'home.html')

def MenuView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    return render(request, 'menu.html', {'items': items, 'list': list})

def AboutView(request):
    return render(request, 'about.html')

def Book_TableView(request):
    if request.method == 'POST':
        name = request.POST.get('user_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('user_email')
        total_person = request.POST.get('total_person')
        booking_date = request.POST.get('booking_date')
        
        if name != '' and email != '' and total_person != 0 and booking_date != '':
            data = BookTable(Name=name, Phone_number=phone_number, Email=email, Total_Person=total_person, booking_date=booking_date)
            data.save()

    return render(request, 'book_table.html')