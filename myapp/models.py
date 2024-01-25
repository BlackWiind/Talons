from django.db import models


class Services(models.Model):
    department_choices = (
        ('11', 'ЭНДОСКОПИЧЕСКИЕ  ИССЛЕДОВАНИЯ - СТАЦИОНАР'),
        ('12', 'ОФУД'),
        ('14', 'ОЛД'),
        ('16', "КТТ"),
        ('17', 'ЛКИ'),
        ('21', 'ФТО'),
        ('32', 'Колопроктологическое отделение'),
        ('33', 'ОРХМДЛ '),
        ('34', 'Челюстно-лицевая хирургия'),
        ('35', 'Торакальная хирургия'),
        ('36', 'Урология'),
        ('37', 'Травматология'),
        ('38', 'Хирургия общая'),
        ('39', 'Сосудистая хирургия'),
        ('40', 'Гинекология'),
        ('41', 'Отделение нарушений ритма сердца'),
        ('42', 'ЛОР отделение'),
        ('43', 'Гастроэнтерология'),
        ('44', 'Кардиология'),
        ('45', 'Эндокринология'),
        ('46', 'Неврология'),
        ('47', 'Пульмонология'),
        ('48', 'Ревматология'),
        ('49', 'Гематология'),
        ('50', 'ОХГД нефрология'),
        ('51', 'РАО'),
    )

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    department = models.CharField(choices=department_choices, max_length=2)