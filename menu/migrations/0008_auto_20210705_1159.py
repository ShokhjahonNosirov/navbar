# Generated by Django 3.2.5 on 2021-07-05 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_thirdcategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thirdcategory',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='thirdcategory',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
