from pinotdb import connect
import pandas as pd

# Conectar al broker de Pinot
# Reemplaza 'broker_host' y 'broker_port' con la IP y puerto de tu broker (por ejemplo, 10.4.45.112:8099)
connection = connect(host='10.4.45.112', port=8099)

# Crear un cursor para ejecutar consultas
cursor = connection.cursor()

# Ejecutar la consulta
query = "SELECT * FROM transcript LIMIT 10"
cursor.execute(query)

# Recuperar los resultados como una lista de tuplas
results = cursor.fetchall()

# Convertir los resultados en un DataFrame para mejor legibilidad
columns = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
df = pd.DataFrame(results, columns=columns)

# Mostrar los resultados
print(df)

# Exportar a CSV si lo necesitas
# df.to_csv("transcript_results.csv", index=False)
