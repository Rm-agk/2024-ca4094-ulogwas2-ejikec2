# Generated by Django 4.2.5 on 2023-10-24 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("GradNav", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Basket",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField()),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
                ),
                ("product_image", models.FileField(upload_to="products")),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("date_ordered", models.DateTimeField(auto_now_add=True)),
                (
                    "total_price",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
                ),
                (
                    "basket_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="GradNav.basket"
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BasketItem",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("quantity", models.IntegerField(default=1)),
                (
                    "basket_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="GradNav.basket"
                    ),
                ),
                (
                    "product_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="GradNav.product",
                    ),
                ),
            ],
        ),
    ]
