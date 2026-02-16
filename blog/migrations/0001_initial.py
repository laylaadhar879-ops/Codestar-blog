from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # usually empty for the first migration
    ]

    operations = [
        # Example: create a model
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
        ),
    ]
