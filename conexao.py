from mysql.connector import connection
from mysql.connector import Error

import os
from pathlib import Path



# Função para receber as variaveis e salvá-las dentro do nosso banco de dados, na tabela tb_abertura
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
        print('Abertura inserida no banco de dados com sucesso')
    except Error as erro:
        print("Falha ao inserir dados de abertura: {}".format(erro))
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
            print("Conexão encerrada com sucesso")