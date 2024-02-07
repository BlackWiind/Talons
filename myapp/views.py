from django.db.models import Q
from django.shortcuts import render, redirect

from .models import Services, Department
from .utils import update_db_from_excel


def import_from_excel(request):
    context = {'department': Department.objects.exclude(name='Общие').order_by('name')}
    return render(request, 'index.html', context)


def talon(request):
    if request.method == "GET":
        try:
            services = Services.objects.filter(Q(department=request.GET.get('department')) | Q(department__name='Общие'))
            dep = services[0].department
        except:
            return redirect('error.html')
        context = {'services': services, 'department': dep}
        return render(request, 'talon.html', context)


def error(request):
    return render(request, 'error.html')


def service(request):
    if request.method == 'POST':
        excel_file = request.FILES['excel_file']
        update_db_from_excel(excel_file)
        return redirect('service.html')
    return render(request, 'service.html')
