# Generated by Django 3.2.12 on 2022-06-28 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('livro', '0010_auto_20220628_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario'),
            preserve_default=False,
        ),
    ]
