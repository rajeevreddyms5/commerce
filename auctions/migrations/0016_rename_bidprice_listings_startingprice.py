# Generated by Django 4.2.3 on 2023-07-21 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_remove_bids_bidlisting_bids_bidlisting'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listings',
            old_name='bidprice',
            new_name='startingprice',
        ),
    ]
