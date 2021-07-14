para rodar esta aplicação local, primeiro deve se ter o python instalado;

Após instalar o python que provavel de estar na versão 3.9.6

usa se o comando pip install virtualenv

Vá para a pasta que terá o a API pelo cmd e utilize o comando virtualelv (nome qualquer de arquivo, eu uso ven);

após isso deve-se ativar este ambiente virtual para isolar as dependencias, vá até a pasta_criada\Scripts\activate

(ven) C:\Users\Cliente\Desktop\hackton> 
No meu caso fica entre colchetes desta forma, no arquivo inicial tem um documento requirements.txt

pelo cmd e com o ambiente virtual ativado se usara o comando pip install -r requirements.txt

logo após pode se rodar o comando python app.py:

O servidor vai estar funcionando;

para iniciar o banco tem que entrar e rodar o models.py semelhante a forma como se abre o serviço;

Este teste.HTML é o modelo de como tem que chamar o forms para enviar a requisição no momento é só a imagem