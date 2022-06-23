# Generated by Django 4.0.4 on 2022-05-12 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helper_app', '0002_uchotchiqarishsababi'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fuqaro', '0024_alter_usmir_familiya_alter_usmir_ism_and_more'),
        ('psix_uchot', '0007_alter_asosiy_add_user_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='asosiy_psix_uchot_chiqarish',
            name='uchotdan_chiqargan_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Kirituvchi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asosiy_psix_uchot_chiqarish',
            name='uchotdan_chiqarish_sababi',
            field=models.ForeignKey(default=23, on_delete=django.db.models.deletion.PROTECT, to='helper_app.uchotchiqarishsababi', verbose_name='Uchotdan chiqarish sababi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asosiy_psix_uchot_chiqarish',
            name='uchotdan_chiqarish_sababi_mkb10_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='fuqaro.mkb10', verbose_name='Hisobdan chiqarilgan sababi mkb10'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asosiy_psix_uchot_chiqarish',
            name='uchotdan_chiqarish_sababi_text',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='asosiy_psix_uchot_chiqarish',
            name='uchotdan_chiqqan_sana',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='asosiy_psix_uchot_chiqarish',
            name='qushulgan_sana',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='asosiy_psix_uchot_chiqarish',
            name='yangilangan_sana',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]