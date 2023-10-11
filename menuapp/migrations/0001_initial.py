# Generated by Django 4.1.7 on 2023-10-11 01:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DataMeja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomor_meja', models.CharField(max_length=10, unique=True)),
                ('status_aktif_meja', models.BooleanField(default=True)),
                ('keterangan_meja', models.TextField()),
                ('kapasitas_meja', models.PositiveIntegerField()),
                ('status_terpakai', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DataMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_menu', models.CharField(max_length=10, unique=True)),
                ('nama_menu_lengkap', models.CharField(max_length=255)),
                ('nama_menu_singkat', models.CharField(max_length=50)),
                ('gambar_menu', models.ImageField(upload_to='menu_images/')),
                ('keterangan_menu', models.TextField()),
                ('status_aktif_menu', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceSequence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomor_meja', models.CharField(max_length=10, unique=True)),
                ('nota_sequence', models.PositiveIntegerField(default=1)),
                ('faktur_sequence', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='JenisSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_size', models.CharField(max_length=10, unique=True)),
                ('nama_size', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='KelompokMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_kelompok', models.CharField(max_length=10, unique=True)),
                ('nama_kelompok', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PenjualanFaktur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_penjualan_faktur', models.CharField(max_length=20, unique=True)),
                ('nomor_nota_penjualan', models.CharField(max_length=20)),
                ('nomor_meja', models.CharField(max_length=10)),
                ('cara_pembayaran', models.CharField(max_length=50)),
                ('status_lunas', models.BooleanField(default=False)),
                ('jenis_pembayaran', models.CharField(max_length=50)),
                ('tanggal_penjualan', models.DateTimeField(auto_now_add=True)),
                ('total_penjualan', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pembayaran', models.DecimalField(decimal_places=2, max_digits=10)),
                ('kembalian', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='PenjualanDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomor_nota_penjualan', models.CharField(max_length=20)),
                ('harga_menu', models.DecimalField(decimal_places=2, max_digits=10)),
                ('jumlah_harga', models.DecimalField(decimal_places=2, max_digits=10)),
                ('qty_menu', models.PositiveIntegerField()),
                ('kode_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuapp.datamenu')),
            ],
        ),
        migrations.CreateModel(
            name='JenisMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_jenis', models.CharField(max_length=10, unique=True)),
                ('nama_jenis', models.CharField(max_length=255)),
                ('kelompok_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuapp.kelompokmenu')),
            ],
        ),
        migrations.CreateModel(
            name='HargaMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('harga_menu', models.DecimalField(decimal_places=2, max_digits=10)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuapp.datamenu')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuapp.jenissize')),
            ],
        ),
        migrations.AddField(
            model_name='datamenu',
            name='jenis_menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuapp.jenismenu'),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(default=0)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuapp.datamenu')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuapp.jenissize')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
