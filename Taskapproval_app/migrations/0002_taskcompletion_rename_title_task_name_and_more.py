# Generated by Django 4.2.5 on 2024-01-16 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Taskapproval_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskCompletion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='task',
            name='assigned_user',
        ),
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='task',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Taskapproval_app.department'),
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='taskcompletion',
            name='new_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='new_task', to='Taskapproval_app.task'),
        ),
        migrations.AddField(
            model_name='taskcompletion',
            name='original_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='original_task', to='Taskapproval_app.task'),
        ),
    ]
