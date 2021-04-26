from mysql.connector import connection
from mysql.connector import Error

import os
from pathlib import Path



# Função para receber as variaveis e salvá-las dentro da tabela no banco de dados

def inserir(datasT, remetenteT, assuntoT, mensagemT):
    try:
        con = connection.MySQLConnection(
                host='localhost',
                user='root',
                password= 'root',
                database='testeml'
                )

        cursor = con.cursor()

        query = """INSERT INTO dados (datas, remetente, assunto, mensagem)
                   VALUES ('%s', '%s', '%s', '%s')""" % (datasT, remetenteT, assuntoT, mensagemT)

        cursor.execute(query)
        con.commit()
        cursor.close()
        print('Dado inserido no banco de dados com sucesso')
    except Error as erro:
        print("Falha ao inserir dados no banco de dados: {}".format(erro))
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
            print("Conexão encerrada com sucesso")
