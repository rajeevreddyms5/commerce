# Generated by Django 4.2.3 on 2023-07-19 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_alter_listings_time_alter_listings_wathlist_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='category',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='listings',
            name='description',
            field=models.TextField(),
        ),
    ]
