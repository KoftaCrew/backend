# Generated by Django 4.2.2 on 2023-07-01 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_answer', '0007_alter_answer_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
    ]
