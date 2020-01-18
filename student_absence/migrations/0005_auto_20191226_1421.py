# Generated by Django 2.2.8 on 2019-12-26 13:21

import datetime

from django.db import migrations

from student_absence.models import StudentAbsenceModel, PeriodModel


def two_period_to_any(apps, schema_editor):
    if not StudentAbsenceModel.objects.exists():
        return

    am = PeriodModel.objects.create(
        name="Matin", start=datetime.time(8, 30), end=datetime.time(12, 30)
    )
    pm = PeriodModel.objects.create(
        name="Après-midi", start=datetime.time(12, 30), end=datetime.time(16, 30)
    )

    for absence in StudentAbsenceModel.objects.all():
        creation = absence.datetime_creation
        last_update = absence.datetime_update
        absence.period = am
        absence.is_absent = absence.morning
        absence.save()
        StudentAbsenceModel.objects.filter(pk=absence.pk).update(
            datetime_creation=creation,
            datetime_update=last_update,
        )

        absence.pk = None
        absence.period = pm
        absence.is_absent = absence.afternoon
        absence.save()
        StudentAbsenceModel.objects.filter(pk=absence.pk).update(
            datetime_creation=creation,
            datetime_update=last_update,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('student_absence', '0004_auto_20191224_1145'),
    ]

    operations = [
        migrations.RunPython(two_period_to_any),
    ]