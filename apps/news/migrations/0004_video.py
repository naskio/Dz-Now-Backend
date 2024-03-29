# Generated by Django 2.2.2 on 2019-09-17 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20190614_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('is_enabled', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=255)),
                ('cover_url', models.URLField(blank=True, null=True)),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='videos', to='news.Article')),
            ],
        ),
    ]
