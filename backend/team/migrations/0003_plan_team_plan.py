# Generated by Django 4.2.4 on 2023-09-09 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_team_created_at_team_created_by_team_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('max_leads', models.IntegerField(default=5)),
                ('max_clients', models.IntegerField(default=5)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teams', to='team.plan'),
        ),
    ]
