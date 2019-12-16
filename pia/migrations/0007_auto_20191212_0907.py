# Generated by Django 2.2.8 on 2019-12-12 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pia', '0006_auto_20191209_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='goalmodel',
            name='indicator_action',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AddField(
            model_name='subgoalmodel',
            name='indicator_action',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='goalmodel',
            name='given_help',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='goalmodel',
            name='self_assessment',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='subgoalmodel',
            name='given_help',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='subgoalmodel',
            name='parent_commitment',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='subgoalmodel',
            name='self_assessment',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]