from django.shortcuts import render
from .models import User, Property

def index(request):
    return render(request,'landing.html')
def property(request):
    return render(request,'property.html')

def register(request):
    return render(request,'register.html')

def user_login(request):
    print("user_login")
    return render(request,'login.html')

def register_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        is_seller = request.POST.get('is_seller')

        user = User.objects.create(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, is_seller=is_seller)
        user.save()
        return render(request, 'registration_success.html')
    return render(request, 'register.html')

def property_listing(request):
    properties = Property.objects.all()
    return render(request, 'property_listing.html', {'properties': properties})

def property_details(request, property_id):
    property = Property.objects.get(id=property_id)
    return render(request, 'property_details.html', {'property': property})
