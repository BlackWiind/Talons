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
            # print(id)
            # if id[-1] == '.':
            #     id = float(id[:-1])
            # else:
            #     id = float(id)
            # department_id = None
            if 14 < int(id) < 16:
                department_id = '14'
            elif 21 < int(id) < 23:
                department_id = '21'
            elif int(id) == 31:
                for department in new_list:
                    Services.objects.create(name=row[2], price=round(row[4], 2), type=row[3], department=department)
            else:
                department_id = id
            # if 11 < id < 12:
            #     department_id = '1'
            # elif 12 < id < 13:
            #     department_id = '2'
            # elif 14 < id < 16:
            #     department_id = '3'
            # elif 16 < id < 17:
            #     department_id = '4'
            # elif 17 < id < 18:
            #     department_id = '5'
            # elif 21 < id < 23:
            #     department_id = '6'
            # elif 32 < id < 33:
            #     department_id = '7'
            # elif 33 < id < 34:
            #     department_id = '8'
            # elif 34 < id < 35:
            #     department_id = '9'
            # elif 35 < id < 36:
            #     department_id = '10'
            # elif 36 < id < 37:
            #     department_id = '11'
            # elif 37 < id < 38:
            #     department_id = '12'
            # elif 38 < id < 39:
            #     department_id = '13'
            # elif 39 < id < 40:
            #     department_id = '14'
            # elif 40 < id < 41:
            #     department_id = '15'
            # elif 41 < id < 42:
            #     department_id = '16'
            # elif 42 < id < 43:
            #     department_id = '17'
            # elif 43 < id < 44:
            #     department_id = '18'
            # elif 44 < id < 45:
            #     department_id = '19'
            # elif 45 < id < 46:
            #     department_id = '20'
            # elif 46 < id < 47:
            #     department_id = '21'
            # elif 47 < id < 48:
            #     department_id = '22'
            # elif 48 < id < 49:
            #     department_id = '23'
            # elif 49 < id < 50:
            #     department_id = '24'
            # elif 50 < id < 51:
            #     department_id = '25'
            # elif 51 < id < 52:
            #     department_id = '26'
            if row[4] != '':
                Services.objects.create(name=row[2], price=round(row[4], 2), type=row[3], department=department_id)
        except:
            pass


def reg_exp(string: str) -> str:
    # regex = r'\d+\.\d+'
    regex = r'\d+'
    return re.search(regex, string)[0]
