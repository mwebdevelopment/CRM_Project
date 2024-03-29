# Generated by Django 4.2.4 on 2023-09-09 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0010_alter_lead_priority_alter_lead_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='priority',
            field=models.CharField(choices=[('low', 'low'), ('high', 'high'), ('medium', 'medium')], default='medium', max_length=25),
        ),
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('inprogress', 'inprogress'), ('new', 'new'), ('contacted', 'contacted'), ('lost', 'lost'), ('won', 'won')], default='new', max_length=25),
        ),
    ]
