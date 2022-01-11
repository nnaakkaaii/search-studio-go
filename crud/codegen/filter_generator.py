import os


d = {
    'AutoField': 'NUMBER_FILTER_LIST',
    'BigAutoField': 'NUMBER_FILTER_LIST',
    'IntegerField': 'NUMBER_FILTER_LIST',
    'FloatField': 'NUMBER_FILTER_LIST',
    'CharField': 'CHAR_FILTER_LIST',
    'TextField': 'CHAR_FILTER_LIST',
    'DateTimeField': 'DATETIME_FILTER_LIST',
    'DateField': 'DATE_FILTER_LIST',
    'TimeField': 'TIME_FILTER_LIST',
    'ForeignKey': 'NUMBER_FILTER_LIST',
    'BooleanField': 'BOOLEAN_FILTER_LIST'
}


if __name__ == '__main__':
    print('''from django_filters import rest_framework as filters

from crud import models

# modelのfieldがCharField,TextFieldの場合
CHAR_FILTER_LIST = [
    'exact',
    'in',
    'contains',
    'startswith',
    'endswith',
    'regex',
    'in',
    'isnull',
]

# modelのfieldがIntegerField, FloatField, DecimalFieldの場合
NUMBER_FILTER_LIST = [
    'exact',
    'in',
    'gt',
    'lt',
    'gte',
    'lte',
    'isnull',
]

# modelのfieldがDataTimeFieldの場合
DATETIME_FILTER_LIST = [
    'exact',
    'in',
    'date',
    'year',
    'month',
    'day',
    'week_day',
    'hour',
    'minute',
    'second',
    'gt',
    'lt',
    'gte',
    'lte',
    'isnull',
]

# modelのfieldがDateFieldの場合
DATE_FILTER_LIST = [
    'exact',
    'in',
    'year',
    'month',
    'day',
    'week_day',
    'gt',
    'lt',
    'gte',
    'lte',
    'isnull',
]

# modelのfieldがTimeFieldの場合
TIME_FILTER_LIST = [
    'exact',
    'in',
    'hour',
    'minute',
    'second',
    'gt',
    'lt',
    'gte',
    'lte',
    'isnull',
]

# modelのfieldがBooleanFieldの場合
BOOLEAN_FILTER_LIST = [
    'isnull',
]''')

    flag = False
    with open(os.path.join('crud', 'models.py'), 'r') as f:
        for line in f.readlines():
            if line.startswith('class '):
                cls_name = line.split('class ')[1].split('(')[0]
                print()
                print()
                print(f'class {cls_name}Filter(filters.FilterSet):')
                print(f'    class Meta:')
                print(f'        model = models.{cls_name}')
                print('        fields = {')
                flag = True
                continue
            if flag and not line.strip():
                print('        }')
                flag = False
                continue
            if flag:
                field = line.strip().split(' = ')[0]
                type_ = line.strip().split('models.')[1].split('(')[0]
                print(f"            '{field}': {d[type_]},")
