import random
import sqlite3

conec = sqlite3.connect('db_customer_account.db')

data = conec.cursor()


# SQL

# função criar a tabela
def create_table():
    data.execute("CREATE TABLE IF NOT EXISTS tb_customer_account ("
                 "                                               id_customer  int PRIMARY KEY NOT NULL  , "  # Identificação unica do cliente. 
                 "                                               cpf_cnpj varchar(18) NOT NULL          , "  # CPF ou CNPJ do Cliente 
                 "                                               nm_customer varchar(45) NOT NULL       , "  # Nome do Cliente 
                 "                                               is_active int                          , "  # Indica se o cliente está ativo ou não 
                 "                                               vl_total real                            "  # Mostra quando que o cliente possui de saldo
                 ")")
pass

create_table()

#função inserir dados
def dataEntry(cod, cpf_cnpj, nome, ativ_cliente, saldo):
    data.execute('INSERT INTO tb_customer_account VALUES(?,?,?,?,?)', (cod, cpf_cnpj, nome, ativ_cliente, saldo))

    # escrever os dados no banco de dados
    conec.commit()
pass

#SELECT para exibir media
def selectDataMed():
        for row in data.execute('SELECT AVG(vl_total) FROM tb_customer_account WHERE vl_total > 560 AND id_customer BETWEEN 1500 AND 2700;'):
            print('========================================================\nMedia: ', row[0])

pass


#SELECT para exibir todos os dados filtrados
def selectAllData():
        for row in data.execute('SELECT * FROM tb_customer_account WHERE 560 AND id_customer BETWEEN 1500 AND 2700 ORDER BY vl_total DESC'):
            print('========================================================\n')
            print(row, '\n')
pass

n = int(input('Digite a quantidade de registros para cadastramento: '))
cont = 0

# popular banco
while cont < n:
    # dados
    cod = input('Digite a identificação do cliente: ') #random.randint(1450, 2790)
    cpf_cnpj = input('Digite o CNPJ/CPF: ')
    nome = input('Digite o nome do cliente: ')
    ativ_cliente = input('O cliente está ativo?(1-Sim/2-Não) ')


    saldo= input('Digite o valor do saldo: ')

    dataEntry(cod, cpf_cnpj, nome, ativ_cliente, saldo)
    #contador
    cont = cont + 1


selectDataMed()
selectAllData()

conec.close();

"""
#media
SELECT AVG(vl_total) FROM tb_customer_account WHERE vl_total > 560 AND id_customer BETWEEN 1500 AND 2700;

#lista nomes
SELECT * FROM tb_customer_account WHERE 560 AND id_customer BETWEEN 1500 AND 2700 ORDER BY DESC;
"""
