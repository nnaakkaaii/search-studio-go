import os


if __name__ == '__main__':
    print('''from django.contrib import admin
from crud import models

# Register your models here.''')

    with open(os.path.join('crud', 'models.py'), 'r') as f:
        for line in f.readlines():
            if not line.startswith('class '):
                continue
            cls_name = line.split('class ')[1].split('(')[0]
            print(f'admin.site.register(models.{cls_name})')
