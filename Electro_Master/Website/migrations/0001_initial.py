# Generated by Django 4.2.4 on 2023-09-07 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=30)),
                ('image', models.ImageField(upload_to='./images')),
                ('preco', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('quant', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NewProdutos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=30)),
                ('image', models.ImageField(upload_to='./images')),
                ('precoD', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('precoA', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('new', models.CharField(choices=[('1', 'None'), ('2', 'New')], default='1', max_length=20)),
                ('desconto', models.CharField(choices=[('1', 'None'), ('2', '-10%'), ('3', '-30%')], default='1', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=30)),
                ('image', models.ImageField(upload_to='./images')),
                ('buttom', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=30)),
                ('image', models.ImageField(upload_to='./images')),
                ('precoD', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('precoA', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('new', models.CharField(choices=[('1', 'None'), ('2', 'New')], default='1', max_length=20)),
                ('desconto', models.CharField(choices=[('1', 'None'), ('2', '-10%'), ('3', '-30%')], default='1', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TopProdutos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=30)),
                ('image', models.ImageField(upload_to='./images')),
                ('precoD', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('precoA', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('new', models.CharField(choices=[('1', 'None'), ('2', 'New')], default='1', max_length=20)),
                ('desconto', models.CharField(choices=[('1', 'None'), ('2', '-10%'), ('3', '-30%')], default='1', max_length=20)),
            ],
        ),
    ]
