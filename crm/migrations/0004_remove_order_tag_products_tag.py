# Generated by Django 4.1 on 2022-08-27 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_tag_order_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tag',
        ),
        migrations.AddField(
            model_name='products',
            name='tag',
            field=models.ManyToManyField(to='crm.tag'),
        ),
    ]
