from django.shortcuts import render, redirect
from openpyxl import load_workbook

from .models import Services
from .utils import update_db_from_excel


def import_from_excel(request):
    context = {'department': Services.department_choices}
    return render(request, 'index.html', context)


def talon(request):
    if request.method == "GET":
        try:
            services = Services.objects.filter(department=request.GET.get('department'))
            dep = services[0].get_department_display()
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
