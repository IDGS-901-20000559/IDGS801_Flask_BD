from db import get_connection

"""

#Consulta de todos  los alumnos
try:
    connection = get_connection()
    with connection.cursor() as curso:
        #Sirve para ejecutar un stored procedure
        curso.execute('call consulta_alumnos()')

        resultset = curso.fetchall()

        for row in resultset:
            print(row)

    connection.close()
    
except Exception as ex:
    print('Error '+ex)

# Consulta de solo un alumno
try:
    connection = get_connection()
    with connection.cursor() as curso:
        #Sirve para ejecutar un stored procedure
        curso.execute('call consulta_alumno(3)')

        resultset = curso.fetchall()

        for row in resultset:
            print(row)

    connection.close()
except Exception as ex:
    print('Error '+ex)

try:
    connection = get_connection()
    with connection.cursor() as curso:
        #Sirve para ejecutar un stored procedure
        curso.execute('call agrega_alumno(%s, %s, %s)', ('valor1', 'valor2', 'valor3'))

        resultset = curso.fetchall()

        for row in resultset:
            print(row)

    connection.close()
    
except Exception as ex:
    print('Error '+ex)
"""