# Generated by Django 2.0.7 on 2018-07-30 19:25

from django.db import migrations, models


def rename_group(apps, schema_editor, old_name, new_name):
    Group = apps.get_model('auth', 'group')
    db_alias = schema_editor.connection.alias
    Group.objects.using(db_alias).filter(name=old_name).update(name=new_name)


def rename_group_forward(apps, schema_editor):
    rename_group(apps, schema_editor, 'Staff', 'Manager')


def rename_group_reverse(apps, schema_editor):
    rename_group(apps, schema_editor, 'Manager', 'Staff')


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0078_populate_voter_and_participant_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionnaire',
            old_name='staff_only',
            new_name='manager_only'
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='manager_only',
            field=models.BooleanField(default=False, verbose_name='display for managers only')
        ),
        migrations.RunPython(rename_group_forward, reverse_code=rename_group_reverse)
    ]
