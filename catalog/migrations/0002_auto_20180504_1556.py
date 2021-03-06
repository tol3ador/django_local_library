# Generated by Django 2.0.5 on 2018-05-04 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='author',
            managers=[
                ('authors', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='book',
            managers=[
                ('books', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='bookinstance',
            managers=[
                ('bookInstance', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='borrower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
