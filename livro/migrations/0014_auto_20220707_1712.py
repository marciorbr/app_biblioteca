# Generated by Django 3.2.12 on 2022-07-07 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('livro', '0013_auto_20220707_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimos',
            name='nome_emprestado_anonimo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='nome_emprestado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario'),
            preserve_default=False,
        ),
    ]