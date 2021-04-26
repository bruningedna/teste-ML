import email
import imaplib
import urllib.parse
import re
import os
from pathlib import Path

from conexao import inserir

EMAIL = 'edaobruning@gmail.com'
PASSWORD = 'lxiodknedsyetpiu'
SERVER = 'imap.gmail.com'

try:

    # Abrir uma conexão com o servidor do Gmail, fazer login e acessar a pasta desejada "Teste"
    mail = imaplib.IMAP4_SSL(SERVER)
    mail.login(EMAIL, PASSWORD)
    mail.select('Teste')


    # Realizar uma busca na inbox com o critério de busca ALL para pegar todos os emails da inbox
  
    status, data = mail.search(None, 'ALL')

    # Separar os ids numa lista vazia

    mail_ids = []

    for block in data:
        
        mail_ids += block.split()

    # Para cada id de e-mail baixar do Gmail e extrair o conteúdo com o padrão RFC
    
    for i in mail_ids:

        status, data = mail.fetch(i, '(RFC822)')
        

        for response_part in data:

            if isinstance(response_part, tuple):

                message = email.message_from_bytes(response_part[1])

    # Com o resultado, é possível tirar as informações de quem enviou o e-mail, assunto e data

                mail_from = message['from']
                mail_from = mail_from.split("<")[1].rstrip(">")

                mail_subject = message['subject']

                mail_date = message['Date']
                d = mail_date.split()[1]
                m = mail_date.split()[2]
                a = mail_date.split()[3]
                mail_date = f'{d} {m} {a}'
        
                
    # Ajustar texto e extrair o necessário 

                if message.is_multipart():
                    mail_content = ''
                    for part in message.get_payload():
                        if part.get_content_type() == 'text/plain':
                            mail_content += part.get_payload()

                else:
                    mail_content = message.get_payload()
                    

                tipoDeDado = mail_subject

                mensagem = mail_content
                reg = re.compile(r'(devops)', re.IGNORECASE | re.DOTALL)
                res = reg.search(mensagem)
                text = res.group(1)

                mensagemT = mail_subject
                datasT = mail_date
                remetenteT = mail_from
                assuntoT = text

                inserir(datasT, remetenteT, assuntoT, mensagemT)
        
               

                
                    
except Exception as exception:
    print(exception)
