Python é uma linguagem de programação de uso geral conhecida pela simplicidade e pela facilidade de uso.

É usada em ciências de dados, IoT, aprendizado de máquina, desenolvimento web, automação e etc.
Seu uso é vasto, basta apenas ter criatividade e conhecimento. 

Python é amplamente usado em DevOps para escrever scripts de CI/CD e gerenciar infraestrutura em pipelines de desenvolvimento. 
Também é comumente usado para construir serviços de back-end e APIs internas.

Finalmente, uma das maiores forças do Python é a automação. 
Você pode escrever scripts simples para ajudar com tarefas repetitivas como extrair dados de planilhas, 
enviar e-mails e trabalhar com arquivos na sua máquina local.

Finalmente, uma das maiores forças do Python é a automação. 
Você pode escrever scripts simples para ajudar com tarefas repetitivas como extrair dados de planilhas, 
enviar e-mails e trabalhar com arquivos na sua máquina local.

-------------------------------

Como funciona as variáveis? ---- 

Em python você só precisa fazer:

name = "John Doe"
age = 25

Simples assim, ele reconhece o tipo de variável e armazena ali. 

Python reconhece strings e números, importante saber disso. 
Se quer uma string, use '' ou "" para que ele saiba. 

-------------------------------

Strings é uma sequencia de caracteres cercada por aspas simples ou duplas. 
Em algumas linguagens as aspas diferenciam o tipo de dado, mas em python tanto faz o tipo.

- String multilinha assim: """ """ ou ''' '''

- Verificar se algo está em uma string assim: ('X' in my_str) #A saída será True ou False.

- O comando len diz o comprimento da string.

- Concatenar strings usa-se o +. Ex: my_str_1 + ' ' + my_str_2

- Para deixar uma string toda maiúscula usa-se .upper(). Para deixar minúscula > .lower().

-------------------------------

Operadores Lógicos e Condicionais -

Comparadores = Ele vai verificar a comparação entre valores e retonar um booleano implicito ou explicito. 

São eles: 
== igual
!= diferente 
> maior que 
< menor que
>= maior ou igual 
<= menor ou igual

Condicionais = De acordo com condições pré-definidas, ele vai executar ou não códigos. 

- A condição mais básica é o If - Se alguma coisa, então
- Depois ele tem o Else - Se não If, então Else
- O Elif é uma multipla condição entre o If e Else 

Eu posso aninhar vários If's para ir montando um condicional grande. 


-------------------------------

O **`for`** em Python é uma estrutura de repetição usada para percorrer e processar, um a um, os elementos de qualquer sequência ou objeto iterável.

linguagens = ["Python", "JavaScript", "Go"]
for lang in linguagens:
    print(f"Estudando {lang}") 

-------------------------------

O laço while executa um bloco de código enquanto uma condição for verdadeira. 

senha_correta = "python123"
tentativa = ""

while tentativa != senha_correta:
    tentativa = input("Digite a senha: ")

print("Acesso liberado!")

-------------------------------

Funções Def são muito úteis em python. Com elas eu posso criar códigos reutilizáveis no resto do programa

def hello()
    print("Hello World")

hello()

