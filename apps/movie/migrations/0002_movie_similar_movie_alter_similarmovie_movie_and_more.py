# Generated by Django 4.2 on 2023-05-17 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='similar_movie',
            field=models.ManyToManyField(through='movie.SimilarMovie', to='movie.movie'),
        ),
        migrations.AlterField(
            model_name='similarmovie',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='similar_movies', to='movie.movie'),
        ),
        migrations.AlterField(
            model_name='similarmovie',
            name='similar_movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie'),
        ),
    ]