# Generated by Django 3.2.12 on 2022-06-23 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0002_livros_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='autor',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
