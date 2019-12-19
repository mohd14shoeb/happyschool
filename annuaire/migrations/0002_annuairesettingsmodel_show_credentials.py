# Generated by Django 2.2.8 on 2019-12-19 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annuaire', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='annuairesettingsmodel',
            name='show_credentials',
            field=models.BooleanField(default=True, help_text='Montre les champs utilisateur/mot de passe dans la fiche info\n            et permet également de générer la liste des mots de passe des élèves par classe'),
        ),
    ]
