# Generated by Django 4.2.1 on 2023-06-14 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=30)),
                ('marks', models.IntegerField()),
                ('student', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='course', to='first_app.students')),
            ],
        ),
    ]
