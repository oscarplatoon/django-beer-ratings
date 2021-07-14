# Generated by Django 3.2.5 on 2021-07-14 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beer_reviews_app', '0002_auto_20210714_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('beer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='beer_reviews_app.beer')),
            ],
        ),
    ]
