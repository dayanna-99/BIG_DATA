import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar estilo de gráficas
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Cargar el archivo CSV
df = pd.read_csv('datos_sinteticos.csv')

print("="*80)
print("ANÁLISIS DE DATOS DE CAMPAÑAS PUBLICITARIAS")
print("="*80)

# 1. INFORMACIÓN GENERAL
print("\n1. INFORMACIÓN GENERAL DEL DATASET")
print("-" * 80)
print(f"Número de registros: {len(df)}")
print(f"Número de columnas: {len(df.columns)}")
print(f"Rango de fechas: {df['fecha_campana'].min()} - {df['fecha_campana'].max()}")

# 2. DISTRIBUCIÓN POR PLATAFORMA
print("\n2. DISTRIBUCIÓN POR PLATAFORMA")
print("-" * 80)
plataforma_count = df['plataforma'].value_counts()
for plat, count in plataforma_count.items():
    print(f"  {plat}: {count} campañas")

# 3. DISTRIBUCIÓN POR TIPO DE CAMPAÑA
print("\n3. DISTRIBUCIÓN POR TIPO DE CAMPAÑA")
print("-" * 80)
tipo_count = df['tipo_campana'].value_counts()
for tipo, count in tipo_count.items():
    print(f"  {tipo}: {count} campañas")

# 4. DISTRIBUCIÓN POR AUDIENCIA OBJETIVO
print("\n4. DISTRIBUCIÓN POR AUDIENCIA OBJETIVO")
print("-" * 80)
audiencia_count = df['audiencia_objetivo'].value_counts().sort_index()
for aud, count in audiencia_count.items():
    print(f"  {aud}: {count} campañas")

# 5. ESTADÍSTICAS FINANCIERAS
print("\n5. ESTADÍSTICAS FINANCIERAS")
print("-" * 80)
print(f"Presupuesto diario total: ${df['presupuesto_diario'].sum():,.2f}")
print(f"Presupuesto diario promedio: ${df['presupuesto_diario'].mean():,.2f}")
print(f"Costo total general: ${df['costo_total'].sum():,.2f}")
print(f"Revenue total generado: ${df['revenue_generado'].sum():,.2f}")
print(f"Ganancia neta total: ${(df['revenue_generado'].sum() - df['costo_total'].sum()):,.2f}")

# 6. ESTADÍSTICAS DE PERFORMANCE
print("\n6. ESTADÍSTICAS DE PERFORMANCE")
print("-" * 80)
print(f"Total de impresiones: {df['impresiones'].sum():,.0f}")
print(f"Total de clicks: {df['clicks'].sum():,.0f}")
print(f"Total de conversiones: {df['conversiones'].sum():,.0f}")
print(f"Alcance total combinado: {df['alcance'].sum():,.0f}")

print(f"\nCTR (Click-Through Rate) promedio: {df['ctr'].mean():.2f}%")
print(f"Conversion Rate promedio: {df['conversion_rate'].mean():.2f}%")
print(f"Engagement Rate promedio: {df['engagement_rate'].mean():.2f}%")
print(f"ROAS (Return on Ad Spend) promedio: {df['roas'].mean():.2f}")

# 7. COSTOS POR ACCIÓN
print("\n7. COSTOS Y VALORES POR ACCIÓN")
print("-" * 80)
print(f"CPC (Costo Por Click) promedio: ${df['cpc'].mean():.2f}")
print(f"CPA (Costo Por Acción) promedio: ${df['cpa'].mean():.2f}")

# 8. ANÁLISIS POR PLATAFORMA
print("\n8. ANÁLISIS POR PLATAFORMA")
print("-" * 80)
for plat in df['plataforma'].unique():
    datos_plat = df[df['plataforma'] == plat]
    print(f"\n  {plat}:")
    print(f"    - Campañas: {len(datos_plat)}")
    print(f"    - Revenue total: ${datos_plat['revenue_generado'].sum():,.2f}")
    print(f"    - Costo total: ${datos_plat['costo_total'].sum():,.2f}")
    print(f"    - ROAS promedio: {datos_plat['roas'].mean():.2f}")
    print(f"    - Engagement Rate promedio: {datos_plat['engagement_rate'].mean():.2f}%")

# 9. TOP 5 CAMPAÑAS POR ROAS
print("\n9. TOP 5 CAMPAÑAS POR ROAS (Mejor ROI)")
print("-" * 80)
top_roas = df.nlargest(5, 'roas')[['campana_id', 'plataforma', 'tipo_campana', 'revenue_generado', 'costo_total', 'roas']]
for idx, (i, row) in enumerate(top_roas.iterrows(), 1):
    print(f"  {idx}. {row['campana_id']} ({row['plataforma']}) - ROAS: {row['roas']:.2f}")
    print(f"     Tipo: {row['tipo_campana']}, Revenue: ${row['revenue_generado']:,.2f}, Costo: ${row['costo_total']:,.2f}")

