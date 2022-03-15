import sqlite3
from config import db


def crear_tabla_inventario():
    conexion = sqlite3.connect(db.nombre)
    try:
        conexion.execute("""
                create table inventario (
                    codigo integer primary key autoIncrement,
                    descripcion text,
                    nombre text,
                    cantidad real
                    )
                """)
        print("La tabla inventario se creo exitosamente")
    except sqlite3.OperationalError:
        print("La tabla inventario ya fue creada")
    conexion.close()


def insertar_valores_inventario():
    conexion = sqlite3.connect(db.nombre)
    try:
        print("Agregando datos")
        query = """insert into inventario(descripcion,nombre,cantidad)
                    values(?,?,?)"""
        conexion.execute(query, ("Vegetal", "Romero", 24))
        conexion.commit()
        print("Datos agregados")
    except sqlite3.OperationalError:
        print("fallo al insertar en la tabla inventario")
    conexion.close()


def listar_valores_inventario():
    conexion = sqlite3.connect(db.nombre)
    try:
        print("Obteniendo datos")
        cursor = conexion.execute("select nombre, cantidad from inventario")
        for fila in cursor:
            print(fila)
    except sqlite3.OperationalError:
        print("fallo listar la tabla inventario")
    conexion.close()


def buscar_por_id(id):
    conexion = sqlite3.connect(db.nombre)
    try:
        print("Obteniendo datos de id", id)
        query = """
                    select nombre, cantidad
                    from inventario
                    where codigo = {codigo}
                """
        cursor = conexion.execute(query.format(codigo=id))
        fila = cursor.fetchone()
        if fila is not None:
            print(fila)

        else:
            print("No existe dato con id", id)

    except sqlite3.OperationalError:
        print("fallo al buscar por id", id)
    conexion.close()
