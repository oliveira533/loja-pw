# Generated by Django 4.1.3 on 2022-11-02 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lojaApp', '0004_alter_produtos_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='desc',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='tamanhos',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
