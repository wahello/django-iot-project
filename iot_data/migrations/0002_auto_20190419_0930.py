# Generated by Django 2.2 on 2019-04-19 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("iot_data", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="iotdata",
            name="user",
            field=models.CharField(default="peter", max_length=50),
        )
    ]
