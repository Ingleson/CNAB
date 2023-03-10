# Generated by Django 4.1.5 on 2023-01-29 14:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("stores", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
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
                (
                    "typetransaction",
                    models.IntegerField(
                        choices=[
                            ("None", "Default"),
                            ("1", "Debito"),
                            ("2", "Boleto"),
                            ("3", "Financiamento"),
                            ("4", "Credito"),
                            ("5", "Emprestimo"),
                            ("6", "Vendas"),
                            ("7", "Ted"),
                            ("8", "Doc"),
                            ("9", "Aluguel"),
                        ],
                        default="None",
                    ),
                ),
                ("date", models.DateField(auto_now_add=True)),
                ("value", models.FloatField()),
                ("cpf", models.CharField(max_length=11)),
                ("card", models.CharField(max_length=12)),
                (
                    "hour",
                    models.TimeField(
                        default=datetime.datetime(
                            2023,
                            1,
                            29,
                            14,
                            57,
                            33,
                            280432,
                            tzinfo=datetime.timezone.utc,
                        )
                    ),
                ),
                (
                    "store",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transactions",
                        to="stores.store",
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
            },
        ),
    ]
