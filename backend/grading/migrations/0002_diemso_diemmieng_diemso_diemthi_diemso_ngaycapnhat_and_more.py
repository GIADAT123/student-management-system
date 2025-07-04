# Generated by Django 5.0.14 on 2025-07-02 18:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grading', '0001_initial'),
        ('students', '0001_initial'),
        ('subjects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='diemso',
            name='DiemMieng',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='diemso',
            name='DiemThi',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='diemso',
            name='NgayCapNhat',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='diemso',
            name='NguoiCapNhat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='diemso',
            unique_together={('IDHocSinh', 'IDMonHoc', 'IDHocKy')},
        ),
        migrations.CreateModel(
            name='DiemSoLichSu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ThoiGian', models.DateTimeField(auto_now_add=True)),
                ('NoiDungThayDoi', models.TextField()),
                ('DiemGoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grading.diemso')),
                ('NguoiThayDoi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'DIEMSO_LICHSU',
            },
        ),
    ]
