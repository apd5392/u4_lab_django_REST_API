# Generated by Django 4.1 on 2022-08-31 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0002_alter_team_losses_alter_team_wins'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=200)),
                ('age', models.SmallIntegerField()),
                ('injured', models.CharField(default='yes/no', max_length=3)),
                ('points', models.SmallIntegerField()),
                ('rebounds', models.SmallIntegerField()),
                ('assists', models.SmallIntegerField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team', to='basketball.team')),
            ],
        ),
    ]
