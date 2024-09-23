from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    # cars=Car.objects.filter(factory_year=1)
    # cars=Car.objects.filter(brand__name='bmw')
    # cars=Car.objects.filter(brand__contains='bm')
    
    # print(request)
    # print(request.GET.get('search'))
    search=request.GET.get('search')
    # print(search)
    
    if search:
        cars=Car.objects.filter(model=search)
    else:
        cars=Car.objects.all()
    
    return render(
        request,
        'cars.html', 
        {'cars': cars }
    )