# 10. BOTTOM 5 CAMPAÑAS POR ROAS
print("\n10. BOTTOM 5 CAMPAÑAS POR ROAS (Peor ROI)")
print("-" * 80)
bottom_roas = df.nsmallest(5, 'roas')[['campana_id', 'plataforma', 'tipo_campana', 'revenue_generado', 'costo_total', 'roas']]
for idx, (i, row) in enumerate(bottom_roas.iterrows(), 1):
    print(f"  {idx}. {row['campana_id']} ({row['plataforma']}) - ROAS: {row['roas']:.2f}")
    print(f"     Tipo: {row['tipo_campana']}, Revenue: ${row['revenue_generado']:,.2f}, Costo: ${row['costo_total']:,.2f}")

# 11. ANÁLISIS POR TIPO DE CAMPAÑA
print("\n11. ANÁLISIS POR TIPO DE CAMPAÑA")
print("-" * 80)
for tipo in df['tipo_campana'].unique():
    datos_tipo = df[df['tipo_campana'] == tipo]
    print(f"\n  {tipo}:")
    print(f"    - Campañas: {len(datos_tipo)}")
    print(f"    - Revenue total: ${datos_tipo['revenue_generado'].sum():,.2f}")
    print(f"    - Conversion Rate promedio: {datos_tipo['conversion_rate'].mean():.2f}%")
    print(f"    - ROAS promedio: {datos_tipo['roas'].mean():.2f}")

print("\n" + "="*80)
print("GENERANDO GRÁFICAS...")
print("="*80)

# Crear figura con múltiples subgráficas
fig = plt.figure(figsize=(16, 12))

# 1. Distribución de campañas por plataforma
ax1 = plt.subplot(3, 3, 1)
plataforma_count = df['plataforma'].value_counts()
colors = sns.color_palette("husl", len(plataforma_count))
plataforma_count.plot(kind='bar', ax=ax1, color=colors)
ax1.set_title('Campañas por Plataforma', fontsize=12, fontweight='bold')
ax1.set_xlabel('Plataforma')
ax1.set_ylabel('Cantidad')
ax1.tick_params(axis='x', rotation=45)

# 2. Distribución por tipo de campaña
ax2 = plt.subplot(3, 3, 2)
tipo_count = df['tipo_campana'].value_counts()
tipo_count.plot(kind='bar', ax=ax2, color=sns.color_palette("Set2"))
ax2.set_title('Campañas por Tipo', fontsize=12, fontweight='bold')
ax2.set_xlabel('Tipo de Campaña')
ax2.set_ylabel('Cantidad')
ax2.tick_params(axis='x', rotation=45)

# 3. Distribución por audiencia objetivo
ax3 = plt.subplot(3, 3, 3)
audiencia_count = df['audiencia_objetivo'].value_counts().sort_index()
audiencia_count.plot(kind='bar', ax=ax3, color=sns.color_palette("muted"))
ax3.set_title('Campañas por Audiencia', fontsize=12, fontweight='bold')
ax3.set_xlabel('Rango de Edad')
ax3.set_ylabel('Cantidad')
ax3.tick_params(axis='x', rotation=45)

# 4. Revenue total por plataforma
ax4 = plt.subplot(3, 3, 4)
revenue_por_plat = df.groupby('plataforma')['revenue_generado'].sum().sort_values(ascending=False)
revenue_por_plat.plot(kind='bar', ax=ax4, color='green', alpha=0.7)
ax4.set_title('Revenue Total por Plataforma', fontsize=12, fontweight='bold')
ax4.set_xlabel('Plataforma')
ax4.set_ylabel('Revenue ($)')
ax4.tick_params(axis='x', rotation=45)
ax4.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))

# 5. Costo total por plataforma
ax5 = plt.subplot(3, 3, 5)
costo_por_plat = df.groupby('plataforma')['costo_total'].sum().sort_values(ascending=False)
costo_por_plat.plot(kind='bar', ax=ax5, color='red', alpha=0.7)
ax5.set_title('Costo Total por Plataforma', fontsize=12, fontweight='bold')
ax5.set_xlabel('Plataforma')
ax5.set_ylabel('Costo ($)')
ax5.tick_params(axis='x', rotation=45)
ax5.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))

