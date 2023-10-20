import mysql.connector
import os
from mysql.connector import errorcode
from mysql.connector import IntegrityError
from datetime import datetime
from openpyxl import Workbook

try:   
    db_connection = mysql.connector.connect(host= os.getenv('MYSQL_HOST'), user=os.getenv('MYSQL_USR'),
                                            password=os.getenv('MYSQL_PWD'), database=os.getenv('MYSQL_DB'),
                                            port=os.getenv('MYSQL_PORT'))
    print('Database acessado!')

except mysql.connector.Error as error:
	
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database doesn't exist")
	elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("User name or password is wrong")
	else:
		print(error)

workbook = Workbook()
planilha = workbook.active
planilha['A1'] = 'processo'
planilha['B1'] = 'erro'
contador = 2

if __name__ == "__main__":
    with open('C:\\Users\\gabriel.nicacio\\Downloads\\BASE_BANCO_SQL_19_10.csv', 'r', errors='ignore') as f:
        linha = 0
        while True:
        
            registro = f.readline()

            partes2 = registro.split('¬')
            partes = ['NULL' if valor == "" else valor for valor in partes2]
            if not registro:
                break

            if linha != 0 and linha >= 18000:
                

                #Retira a separação
                if partes[37] == "\n":
                    partes[37] = partes[37].replace("\n","NULL")
                else:
                    partes[37] = partes[37].replace("\n","")
                     
                
                partes[5] = partes[5].replace("'","")
                partes[33] = partes[33].replace("í","")
                partes[2] = partes[2].replace("\'","").replace("'","")

                #retira sifrão
                partes[6] = partes[6].replace("R$ ","").replace(".","").replace(",",".")
                partes[7] = partes[7].replace("R$ ","").replace(".","").replace(",",".")
                partes[8] = partes[8].replace("R$ ","").replace(".","").replace(",",".")
                partes[30] = partes[30].replace("R$ ","").replace(".","").replace(",",".")
                partes[31] = partes[31].replace("R$ ","").replace(".","").replace(",",".")
                partes[32] = partes[32].replace("R$ ","").replace(".","").replace(",",".")
                partes[33] = partes[33].replace("R$ ","").replace(".","").replace(",",".")
            
                #Retira as horas
                data_oficio = partes[13].split(' ',1)
                ultima_hora_user = partes[23].split(' ',1)
                ultima_hora_adm = partes[24].split(' ',1)
                data_cessao = partes[28].split(' ',1)
                data_intencao = partes[27].split(' ',1)
                data_criacao = partes[37].split(' ',1)

                #ajuste de data
                if partes[12] != 'NULL':
                    partes[12] = partes[12].replace("/","-")
                    partes[12] = datetime.strptime(partes[12], "%d-%m-%Y")
                    data_base = partes[12].strftime("%Y-%m-%d")
                    data_base = data_base.replace("-","")
                else:
                    data_base = 'NULL'
                
                if data_oficio[0] != 'NULL':
                    data_oficio[0] = data_oficio[0].replace("/","-")
                    data_oficio[0] = datetime.strptime(data_oficio[0], "%d-%m-%Y")
                    data_oficio_c = data_oficio[0].strftime("%Y-%m-%d")
                    data_oficio_c = data_oficio_c.replace("-","")
                else:
                    data_oficio_c = 'NULL'
                    
                if partes[16] != 'NULL':
                    partes[16] = partes[16].replace("/","-")
                    partes[16] = datetime.strptime(partes[16], "%d-%m-%Y")
                    data_caderno = partes[16].strftime("%Y-%m-%d")
                    data_caderno = data_caderno.replace("-","")
                else:
                     data_caderno = 'NULL'

                if ultima_hora_user[0] != 'NULL':
                    ultima_hora_user[0] = ultima_hora_user[0].replace("/","-")
                    ultima_hora_user[0] = datetime.strptime(ultima_hora_user[0], "%d-%m-%Y")
                    ultima_hora_user_c = ultima_hora_user[0].strftime("%Y-%m-%d")
                    ultima_hora_user_c = ultima_hora_user_c.replace("-","")
                else:
                    ultima_hora_user_c = 'NULL'

                if ultima_hora_adm[0] != 'NULL':
                    ultima_hora_adm[0] = ultima_hora_adm[0].replace("/","-")
                    ultima_hora_adm[0] = datetime.strptime(ultima_hora_adm[0], "%d-%m-%Y")
                    ultima_hora_adm_c = ultima_hora_adm[0].strftime("%Y-%m-%d")
                    ultima_hora_adm_c = ultima_hora_adm_c.replace("-","")
                else:
                    ultima_hora_adm_c = 'NULL'

                if data_intencao[0] != 'NULL':
                    data_intencao[0] = data_intencao[0].replace("/","-")
                    data_intencao[0] = datetime.strptime(data_intencao[0], "%d-%m-%Y")
                    data_intencao_c = data_intencao[0].strftime("%Y-%m-%d")
                    data_intencao_c = data_intencao_c.replace("-","")
                else:
                    data_intencao_c = 'NULL'
                
                if data_cessao[0] != 'NULL':
                    data_cessao[0] = data_cessao[0].replace("/","-")
                    data_cessao[0] = datetime.strptime(data_cessao[0], "%d-%m-%Y")
                    data_cessao_c = data_cessao[0].strftime("%Y-%m-%d")
                    data_cessao_c = data_cessao_c.replace("-","")
                else:
                    data_cessao_c = 'NULL'

                if partes[29] != 'NULL':
                    partes[29] = partes[29].replace("/","-")
                    partes[29] = datetime.strptime(partes[29], "%d-%m-%Y")
                    data_credito = partes[29].strftime("%Y-%m-%d")
                    data_credito = data_credito.replace("-","")
                else: 
                    data_credito = 'NULL'

                if partes[36] != 'NULL':
                    partes[36] = partes[36].replace("/","-")
                    partes[36] = datetime.strptime(partes[36], "%d-%m-%Y")
                    data_parecer = partes[36].strftime("%Y-%m-%d")
                    data_parecer = data_parecer.replace("-","")
                else:
                    data_parecer = 'NULL'
                
                data_criacao[0] = data_criacao[0].replace("/","-")
                data_criacao[0] = datetime.strptime(data_criacao[0], "%d-%m-%Y")
                data_criacao_c = data_criacao[0].strftime("%Y-%m-%d")
                data_criacao_c = data_criacao_c.replace("-","")

                partes[11] = partes[11].replace("'","")
                partes[2] = partes[2].replace("'","")

                sql = "insert into oportunidades (id_registro,id_robo,credor,idade,cidade,processo,liquido,juros,somatoria,tipo,vara,advogado_patrono,data_base,data_oficio,ordem_cronologica,orgao_devedor,data_caderno,caderno,layout,fluxo,estagio,agente,coordenador,ultima_atividade_user,ultima_atividade_adm,advogado_dd,advogado_parecer,data_intecao,data_cessao,data_credito,valor_cedivel,valor_pago_credor,valor_venda,motivo_negativa_dd,motivo_negativa_parecer,motivo_desistencia,data_parecer,data_criacao)"\
                f"Values('{partes[0]}','{partes[1]}','{partes[2]}','{partes[3]}','{partes[4]}','{partes[5]}',{partes[6]},{partes[7]},{partes[8]},'{partes[9]}','{partes[10]}','{partes[11]}',{data_base},{data_oficio_c},'{partes[14]}','{partes[15]}',{data_caderno},'{partes[17]}','{partes[18]}','{partes[19]}','{partes[20]}','{partes[21]}','{partes[22]}',{ultima_hora_user_c},{ultima_hora_adm_c},'{partes[25]}','{partes[26]}',{data_intencao_c},{data_cessao_c},{data_credito},{partes[30]},{partes[31]},{partes[32]},{partes[33]},'{partes[34]}','{partes[35]}',{data_parecer},{data_criacao_c})"
                
                cursor = db_connection.cursor()
                try:

                    cursor.execute(sql)
                    db_connection.commit()
                    print(f"{linha} - ADICIONADO")

                except IntegrityError as erro:

                    if "Duplicate entry" in str(erro):

                        
                        sql_up = f"update oportunidades set id_robo='{partes[1]}', credor='{partes[2]}', idade='{partes[3]}', cidade='{partes[4]}', processo='{partes[5]}', liquido={partes[6]}, juros={partes[7]}, somatoria={partes[8]},	tipo='{partes[9]}',	vara='{partes[10]}', advogado_patrono='{partes[11]}', data_base={data_base}, data_oficio={data_oficio_c}, ordem_cronologica='{partes[14]}', orgao_devedor='{partes[15]}', data_caderno={data_caderno}, caderno='{partes[17]}',	layout='{partes[18]}', fluxo='{partes[19]}', estagio='{partes[20]}', agente='{partes[21]}', coordenador='{partes[22]}',	ultima_atividade_user={ultima_hora_user_c},	ultima_atividade_adm={ultima_hora_adm_c}, advogado_dd='{partes[25]}', advogado_parecer='{partes[26]}', data_intecao={data_intencao_c}, data_cessao={data_cessao_c}, data_credito={data_credito}, valor_cedivel={partes[30]}, valor_pago_credor={partes[31]}, valor_venda={partes[32]},	motivo_negativa_dd={partes[33]}, motivo_negativa_parecer='{partes[34]}', motivo_desistencia='{partes[35]}', data_parecer={data_parecer}, data_criacao={data_criacao_c} where id_registro = '{partes[0]}'"
                    
                        try:

                            cursor.execute(sql_up)
                            db_connection.commit()
                            print(f"{linha} - ATUALIZADO")

                        except Exception as erro_final:
                            pass
                            print(f'{linha} - ERRO')
                            
                            descricao = f"o erro é {erro_final}"
                            planilha[f'A{contador}'] = partes[0]
                            planilha[f'B{contador}'] = descricao
                            contador += 1


                    else:
                        print('ERRO INESPERADO')
                except Exception as erro_final:
                    pass
                    print(f'{linha} - ERRO')
                    
                    descricao = f"o erro é {erro_final}"
                    planilha[f'A{contador}'] = partes[0]
                    planilha[f'B{contador}'] = descricao
                    contador += 1
                    
            linha += 1
            
workbook.save("erro_importacao.xlsx")
del db_connection