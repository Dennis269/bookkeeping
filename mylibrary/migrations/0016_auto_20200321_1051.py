# Generated by Django 3.0.4 on 2020-03-21 10:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mylibrary', '0015_auto_20200321_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='borrow_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 21, 10, 51, 35, 573981), verbose_name='借出时间'),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='return_ddl',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 21, 10, 51, 35, 574022), verbose_name='归还期限'),
        ),
        migrations.AlterField(
            model_name='log',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mylibrary.User', verbose_name='用户'),
        ),
    ]
