#!/usr/bin/env python3
"""
=============================================================================
MAPA CROMOSÓMICO DE Yuca (Manihot esculenta)
=============================================================================
Genera un ideograma cromosómico con posiciones de genes/QTLs inventados.
Datos simulados para 18 cromosomas de yuca.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

# =============================================================================
# DATOS INVENTADOS - Mapa cromosómico de yuca
# =============================================================================

CROMOSOMAS = {
    'Me_01': 42.1, 'Me_02': 38.7, 'Me_03': 36.2, 'Me_04': 34.8,
    'Me_05': 33.1, 'Me_06': 31.5, 'Me_07': 29.8, 'Me_08': 28.3,
    'Me_09': 26.7, 'Me_10': 25.2, 'Me_11': 23.8, 'Me_12': 22.1,
    'Me_13': 20.5, 'Me_14': 19.2, 'Me_15': 17.8, 'Me_16': 16.3,
    'Me_17': 15.1, 'Me_18': 13.7
}

QTLs = {
    'Me_01': [('YLD', 12.3, 15.8, '#e74c3c'),
              ('DRO', 28.5, 32.1, '#3498db'),
              ('STARCH', 5.2, 8.9, '#f39c12')],
    'Me_02': [('CYAN', 18.7, 22.3, '#2ecc71'),
              ('RFLW', 8.1, 11.5, '#9b59b6')],
    'Me_03': [('CMS', 15.0, 19.5, '#e67e22'),
              ('BLR', 30.2, 34.8, '#1abc9c')],
    'Me_04': [('YLD', 20.1, 24.6, '#e74c3c'),
              ('PHT', 10.5, 14.2, '#34495e')],
    'Me_05': [('RFLW', 25.3, 29.1, '#9b59b6')],
    'Me_06': [('DRO', 12.8, 16.5, '#3498db'),
              ('CMS', 22.4, 26.9, '#e67e22')],
    'Me_07': [('STARCH', 8.3, 12.0, '#f39c12'),
              ('YLD', 18.5, 22.2, '#e74c3c')],
    'Me_08': [('CYAN', 5.7, 9.2, '#2ecc71')],
    'Me_09': [('BLR', 14.6, 18.3, '#1abc9c'),
              ('PHT', 25.8, 29.5, '#34495e')],
    'Me_10': [('CMS', 10.2, 14.8, '#e67e22')],
    'Me_11': [('DRO', 19.4, 23.0, '#3498db')],
    'Me_12': [('YLD', 7.5, 11.2, '#e74c3c'),
              ('RFLW', 16.8, 20.5, '#9b59b6')],
    'Me_13': [('STARCH', 3.2, 6.8, '#f39c12')],
    'Me_14': [('PHT', 11.5, 15.1, '#34495e')],
    'Me_15': [('BLR', 8.9, 12.5, '#1abc9c')],
    'Me_16': [('CYAN', 4.1, 7.8, '#2ecc71')],
    'Me_17': [('CMS', 6.3, 10.0, '#e67e22')],
    'Me_18': [('YLD', 2.5, 6.1, '#e74c3c')]
}

GENES_MARCADORES = {
    'Me_01': [('SSRY145', 8.4), ('SSRY22', 21.3), ('SSRY88', 35.7)],
    'Me_02': [('SSRY55', 14.2), ('SSRY199', 27.8)],
    'Me_03': [('SSRY12', 10.5), ('SSRY77', 24.1)],
    'Me_04': [('SSRY200', 16.8), ('SSRY33', 30.2)],
    'Me_05': [('SSRY91', 21.5)],
    'Me_06': [('SSRY44', 9.3), ('SSRY167', 25.6)],
    'Me_07': [('SSRY120', 14.7)],
    'Me_08': [('SSRY8', 7.2)],
    'Me_09': [('SSRY155', 20.4)],
    'Me_10': [('SSRY63', 11.8)],
    'Me_11': [('SSRY110', 18.3)],
    'Me_12': [('SSRY28', 13.6)],
    'Me_13': [('SSRY99', 5.4)],
    'Me_14': [('SSRY176', 12.9)],
    'Me_15': [('SSRY7', 10.1)],
    'Me_16': [('SSRY42', 5.8)],
    'Me_17': [('SSRY85', 8.0)],
    'Me_18': [('SSRY11', 4.3)]
}

# =============================================================================
# LEYENDA DE COLORES
# =============================================================================

LEYENDA = {
    'YLD':  ('#e74c3c', 'Rendimiento (YLD)'),
    'DRO':  ('#3498db', 'Tolerancia sequía (DRO)'),
    'STARCH': ('#f39c12', 'Contenido almidón (STARCH)'),
    'CYAN': ('#2ecc71', 'Contenido cianuro (CYAN)'),
    'RFLW': ('#9b59b6', 'Floración (RFLW)'),
    'CMS':  ('#e67e22', 'Resistencia CMS (CMS)'),
    'BLR':  ('#1abc9c', 'Resistencia tizón (BLR)'),
    'PHT':  ('#34495e', 'Altura planta (PHT)')
}

# =============================================================================
# FUNCIÓN PRINCIPAL
# =============================================================================

def generar_mapa_cromosomico():
    """Genera el ideograma cromosómico completo"""
    
    n_crom = len(CROMOSOMAS)
    fig, ax = plt.subplots(1, 1, figsize=(14, 16))
    
    y_pos = 0
    y_ticks = []
    y_labels = []
    
    for crom, largo in CROMOSOMAS.items():
        y_ticks.append(y_pos + 3)
        y_labels.append(crom)
        
        # Dibujar cromosoma (rectángulo redondeado)
        chrom_rect = patches.FancyBboxPatch(
            (0, y_pos), largo, 5.5,
            boxstyle="round,pad=0.3",
            facecolor='#ecf0f1', edgecolor='#2c3e50', linewidth=1.5
        )
        ax.add_patch(chrom_rect)
        
        # Centrómetro (punto de constricción)
        ax.plot(largo/2, y_pos + 2.75, 'o', color='#c0392b', 
                markersize=8, zorder=5)
        
        # Dibujar QTLs
        if crom in QTLs:
            for qtl, inicio, fin, color in QTLs[crom]:
                rect = patches.Rectangle(
                    (inicio, y_pos + 1), fin - inicio, 3.5,
                    facecolor=color, alpha=0.75, edgecolor='black',
                    linewidth=0.5
                )
                ax.add_patch(rect)
                # Etiqueta del QTL
                ax.text((inicio + fin)/2, y_pos + 2.75, qtl,
                       ha='center', va='center', fontsize=7,
                       fontweight='bold', color='white')
        
        # Dibujar genes marcadores
        if crom in GENES_MARCADORES:
            for gen, pos in GENES_MARCADORES[crom]:
                ax.plot(pos, y_pos + 5.8, 'v', color='#2c3e3e',
                       markersize=6, zorder=5)
                ax.text(pos, y_pos + 6.5, gen, ha='center', va='bottom',
                       fontsize=5, rotation=45, color='#2c3e50')
        
        y_pos += 9
    
    # Formato del gráfico
    ax.set_xlim(-3, max(CROMOSOMAS.values()) + 5)
    ax.set_ylim(-2, y_pos + 2)
    ax.set_xlabel('Posición (Mb)', fontsize=12, fontweight='bold')
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(y_labels, fontsize=10)
    ax.set_title('🧬 Mapa Cromosómico de Yuca (Manihot esculenta)\n'
                'QTLs y marcadores SSR simulados',
                fontsize=14, fontweight='bold', pad=20)
    ax.set_facecolor('#fafafa')
    fig.patch.set_facecolor('white')
    
    # Leyenda
    legend_elements = []
    for key, (color, label) in LEYENDA.items():
        legend_elements.append(patches.Patch(facecolor=color, 
                                            edgecolor='black',
                                            alpha=0.75, label=label))
    ax.legend(handles=legend_elements, loc='upper right', 
             fontsize=8, framealpha=0.9)
    
    plt.tight_layout()
    
    # Guardar figura
    output = os.path.join(os.path.expanduser('~'), 'repos', 
                         'yuca-chromosome-map', 'mapa_cromosomico_yuca.png')
    os.makedirs(os.path.dirname(output), exist_ok=True)
    plt.savefig(output, dpi=300, bbox_inches='tight')
    print(f"✅ Mapa guardado: {output}")
    
    plt.show()

if __name__ == '__main__':
    print("🧬 Generando mapa cromosómico de yuca...")
    print(f"   {len(CROMOSOMAS)} cromosomas")
    print(f"   {sum(len(v) for v in QTLs.values())} QTLs")
    print(f"   {sum(len(v) for v in GENES_MARCADORES.values())} marcadores SSR")
    print("=" * 60)
    generar_mapa_cromosomico()
    print("🎉 ¡Mapa cromosómico generado exitosamente!")
