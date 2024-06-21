# Generated by Django 2.0.5 on 2019-03-15 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_useraccount_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserComplaint_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('accountnumber', models.IntegerField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('mobilenumber', models.IntegerField()),
                ('complaint', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('cuname', models.ForeignKey(on_delete='cascade', to='User.UserRegister_Model')),
            ],
        ),
        migrations.AlterField(
            model_name='useraccount_model',
            name='uuname',
            field=models.ForeignKey(on_delete='cascade', to='User.UserRegister_Model'),
        ),
    ]
