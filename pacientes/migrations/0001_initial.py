# Generated by Django 5.1.6 on 2025-02-15 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.CharField(blank=True, max_length=16, null=True)),
                ('foto', models.ImageField(upload_to='fotos')),
                ('pagamento_em_dia', models.BooleanField(default=True)),
                ('queixa', models.CharField(choices=[('TDAH', 'Transtorno do Déficit de Atenção com Hiperatividade'), ('TEA', 'Transtorno do Espectro Autista'), ('D', 'Depressão'), ('A', 'Ansiedade'), ('TAG', 'Transtorno de Ansiedade Generalizada'), ('TA', 'Transtorno Alimentar'), ('TOC', 'Transtorno Obsessivo Compulsivo'), ('TPS', 'Transtorno do Processamento Sensorial'), ('TDI', 'Transtorno Dissociativo de Identidade'), ('SEP', 'Síndrome do Esgotamento Profissional (Burnout)'), ('DISL', 'Dislexia'), ('DISC', 'Discalculia')], max_length=4)),
            ],
        ),
    ]
