from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'website/index.html')

def contact_us(request):
    address = 'Bokonbaeva 123'
    tel = '+996 5009009013'
    contactNames = ['Esen Umarov', 'Dolon Bakytov', 'Idris Turunov']

    companyInfo = {
        'inn': 23423423423423,
        'osoo': 'Company United CO',
        'company_age': 20
    }
    context = {
        'address': address,
        'telephone': tel,
        'names': contactNames,
        'c_info': companyInfo,
    }
    return render(request, 'website/contactus.html',context)

def about_us(request):
    return render(request, 'website/aboutus.html')

