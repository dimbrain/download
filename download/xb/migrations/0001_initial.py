# Generated by Django 2.0 on 2017-12-28 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thread_id', models.IntegerField()),
                ('start_page', models.IntegerField()),
                ('end_page', models.IntegerField()),
                ('in_progress', models.BooleanField()),
                ('is_error', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xb.Thread'),
        ),
    ]
