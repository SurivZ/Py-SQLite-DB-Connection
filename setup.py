from setuptools import setup, find_packages

setup(
    name='PySQLiteDBConnection',
    version='1.0.3',
    author='SurivZ',
    author_email='franklinserrano23@email.com',
    description='Paquete para manejar conexiones de bases de datos SQLite3 y operaciones CRUD.',
    long_description="""# Py-SQLite-DB-Connection

Este paquete proporciona una clase `Connect` para gestionar conexiones y operaciones CRUD en bases de datos SQLite3 de manera sencilla y estandarizada.

## Instalación

Puedes instalar el paquete utilizando pip:
```nash
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
  ¡Las contribuciones son bienvenidas! Si encuentras algún error o tienes sugerencias para mejoras, siéntete libre de abrir un issue o enviar un pull request.""",
    long_description_content_type='text/markdown',
    url='https://github.com/SurivZ/Py-SQLite-DB-Connection',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.7',
    install_requires=[],
)
