# Generated by Django 4.1.6 on 2023-03-05 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bolao', '0002_alter_lutador_apelido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='luta',
            name='card',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bolao.card', verbose_name='Card'),
        ),
        migrations.AlterField(
            model_name='luta',
            name='lutadorA',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lutador', to='bolao.lutador', verbose_name='Lutador 1'),
        ),
        migrations.AlterField(
            model_name='luta',
            name='lutadorB',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='oponente', to='bolao.lutador', verbose_name='Lutador 2'),
        ),
    ]