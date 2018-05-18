# Generated by Django 2.0.1 on 2018-05-16 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engagementSurvey', '0007_auto_20180516_0941'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ['employee', 'question']},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['company_name'], 'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['question_type', 'question_text']},
        ),
        migrations.AlterField(
            model_name='company',
            name='cid',
            field=models.CharField(default='e112b254-58e5-11e8-824e-acbc32af581d', editable=False, max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='eid',
            field=models.CharField(default='e1132e46-58e5-11e8-8955-acbc32af581d', editable=False, max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_id',
            field=models.CharField(default='e1105fcc-58e5-11e8-ba9c-acbc32af581d', editable=False, max_length=36, primary_key=True, serialize=False),
        ),
    ]