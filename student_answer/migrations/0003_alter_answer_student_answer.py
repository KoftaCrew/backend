# Generated by Django 4.2.2 on 2023-06-30 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_answer', '0002_studentanswer_remove_answer_user_answer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='student_answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_answer', to='student_answer.studentanswer'),
        ),
    ]
