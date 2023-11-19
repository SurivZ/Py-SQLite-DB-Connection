# Py-SQLite-DB-Connection `v1.0.4`

Este paquete proporciona una clase `Connect` para gestionar conexiones y operaciones CRUD en bases de datos SQLite3 de manera sencilla y estandarizada.

## Instalación

Puedes instalar el paquete utilizando pip:

```bash
pip install PySQLiteDBConnection
```

## Ejemplo de uso

### Importar el paquete

```Python
from PySQLiteDBConnection import Connect
```

### Crear una instancia de la clase Connect

```Python
db = Connect('path_to_your_database.db')
```

### Establecer conexión a la base de datos

```Python
connected = db.connect()
```

### Mostrar información sobre la conexión con la base de datos

```Python
print(db)
```

### Leer todos los registros de una tabla

```Python
table_data = db.read_table('table_name')
```

### Insertar datos en una tabla

```Python
data_to_insert = {'column1': 'value1', 'column2': 'value2'}
inserted = db.insert_into_table('table_name', data_to_insert)
```

### Actualizar registros en una tabla

```Python
update_data = {'column1': 'new_value'}
condition = {'column2': 'value2'}
updated = db.update_record('table_name', update_data, condition)
```

### Eliminar registros de una tabla

```Python
delete_condition = {'column1': 'value1'}
deleted = db.delete_record('table_name', delete_condition)
```

### Cerrar la conexión con la base de datos

```Python
db.close()
```

## Contribución

¡Las contribuciones son bienvenidas! Si encuentras algún error o tienes sugerencias para mejoras, siéntete libre de abrir un issue o enviar un pull request.
