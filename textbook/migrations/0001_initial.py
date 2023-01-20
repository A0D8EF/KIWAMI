# Generated by Django 4.1.2 on 2022-12-30 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MajorCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='大カテゴリ名')),
                ('order', models.IntegerField(unique=True, verbose_name='順番')),
            ],
        ),
        migrations.CreateModel(
            name='MinorCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='小カテゴリ名')),
                ('order', models.IntegerField(verbose_name='順番')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='textbook.majorcategory', verbose_name='大カテゴリ')),
            ],
        ),
        migrations.CreateModel(
            name='Textbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日時')),
                ('title', models.CharField(max_length=100, verbose_name='タイトル')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='textbook/thubnail/', verbose_name='サムネイル画像')),
                ('thumbnail_url', models.URLField(blank=True, null=True, verbose_name='Youtubeのサムネイル')),
                ('file_content', models.FileField(blank=True, null=True, upload_to='textbook/movie/', verbose_name='ファイル')),
                ('is_youtube', models.BooleanField(default=False, verbose_name='Youtubeか')),
                ('youtube_url', models.URLField(blank=True, null=True, verbose_name='YoutubeURL')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='表示の順番')),
                ('is_top', models.BooleanField(default=False, verbose_name='トップ表示')),
                ('top_order', models.IntegerField(blank=True, null=True, verbose_name='トップ表示の順番')),
                ('explanation', models.CharField(blank=True, max_length=5000, null=True, verbose_name='説明文')),
                ('major_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='textbook.majorcategory', verbose_name='大カテゴリ')),
                ('minor_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='textbook.minorcategory', verbose_name='小カテゴリ')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='投稿者')),
            ],
        ),
    ]