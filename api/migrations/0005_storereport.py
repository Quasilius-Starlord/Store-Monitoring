# Generated by Django 4.2.3 on 2023-07-27 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_storestatuslog_store_alter_storetiming_store'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Completed')])),
                ('report_url', models.FileField(blank=True, null=True, upload_to='reports')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='api.store')),
            ],
        ),
    ]
