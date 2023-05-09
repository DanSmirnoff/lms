# Generated by Django 2.2.16 on 2023-05-09 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_created_model_mark_created_many_to_may_with_student_and_task_through_mark'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='group',
        ),
        migrations.CreateModel(
            name='StudentGroupStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Student')),
                ('student_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.StudentGroup')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ManyToManyField(related_name='students', through='tasks.StudentGroupStudent', to='tasks.StudentGroup'),
        ),
    ]