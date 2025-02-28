# Generated by Django 4.2.11 on 2024-06-25 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("facebook", "0003_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.CharField(blank=True, max_length=200)),
                ("mobile", models.BigIntegerField(default=0)),
                ("price", models.IntegerField()),
                ("quantity", models.IntegerField()),
                ("status", models.BooleanField(default=False)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="facebook.registration",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="facebook.product",
                    ),
                ),
            ],
        ),
    ]
