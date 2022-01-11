sleep 30
until psql -h db -U root -d tmp -c "\l"
do
  sleep 1
done
python codegen/conf_url_initializer.py > conf/urls.py
echo "" > crud/models.py
echo "" > crud/admin.py
echo "" > crud/filters.py
echo "" > crud/serializers.py
echo "" > crud/views.py
echo "" > crud/urls.py
python manage.py inspectdb > crud/models.py
python codegen/model_converter.py > crud/_models.py
mv crud/_models.py crud/models.py
python codegen/admin_generator.py > crud/admin.py
python codegen/filter_generator.py > crud/filters.py
python codegen/serializer_generator.py > crud/serializers.py
python codegen/view_generator.py > crud/views.py
python codegen/crud_url_generator.py > crud/urls.py
python codegen/conf_url_generator.py > conf/urls.py
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000