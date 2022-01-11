import os


if __name__ == '__main__':
    print('''from rest_framework import serializers

from crud import models''')

    flag = True
    flag_created = False
    flag_updated = False
    cls_name = ''
    with open(os.path.join('crud', 'models.py'), 'r') as f:
        for line in f.readlines():
            if line.startswith('class '):
                cls_name = line.split('class ')[1].split('(')[0]
                print()
                print()
                print(f'class {cls_name}Serializer(serializers.ModelSerializer):')
                print()
                print('    class Meta:')
                print(f'        model = models.{cls_name}')
                print("        fields = '__all__'")
                flag = True
            if flag:
                if 'created_at = ' in line:
                    flag_created = True
                    continue
                if 'updated_at = ' in line:
                    flag_updated = True
                    continue
                if not line.strip():
                    if flag_created and not flag_updated:
                        print("        read_only_fields = ('created_at')")
                    if flag_updated and not flag_created:
                        print("        read_only_fields = ('updated_at')")
                    if flag_created and flag_updated:
                        print("        read_only_fields = ('created_at', 'updated_at')")
                    flag_created = False
                    flag_updated = False
                    flag = False
                    continue



            if not line.startswith('class '):
                continue
            cls_name = line.split('class ')[1].split('(')[0]
            print()
            print()
            print(f'class {cls_name}Serializer(serializers.ModelSerializer):')
            print()
            print('    class Meta:')
            print(f'        model = models.{cls_name}')
            print("        fields = '__all__'")
