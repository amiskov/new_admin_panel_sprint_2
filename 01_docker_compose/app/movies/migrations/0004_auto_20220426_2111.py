# Generated by Django 3.2 on 2022-04-26 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_filmwork_film_work_creation_date_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmwork',
            name='persons',
            field=models.ManyToManyField(through='movies.PersonFilmwork', to='movies.Person'),
        ),
        migrations.AlterField(
            model_name='personfilmwork',
            name='role',
            field=models.CharField(choices=[('actor', 'actor'), ('writer', 'writer'), ('director', 'director')], default='actor', max_length=255, null=True, verbose_name='role'),
        ),
    ]
