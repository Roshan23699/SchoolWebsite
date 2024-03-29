# Generated by Django 3.0.5 on 2020-07-02 07:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard', models.IntegerField(choices=[(5, '5th'), (6, '6th'), (7, '7th'), (8, '8th'), (9, '9th'), (10, '10th')], default=5)),
                ('divison', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], default='A', max_length=1)),
                ('subject', models.CharField(default='Mathematics', max_length=20)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('submission_date', models.DateField()),
                ('heading', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marqueeHeading', models.CharField(default='', max_length=50)),
                ('heading', models.CharField(max_length=100)),
                ('pdf', models.FileField(default='', upload_to='pdf')),
                ('datePublished', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tenth_Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(2021, '2020-21'), (2022, '2021-22'), (2023, '2022-23'), (2024, '2023-24'), (2025, '2024-25'), (2026, '2025-26'), (2027, '2026-27')], default=2020, unique=True)),
                ('heading', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yearname', models.IntegerField(default=2020)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.School')),
            ],
        ),
        migrations.CreateModel(
            name='Tenth_Topper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('percentage', models.SmallIntegerField(default=100)),
                ('image', models.ImageField(default='', upload_to='media/images')),
                ('tenth_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Tenth_Result')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(default='', max_length=50)),
                ('standard', models.IntegerField(choices=[(5, '5th'), (6, '6th'), (7, '7th'), (8, '8th'), (9, '9th'), (10, '10th')], default=5)),
                ('divison', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], default='A', max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('year', models.ForeignKey(default=2020, on_delete=django.db.models.deletion.CASCADE, to='mainsite.Year')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard', models.IntegerField(choices=[(5, '5th'), (6, '6th'), (7, '7th'), (8, '8th'), (9, '9th'), (10, '10th')], default=5)),
                ('term', models.PositiveSmallIntegerField(choices=[(1, 'First'), (2, 'Second')], default=1)),
                ('exam', models.CharField(choices=[('unit test', 'Unit test'), ('semister', 'Semister')], default='unit test', max_length=20)),
                ('Maximum_marks_for_each_subject', models.IntegerField(default=20)),
                ('Marathi', models.IntegerField(blank=True, default=0)),
                ('Hindi', models.IntegerField(blank=True, default=0)),
                ('English', models.IntegerField(blank=True, default=0)),
                ('Mathematics', models.IntegerField(blank=True, default=0)),
                ('SocialScience', models.IntegerField(blank=True, default=0)),
                ('Science', models.IntegerField(blank=True, default=0)),
                ('Total_obtained_marks', models.IntegerField(blank=True, default=0, editable=False)),
                ('Total_maximum_marks', models.IntegerField(blank=True, default=0, editable=False)),
                ('student', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mainsite.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_admission', models.DateField()),
                ('father_name', models.CharField(max_length=40)),
                ('mother_name', models.CharField(max_length=40)),
                ('father_occupation', models.CharField(max_length=20)),
                ('mother_occupation', models.CharField(default='', max_length=20)),
                ('parent_contact_1', models.IntegerField(default=1234567890)),
                ('parent_contact_2', models.IntegerField(default=1234567890)),
                ('temporary_address', models.CharField(blank=True, max_length=100)),
                ('permenant_address', models.CharField(blank=True, max_length=100)),
                ('student_contact', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(upload_to='media/images')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Student')),
            ],
        ),
    ]
