para rodar esta aplicação local, primeiro deve se ter o python instalado;

Após instalar o python que provavel de estar na versão 3.9.6

usa se o comando 
--pip install virtualenv

Vá para a pasta que terá o a API pelo cmd e utilize o comando 
--virtualelv (nome qualquer de arquivo, eu uso ven);

após isso deve-se ativar este ambiente virtual para isolar as dependencias, vá até a 
--pasta_criada\Scripts\activate

(ven) C:\Users\Cliente\Desktop\hackton> 
No meu caso fica entre colchetes desta forma, no arquivo inicial tem um documento requirements.txt

pelo cmd e com o ambiente virtual ativado se usara o comando 
--pip install -r requirements.txt

entrar na pasta models e rodar o comando:
--python models.py

mover o banco em arquivo criado para a pasta geral;

após isso voltar para a pasta geral

logo após pode se rodar o comando python app.py:

O servidor vai estar funcionando;

para iniciar o banco tem que entrar e rodar o models.py semelhante a forma como se abre o serviço;

Este teste.HTML é o modelo de como tem que chamar o forms para enviar a requisição no momento é só a imagem

#conectar com postgres
<!-- # engine = create_engine(
#     "postgresql+pg8000://scott:tiger@localhost/test",
#     execution_options={
#         "isolation_level": "REPEATABLE READ"
#     }
# )
# 
# SEGUE O MODELO DE OCMO TEM QUE SER COMPLETADO AS INFORMAÇÕES
# engine = create_engine("postgresql://(Usuarioaseusar):(senha)@localhost/(nome do banco)")
 -->

-------------------------------------------
ROTA PARA O ADMIN CREATE localhost://5000/admin

Formato Json 
ele vai criar com estes parametros, exemplo de como mandar para o back-end
{
    "name": "Pedro Henrique Silva Marçal",
    "email": "pedro.h.silva.marcal@gmail.com",
    "password": "TESTE"
}

ROTA PARA O CITIZEN POST/GET, GET/DELETE/PUT localhost://5000/citizen/
envia da seguinte maneira 
{
    "fullname": "Pedro Henrique Silva Marçal",
    "email": "pedro.h.silva.marcal361@gmail.com",
    "password": "Why",
    "cpf": "11122233344",
    "whatsapp": "16993933505"
}

ROTA PARA OS STATUS POST/GET, GET/DELETE (Parametros) localhost://status/
{
    "description": "Registro Numero da Ocorrencia"
}

ROTA PARA O PROBLEM TYPES POST/GET, GET/DELETE (Parametros) localhost://problem/

{
    "description": "Registro Numero da Ocorrencia"
}
Obs: semelhante ao de cima

ROTA PARA O OCURRENCE POST/GET, GET/DELETE/PUT (Parametros) localhost://occurrence/

{
    "date": "2021/03/01", 
    "obs": "varia do caso", 
    "proper": "varia pela ocorrencia", 
    "cellphone": 16993933505, 
    "occurrence_status": 1,
    "admin_id": 1,
    "occurrenceType": 1
}

Obs: semelhante ao de cima
