import os
import re


if __name__ == '__main__':
    print('''from rest_framework import routers
from crud import views
''')

    print('router = routers.DefaultRouter()')
    with open(os.path.join('crud', 'models.py'), 'r') as f:
        for line in f.readlines():
            if not line.startswith('class '):
                continue
            cls_name = line.split('class ')[1].split('(')[0]
            cls_name_camel = re.sub("([A-Z])", lambda x: "_" + x.group(1).lower(), cls_name).lstrip('_')
            print(f"router.register(r'{cls_name_camel}', views.{cls_name}ViewSet)")
