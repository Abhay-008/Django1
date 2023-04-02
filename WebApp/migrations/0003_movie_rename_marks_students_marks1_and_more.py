# Generated by Django 4.1.4 on 2023-03-19 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0002_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=150)),
                ('release_year', models.IntegerField()),
                ('director', models.CharField(max_length=100)),
                ('movie_poster', models.ImageField(null=True, upload_to='static/images/')),
                ('movie_plot', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='students',
            old_name='marks',
            new_name='marks1',
        ),
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='sal',
            field=models.FloatField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
