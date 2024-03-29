# Generated by Django 3.1.2 on 2020-10-30 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Confession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('nickname', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('realname', models.CharField(max_length=10)),
                ('sex', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1)),
                ('creation_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(auto_now=True)),
                ('confession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.confession')),
            ],
        ),
        migrations.AddField(
            model_name='confession',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_id', to='index.person'),
        ),
        migrations.AddField(
            model_name='confession',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_id', to='index.person'),
        ),
    ]
