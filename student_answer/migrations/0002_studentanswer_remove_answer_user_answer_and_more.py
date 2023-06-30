# Generated by Django 4.2.2 on 2023-06-30 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
        ('student_answer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student_id', models.CharField(max_length=32, unique=True)),
                ('student_name', models.CharField(max_length=128)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.exam')),
            ],
            options={
                'unique_together': {('exam', 'student_id')},
            },
        ),
        migrations.RemoveField(
            model_name='answer',
            name='user_answer',
        ),
        migrations.DeleteModel(
            name='UserAnswer',
        ),
        migrations.AddField(
            model_name='answer',
            name='student_answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student_answer.studentanswer'),
        ),
    ]
