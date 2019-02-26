# Generated by Django 2.1.5 on 2019-02-18 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_choice', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ExamQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_question', models.CharField(max_length=3000)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='exam_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.ExamQuestion'),
        ),
    ]