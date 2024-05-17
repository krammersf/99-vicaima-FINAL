# Generated by Django 5.0.6 on 2024-05-15 22:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_event_evaluated_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.collaborator')),
                ('evaluator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='home.collaborator')),
            ],
        ),
        migrations.DeleteModel(
            name='Avaliação',
        ),
    ]
