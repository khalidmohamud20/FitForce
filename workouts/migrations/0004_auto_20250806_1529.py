from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0003_exercise_name'),  # This should point to the previous migration
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
