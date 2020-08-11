# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-10 14:20
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("mp", "0011_payment_approved_null"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="app_id",
            field=models.CharField(
                help_text="The APP_ID given by MercadoPago.",
                max_length=16,
                verbose_name="client id",
            ),
        ),
        migrations.AlterField(
            model_name="account",
            name="name",
            field=models.CharField(
                help_text="A friendly name to recognize this account.",
                max_length=32,
                verbose_name="name",
            ),
        ),
        migrations.AlterField(
            model_name="account",
            name="sandbox",
            field=models.BooleanField(
                default=True,
                help_text=(
                    "Indicates if this account uses the sandbox mode, indicated for"
                    " testing rather than real transactions."
                ),
                verbose_name="sandbox",
            ),
        ),
        migrations.AlterField(
            model_name="account",
            name="secret_key",
            field=models.CharField(
                help_text="The SECRET_KEY given by MercadoPago.",
                max_length=32,
                verbose_name="client id",
            ),
        ),
        migrations.AlterField(
            model_name="account",
            name="slug",
            field=models.SlugField(
                help_text="This slug is used for this account's notification URL.",
                unique=True,
                verbose_name="slug",
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="last_update",
            field=models.DateTimeField(auto_now=True, verbose_name="last_update"),
        ),
        migrations.AlterField(
            model_name="notification",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="notifications",
                to="mp.Account",
                verbose_name="owner",
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="resource_id",
            field=models.CharField(max_length=46, verbose_name="resource_id"),
        ),
        migrations.AlterField(
            model_name="notification",
            name="status",
            field=models.CharField(
                choices=[
                    ("unp", "Unprocessed"),
                    ("pro", "Processed"),
                    ("old", "With updates"),
                    ("ign", "Ignored"),
                    ("ok", "Okay"),
                    ("404", "Error 404"),
                    ("err", "Error"),
                ],
                default="unp",
                max_length=3,
                verbose_name="status",
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="approved",
            field=models.DateTimeField(null=True, verbose_name="approved"),
        ),
        migrations.AlterField(
            model_name="payment",
            name="created",
            field=models.DateTimeField(verbose_name="created"),
        ),
        migrations.AlterField(
            model_name="payment",
            name="notification",
            field=models.OneToOneField(
                blank=True,
                help_text="The notification that informed us of this payment.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="payment",
                to="mp.Notification",
                verbose_name="notification",
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="preference",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="payments",
                to="mp.Preference",
                verbose_name="preference",
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="status",
            field=models.CharField(max_length=16, verbose_name="status"),
        ),
        migrations.AlterField(
            model_name="payment",
            name="status_detail",
            field=models.CharField(max_length=32, verbose_name="status detail"),
        ),
        migrations.AlterField(
            model_name="preference",
            name="mp_id",
            field=models.CharField(
                help_text="The id MercadoPago has assigned for this Preference",
                max_length=46,
                verbose_name="mercadopago id",
            ),
        ),
        migrations.AlterField(
            model_name="preference",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="preferences",
                to="mp.Account",
                verbose_name="owner",
            ),
        ),
        migrations.AlterField(
            model_name="preference",
            name="paid",
            field=models.BooleanField(
                default=False,
                help_text="Indicates if the preference has been paid.",
                verbose_name="paid",
            ),
        ),
        migrations.AlterField(
            model_name="preference",
            name="payment_url",
            field=models.URLField(verbose_name="payment url"),
        ),
        migrations.AlterField(
            model_name="preference",
            name="price",
            field=models.DecimalField(
                decimal_places=2, max_digits=15, verbose_name="price"
            ),
        ),
        migrations.AlterField(
            model_name="preference",
            name="reference",
            field=models.CharField(
                max_length=128, unique=True, verbose_name="reference"
            ),
        ),
        migrations.AlterField(
            model_name="preference",
            name="sandbox_url",
            field=models.URLField(verbose_name="sandbox url"),
        ),
        migrations.AlterField(
            model_name="preference",
            name="title",
            field=models.CharField(max_length=256, verbose_name="title"),
        ),
    ]
