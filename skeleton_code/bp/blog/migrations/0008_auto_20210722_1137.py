# Generated by Django 3.2.4 on 2021-07-22 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blog_bodytwo'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='bodyFour',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='bodyThree',
            field=models.TextField(blank=True, null=True),
        ),
    ]
