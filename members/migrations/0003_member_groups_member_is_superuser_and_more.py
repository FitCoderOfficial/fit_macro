# Generated by Django 4.1.7 on 2023-02-17 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("members", "0002_rename_is_admin_member_is_staff_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="member",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="member",
            name="is_superuser",
            field=models.BooleanField(
                default=False,
                help_text="Designates that this user has all permissions without explicitly assigning them.",
                verbose_name="superuser status",
            ),
        ),
        migrations.AddField(
            model_name="member",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
        migrations.AlterField(
            model_name="member",
            name="activity_level",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="member",
            name="age",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="member",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="member", name="name", field=models.CharField(max_length=50),
        ),
    ]
