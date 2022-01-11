import os


if __name__ == '__main__':
    print('''from rest_framework import viewsets

from crud import filters
from crud import models
from crud import serializers''')

    with open(os.path.join('crud', 'models.py'), 'r') as f:
        for line in f.readlines():
            if not line.startswith('class '):
                continue
            cls_name = line.split('class ')[1].split('(')[0]
            print()
            print()
            print(f'class {cls_name}ViewSet(viewsets.ModelViewSet):')
            print(f'    queryset = models.{cls_name}.objects.all()')
            print(f'    serializer_class = serializers.{cls_name}Serializer')
            print(f'    filter_class = filters.{cls_name}Filter')
