# Generated by Django 4.1 on 2022-09-04 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnic193187', '0002_rename_title_question_question_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='corectanswer',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
