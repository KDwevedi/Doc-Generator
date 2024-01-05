# Generated by Django 3.2.12 on 2022-09-26 09:06

from django.db import migrations, models
import fernet_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0004_alter_genericconfig_uploader_ref'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('google_token', fernet_fields.fields.EncryptedTextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]