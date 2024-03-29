# Generated by Django 3.1.2 on 2020-11-15 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_update_sex_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='nickname',
            new_name='display_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='realname',
        ),
        migrations.AddField(
            model_name='person',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='creation_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='confession',
            name='creation_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='confession',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_id', to='index.person'),
        ),
        migrations.AlterField(
            model_name='like',
            name='creation_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='creation_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('X', 'Secret')], max_length=1),
        ),
        migrations.AddConstraint(
            model_name='person',
            constraint=models.UniqueConstraint(fields=('display_name', 'sex'), name='unique_person'),
        ),
    ]
