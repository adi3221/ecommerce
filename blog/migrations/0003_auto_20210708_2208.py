# Generated by Django 3.2.4 on 2021-07-08 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_blog_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='chead0',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='chead1',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='chead2',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='head1',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='head2',
            field=models.CharField(default='', max_length=500),
        ),
    ]