from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='telephone',
            field=models.CharField(default='', max_length=13),
            preserve_default=False,
        ),
    ]
