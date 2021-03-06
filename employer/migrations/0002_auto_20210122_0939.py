# Generated by Django 3.1.4 on 2021-01-22 09:39

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('student', '0001_initial'),
        ('employer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentplacementassignment',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
        migrations.AddField(
            model_name='studentplacementassignment',
            name='supervisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.staff'),
        ),
        migrations.AddField(
            model_name='studentplacement',
            name='employer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.employer'),
        ),
        migrations.AddField(
            model_name='studentplacement',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
        migrations.AddField(
            model_name='studentinterview',
            name='employer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.employer'),
        ),
        migrations.AddField(
            model_name='studentinterview',
            name='job_post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.jobpost'),
        ),
        migrations.AddField(
            model_name='studentinterview',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
        migrations.AddField(
            model_name='staff',
            name='employer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.employer'),
        ),
        migrations.AddField(
            model_name='jobpostactivity',
            name='job_post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.jobpost'),
        ),
        migrations.AddField(
            model_name='jobpostactivity',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='employer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.employer'),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='job_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.jobtype'),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='skills',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
