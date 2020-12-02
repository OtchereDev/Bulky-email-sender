# Generated by Django 3.1.2 on 2020-12-02 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailContacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='email address')),
            ],
        ),
        migrations.CreateModel(
            name='Emailer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sent', models.DateTimeField(auto_now_add=True, verbose_name='email date')),
                ('email_subject', models.CharField(max_length=250, verbose_name='email subject')),
                ('attachment', models.FileField(upload_to='attachments', verbose_name='email attach,emt')),
                ('email_body', models.TextField(verbose_name='email message')),
                ('email_reciever', models.ManyToManyField(to='core.EmailContacts', verbose_name='email recipient')),
            ],
        ),
    ]
