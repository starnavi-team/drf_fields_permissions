# Generated by Django 2.0.4 on 2018-04-25 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='priority',
            field=models.IntegerField(choices=[(1, 'Low'), (2, 'Average'), (3, 'High')], default=1),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.IntegerField(choices=[(1, 'New'), (2, 'In Progress'), (3, 'Done')], default=1),
        ),
    ]
