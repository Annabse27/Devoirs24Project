# Generated by Django 5.1.1 on 2024-09-23 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_payment_stripe_payment_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='stripe_payment_url',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
