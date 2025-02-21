# Generated by Django 4.2.2 on 2023-07-02 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_answer', '0008_alter_answer_text'),
        ('model_answer', '0004_remove_keyphrase_end_index_gt_start_index_and_more'),
        ('grade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerSegment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_index', models.IntegerField()),
                ('end_index', models.IntegerField()),
                ('grade', models.FloatField()),
                ('confidence', models.FloatField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_answer.answer')),
                ('key_phrase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model_answer.keyphrase')),
            ],
        ),
        migrations.RemoveField(
            model_name='answergrade',
            name='answer',
        ),
        migrations.DeleteModel(
            name='AnswerConfidence',
        ),
        migrations.DeleteModel(
            name='AnswerGrade',
        ),
        migrations.AddConstraint(
            model_name='answersegment',
            constraint=models.CheckConstraint(check=models.Q(('end_index__gt', models.F('start_index'))), name='student_answer_end_index_gt_start_index'),
        ),
    ]
