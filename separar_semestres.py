import pandas as pd

# Leer el excel y almacenar en un DataFrame
df = pd.read_excel('inversion_separada_semestres.xlsx')

# Para cada region y año, separar la primera mitad de la cantidad total de datos en semestre 1 y la otra en el 2
df['Semestre'] = 0  # Inicializar la columna Semestre
df['Fecha'] = ''    # Inicializar la columna Fecha

# Obtener todas las combinaciones únicas de región y año
regiones = df['REGIÓN'].unique()
años = df['AÑO'].unique()

for region in regiones:
    for año in años:
        # Filtrar datos por región y año
        mask = (df['REGIÓN'] == region) & (df['AÑO'] == año)
        indices = df[mask].index
        
        if len(indices) > 0:
            total_filas = len(indices)
            mitad = total_filas // 2
            
            # Asignar semestre 1 a la primera mitad
            df.loc[indices[:mitad], 'Semestre'] = 1
            df.loc[indices[:mitad], 'Fecha'] = f'01-01-{año}'
            
            # Asignar semestre 2 a la segunda mitad
            df.loc[indices[mitad:], 'Semestre'] = 2
            df.loc[indices[mitad:], 'Fecha'] = f'01-07-{año}'

# Guardar el DataFrame modificado en un nuevo archivo excel
df.to_excel('inversion_semestres.xlsx', index=False)
print("\n✓ Archivo 'inversion_semestres.xlsx' creado con éxito.")