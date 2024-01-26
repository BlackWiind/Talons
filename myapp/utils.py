import re

from openpyxl import load_workbook

from .models import Services


def update_db_from_excel(file):
    wb = load_workbook(file)
    ws = wb.active
    Services.objects.all().delete()
    new_list = []
    for tup in Services.department_choices:
        new_list.append(tup[0])

    for row in ws.iter_rows(min_row=2, values_only=True):
        try:
            id = reg_exp(row[1])
            if 14 < int(id) < 16:
                department_id = '14'
            elif 21 < int(id) < 23:
                department_id = '21'
            elif int(id) == 31:
                for department in new_list:
                    Services.objects.create(name=row[2], price=round(row[4], 2), type=row[3], department=department)
            else:
                department_id = id
            if row[4] != '':
                Services.objects.create(name=row[2], price=round(row[4], 2), type=row[3], department=department_id)
        except:
            pass


def reg_exp(string: str) -> str:
    regex = r'\d+'
    return re.search(regex, string)[0]
