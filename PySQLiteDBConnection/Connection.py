from sqlite3 import connect, Cursor, Connection
from typing import List, Tuple, Dict, Any as any


class Connect:
    """
    Clase para manejar la conexión y operaciones CRUD en una base de datos SQLite3.

    Args:
        path (str): Ruta al archivo de la base de datos SQLite3.
        __connection (Connection): Conexión a la base de datos.
        __cursor (Cursor): Cursor para ejecutar consultas SQL.
        __connection_status (bool): Variable que muestra el estado de la conexión con la base de datos.
    """
    path: str
    __connection: Connection
    __cursor: Cursor
    __connection_status: bool = False

    def __init__(self, path: str) -> None:
        """
        Inicializa una nueva instancia de la clase Connect.

        Args:
            - path: Ruta al archivo de la base de datos SQLite3.
        """
        self.path = path

    def __str__(self) -> str:
        """
        Método que devuelve información relacionada con la conexión a la base de datos.
        """
        return f"Base de datos: {self.path}\nEstado: {('Sin conexión', 'Conexión establecida')[self.__connection_status]}"

    def connect(self) -> bool:
        """
        Establece una conexión con la base de datos SQLite3.

        Returns:
            - True si la conexión es exitosa, False de lo contrario.
        """
        try:
            self.__connection = connect(self.path)
            self.__cursor = self.__connection.cursor()
            self.__connection_status = True
            print('[¡] Conexión exitosa')
            return True
        except Exception as e:
            print('[!] Error al conectar:', e)
            return False

    def read_table(self, table_name: str) -> List[Tuple[int | float | str, ...]]:
        """
        Lee todos los registros de una tabla en particular.

        Args:
            - table_name: Nombre de la tabla a leer.

        Returns:
            - Lista de tuplas que representan los registros de la tabla.
        """
        try:
            query = f"SELECT * FROM {table_name}"
            self.__cursor.execute(query)
            rows = self.__cursor.fetchall()
            return rows
        except Exception as e:
            print('[!] Error al leer la tabla:', e)
            return []

    def read_table_with_condition(self, table_name: str, condition: Dict[str, any]) -> List[Tuple[int | float | str, ...]]:
        """
        Lee registros de una tabla que cumplen una condición específica.

        Args:
            - table_name: Nombre de la tabla a leer.
            - condition: Diccionario con las condiciones de búsqueda.

        Returns:
            - Lista de tuplas que representan los registros que cumplen la condición.
        """
        try:
            condition_columns = ' AND '.join([f"{column} = ?" for column in condition.keys()])
            query = f"SELECT * FROM {table_name} WHERE {condition_columns}"
            self.__cursor.execute(query, tuple(condition.values()))
            rows = self.__cursor.fetchall()
            return rows
        except Exception as e:
            print('[!] Error al leer la tabla con la condición:', e)
            return []

    def insert_into_table(self, table_name: str, data: Dict[str, any]) -> bool:
        """
        Inserta datos en una tabla.

        Args:
            - table_name: Nombre de la tabla donde se insertarán los datos.
            - data: Diccionario con los datos a insertar.

        Returns:
            - True si la operación es exitosa, False de lo contrario.
        """
        try:
            columns = ', '.join(data.keys())
            values = ', '.join(['?' for _ in range(len(data))])
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
            self.__cursor.execute(query, tuple(data.values()))
            self.__connection.commit()
            print('[¡] Datos insertados exitosamente')
            return True
        except Exception as e:
            print('[!] Error al insertar datos:', e)
            return False

    from typing import Dict, Any

    def update_record(self, table_name: str, data: Dict[str, Any], condition: Dict[str, Any]) -> bool:
        """
        Actualiza registros en una tabla.

        Args:
            - table_name: Nombre de la tabla a actualizar.
            - data: Diccionario con los datos actualizados.
            - condition: Diccionario con la condición para filtrar los registros a actualizar.

        Returns:
            - True si la operación es exitosa, False de lo contrario.
        """
        try:
            set_clause = ', '.join([f"{key} = ?" for key in data.keys()])
            where_clause = ' AND '.join([f"{key} = ?" for key in condition.keys()])
            query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
            values = tuple(data.values()) + tuple(condition.values())
            self.__cursor.execute(query, values)
            self.__connection.commit()
            print('[¡] Datos actualizados exitosamente')
            return True
        except Exception as e:
            print('[!] Error al actualizar datos:', e)
            return False

    from typing import Dict

    def delete_record(self, table_name: str, condition: Dict[str, Any]) -> bool:
        """
        Elimina registros de una tabla.

        Args:
            - table_name: Nombre de la tabla de la cual eliminar los registros.
            - condition: Diccionario con el campo y valor a buscar para filtrar los registros a eliminar.

        Returns:
            - True si la operación es exitosa, False de lo contrario.
        """
        try:
            query = f"DELETE FROM {table_name} WHERE "
            conditions = [f"{field} = {value}" for field, value in condition.items()]
            query += " AND ".join(conditions)
            self.__cursor.execute(query)
            self.__connection.commit()
            print('[¡] Datos eliminados exitosamente')
            return True
        except Exception as e:
            print('[!] Error al eliminar datos:', e)
            return False

    def close(self) -> None:
        """
        Cierra la conexión con la base de datos.
        """
        self.__cursor.close()
        self.__connection.close()
        self.__connection_status = False
