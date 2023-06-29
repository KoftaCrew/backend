# Generated by Django 4.2.2 on 2023-06-29 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('model_answer', '0002_initial'),
        ('student_answer', '0001_initial'),
        ('grade', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answergrade',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_answer.answer'),
        ),
        migrations.AddField(
            model_name='answerconfidence',
            name='answer_grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grade.answergrade'),
        ),
        migrations.AddField(
            model_name='answerconfidence',
            name='key_phrase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model_answer.keyphrase'),
        ),
        migrations.AddConstraint(
            model_name='answerconfidence',
            constraint=models.UniqueConstraint(fields=('answer_grade', 'key_phrase'), name='unique_answer_grade_and_key_phrase_together'),
        ),
    ]