# 6. ROAS promedio por plataforma
ax6 = plt.subplot(3, 3, 6)
roas_por_plat = df.groupby('plataforma')['roas'].mean().sort_values(ascending=False)
roas_por_plat.plot(kind='bar', ax=ax6, color='orange', alpha=0.7)
ax6.set_title('ROAS Promedio por Plataforma', fontsize=12, fontweight='bold')
ax6.set_xlabel('Plataforma')
ax6.set_ylabel('ROAS')
ax6.tick_params(axis='x', rotation=45)
ax6.axhline(y=df['roas'].mean(), color='blue', linestyle='--', linewidth=2, label=f'Promedio: {df["roas"].mean():.2f}')
ax6.legend()

# 7. Conversion Rate vs CTR por plataforma
ax7 = plt.subplot(3, 3, 7)
plataformas = df['plataforma'].unique()
x = np.arange(len(plataformas))
width = 0.35
cr_vals = [df[df['plataforma'] == p]['conversion_rate'].mean() for p in plataformas]
ctr_vals = [df[df['plataforma'] == p]['ctr'].mean() for p in plataformas]
ax7.bar(x - width/2, cr_vals, width, label='Conversion Rate (%)', alpha=0.8)
ax7.bar(x + width/2, ctr_vals, width, label='CTR (%)', alpha=0.8)
ax7.set_xlabel('Plataforma')
ax7.set_ylabel('Porcentaje (%)')
ax7.set_title('Conversion Rate vs CTR por Plataforma', fontsize=12, fontweight='bold')
ax7.set_xticks(x)
ax7.set_xticklabels(plataformas, rotation=45)
ax7.legend()

# 8. Engagement Rate promedio por tipo de campaña
ax8 = plt.subplot(3, 3, 8)
engagement_por_tipo = df.groupby('tipo_campana')['engagement_rate'].mean().sort_values(ascending=False)
engagement_por_tipo.plot(kind='barh', ax=ax8, color='purple', alpha=0.7)
ax8.set_title('Engagement Rate Promedio por Tipo', fontsize=12, fontweight='bold')
ax8.set_xlabel('Engagement Rate (%)')
ax8.set_ylabel('Tipo de Campaña')

# 9. Scatter: Revenue vs Costo (con color por plataforma)
ax9 = plt.subplot(3, 3, 9)
plataformas_unicas = df['plataforma'].unique()
colores_scatter = sns.color_palette("husl", len(plataformas_unicas))
for i, plat in enumerate(plataformas_unicas):
    datos_plat = df[df['plataforma'] == plat]
    ax9.scatter(datos_plat['costo_total'], datos_plat['revenue_generado'], 
               label=plat, alpha=0.6, s=100, color=colores_scatter[i])
ax9.set_xlabel('Costo Total ($)')
ax9.set_ylabel('Revenue Generado ($)')
ax9.set_title('Revenue vs Costo por Campaña', fontsize=12, fontweight='bold')
ax9.legend(fontsize=8)

plt.tight_layout()
plt.savefig('analisis_campanas_1.png', dpi=300, bbox_inches='tight')
print("\n✓ Gráfica guardada: analisis_campanas_1.png")
plt.show()

# SEGUNDA FIGURA: Análisis más detallado
fig2 = plt.figure(figsize=(16, 10))

# 1. Top 10 campañas por ROAS
ax1 = plt.subplot(2, 3, 1)
top10_roas = df.nlargest(10, 'roas')[['campana_id', 'roas']].set_index('campana_id')
top10_roas.plot(kind='barh', ax=ax1, color='green', alpha=0.7, legend=False)
ax1.set_title('Top 10 Campañas por ROAS', fontsize=12, fontweight='bold')
ax1.set_xlabel('ROAS')

# 2. ROAS por tipo de campaña (Boxplot)
ax2 = plt.subplot(2, 3, 2)
df.boxplot(column='roas', by='tipo_campana', ax=ax2)
ax2.set_title('Distribución de ROAS por Tipo de Campaña', fontsize=12, fontweight='bold')
ax2.set_xlabel('Tipo de Campaña')
ax2.set_ylabel('ROAS')
plt.sca(ax2)
plt.xticks(rotation=45)

# 3. Impresiones vs Conversiones
ax3 = plt.subplot(2, 3, 3)
for i, plat in enumerate(plataformas_unicas):
    datos_plat = df[df['plataforma'] == plat]
    ax3.scatter(datos_plat['impresiones'], datos_plat['conversiones'], 
               label=plat, alpha=0.6, s=80, color=colores_scatter[i])
ax3.set_xlabel('Impresiones')
ax3.set_ylabel('Conversiones')
ax3.set_title('Impresiones vs Conversiones', fontsize=12, fontweight='bold')
ax3.legend(fontsize=8)

