# Generated by Django 3.1.2 on 2020-11-06 07:40

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('flow_rate', models.FloatField()),
                ('loss_rate', models.FloatField()),
                ('state', models.BooleanField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=64)),
                ('user_pwd', models.CharField(max_length=64)),
                ('user_type', models.IntegerField(choices=[(1, 'user'), (2, 'admin')], default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_name', models.CharField(max_length=64)),
                ('r_state', models.BooleanField(default=False)),
                ('r_addtime', models.DateTimeField(auto_now_add=True)),
                ('r_isdel', models.BooleanField(default=False)),
                ('r_description', models.TextField()),
                ('r_starttime', models.DateTimeField()),
                ('r_type', models.IntegerField(choices=[(0, 'default'), (1, 'ip'), (2, 'protocal'), (3, 'feature')], default=0)),
                ('src_ip', models.CharField(max_length=64)),
                ('dst_ip', models.CharField(max_length=64)),
                ('min_src_port', models.CharField(max_length=64)),
                ('max_src_port', models.CharField(max_length=64)),
                ('min_dst_port', models.CharField(max_length=64)),
                ('max_dst_port', models.CharField(max_length=64)),
                ('package_type', models.IntegerField()),
                ('feature', models.CharField(max_length=64)),
                ('r_ofadapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.adapter')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.users')),
            ],
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cap_date', models.DateTimeField(auto_now_add=True)),
                ('path', models.FilePathField(path=api.models.pack_path)),
                ('src_ip', models.CharField(max_length=64)),
                ('dst_ip', models.CharField(max_length=64)),
                ('src_port', models.IntegerField()),
                ('dst_port', models.IntegerField()),
                ('package_type', models.IntegerField()),
                ('feature', models.CharField(max_length=64)),
                ('session_id', models.IntegerField()),
                ('adapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.adapter')),
                ('r_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.rule')),
            ],
        ),
    ]