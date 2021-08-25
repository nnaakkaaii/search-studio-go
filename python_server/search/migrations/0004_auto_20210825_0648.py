# Generated by Django 3.2.6 on 2021-08-25 06:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_alter_prefecture_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='id',
            field=models.CharField(help_text='決済方法ID (Q01)。必須。', max_length=3, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='決済方法ID'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.CharField(help_text='予約方法ID (R01)。必須。', max_length=3, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='予約方法ID'),
        ),
    ]