# 4. CPC vs CPA por plataforma
ax4 = plt.subplot(2, 3, 4)
cpc_cpa = df.groupby('plataforma')[['cpc', 'cpa']].mean()
cpc_cpa.plot(kind='bar', ax=ax4, alpha=0.8)
ax4.set_title('Costo Por Click vs Costo Por Acción', fontsize=12, fontweight='bold')
ax4.set_xlabel('Plataforma')
ax4.set_ylabel('Costo ($)')
ax4.tick_params(axis='x', rotation=45)
ax4.legend(['CPC', 'CPA'])

# 5. Evolución temporal de conversiones (por mes)
ax5 = plt.subplot(2, 3, 5)
df['fecha_campana'] = pd.to_datetime(df['fecha_campana'])
conversiones_por_mes = df.groupby(df['fecha_campana'].dt.to_period('M'))['conversiones'].sum()
conversiones_por_mes.plot(kind='line', ax=ax5, marker='o', color='blue', linewidth=2)
ax5.set_title('Conversiones por Mes', fontsize=12, fontweight='bold')
ax5.set_xlabel('Mes')
ax5.set_ylabel('Conversiones')
ax5.grid(True, alpha=0.3)

# 6. Distribución de CTR
ax6 = plt.subplot(2, 3, 6)
ax6.hist(df['ctr'], bins=30, color='skyblue', edgecolor='black', alpha=0.7)
ax6.set_title('Distribución del CTR', fontsize=12, fontweight='bold')
ax6.set_xlabel('CTR (%)')
ax6.set_ylabel('Frecuencia')
ax6.axvline(df['ctr'].mean(), color='red', linestyle='--', linewidth=2, label=f'Media: {df["ctr"].mean():.2f}%')
ax6.legend()

plt.tight_layout()
plt.savefig('analisis_campanas_2.png', dpi=300, bbox_inches='tight')
print("✓ Gráfica guardada: analisis_campanas_2.png")
plt.show()

# TERCERA FIGURA: Resumen de métricas clave
fig3 = plt.figure(figsize=(14, 8))

# 1. Revenue vs Costo acumulado por plataforma
ax1 = plt.subplot(2, 2, 1)
comparativa = df.groupby('plataforma')[['revenue_generado', 'costo_total']].sum()
comparativa.plot(kind='bar', ax=ax1, alpha=0.8, color=['green', 'red'])
ax1.set_title('Revenue vs Costo Total por Plataforma', fontsize=12, fontweight='bold')
ax1.set_xlabel('Plataforma')
ax1.set_ylabel('Monto ($)')
ax1.tick_params(axis='x', rotation=45)
ax1.legend(['Revenue', 'Costo'])

# 2. Ganancia neta por plataforma
ax2 = plt.subplot(2, 2, 2)
ganancia = df.groupby('plataforma').apply(lambda x: (x['revenue_generado'] - x['costo_total']).sum())
colores_ganancia = ['green' if x > 0 else 'red' for x in ganancia]
ganancia.plot(kind='bar', ax=ax2, color=colores_ganancia, alpha=0.7)
ax2.set_title('Ganancia Neta por Plataforma', fontsize=12, fontweight='bold')
ax2.set_xlabel('Plataforma')
ax2.set_ylabel('Ganancia Neta ($)')
ax2.tick_params(axis='x', rotation=45)
ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))

# 3. Alcance por audiencia objetivo
ax3 = plt.subplot(2, 2, 3)
alcance_por_aud = df.groupby('audiencia_objetivo')['alcance'].sum().sort_values(ascending=False)
alcance_por_aud.plot(kind='barh', ax=ax3, color='teal', alpha=0.7)
ax3.set_title('Alcance Total por Audiencia Objetivo', fontsize=12, fontweight='bold')
ax3.set_xlabel('Alcance')

# 4. Pie chart: Distribución de presupuesto
ax4 = plt.subplot(2, 2, 4)
presupuesto_por_plat = df.groupby('plataforma')['presupuesto_diario'].sum()
colors_pie = sns.color_palette("husl", len(presupuesto_por_plat))
ax4.pie(presupuesto_por_plat, labels=presupuesto_por_plat.index, autopct='%1.1f%%', 
        colors=colors_pie, startangle=90)
ax4.set_title('Distribución del Presupuesto Diario', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('analisis_campanas_3.png', dpi=300, bbox_inches='tight')
print("✓ Gráfica guardada: analisis_campanas_3.png")
plt.show()

print("\n" + "="*80)
print("FIN DEL ANÁLISIS - Se han generado 3 archivos de gráficas:")
print("  1. analisis_campanas_1.png - Análisis general")
print("  2. analisis_campanas_2.png - Análisis detallado")
print("  3. analisis_campanas_3.png - Resumen de métricas clave")
print("="*80)
