# Generated by Django 3.2.12 on 2022-07-08 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0015_alter_emprestimos_nome_emprestado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='data_devolucao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='tempo_duracao',
            field=models.DateField(blank=True, null=True),
        ),
    ]