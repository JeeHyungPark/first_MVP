# Generated by Django 3.0.9 on 2020-09-02 13:05

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lectures', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='이름')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='이메일')),
                ('lecture_count', models.PositiveIntegerField(default=0, verbose_name='시청한 강의 개수')),
                ('is_subscriber', models.BooleanField(default=False, verbose_name='구독의향')),
                ('is_staff', models.BooleanField(db_index=True, default=True, verbose_name='스태프')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='계정 활성')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
                'ordering': ['-is_subscriber', 'username'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lectures.Lecture', verbose_name='강의')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자')),
            ],
            options={
                'verbose_name': '시청기록',
                'verbose_name_plural': '시청기록',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='user',
            name='lecture_history',
            field=models.ManyToManyField(through='accounts.History', to='lectures.Lecture', verbose_name='시청한 강의'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddConstraint(
            model_name='history',
            constraint=models.UniqueConstraint(fields=('user', 'lecture'), name='history_pair'),
        ),
    ]
