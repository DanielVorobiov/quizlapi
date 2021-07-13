# Generated by Django 2.2.12 on 2021-07-09 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answerTitle', models.CharField(max_length=15)),
                ('correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameTitle', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionTitle', models.CharField(default='Title', max_length=100)),
                ('numberOfAnswers', models.IntegerField(choices=[(2, 2), (4, 4)], default=4)),
                ('points', models.IntegerField(choices=[(5, 5), (10, 10), (15, 15)], default=5)),
            ],
        ),
    ]
