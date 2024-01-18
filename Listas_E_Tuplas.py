# -*- coding: utf-8 -*-
def ex1():
'''1.Crie um Python Script que conte quantas vezes cada nome está presente em uma lista 
[’nome1’, ’nome2’, ...] e armazena essa contagem em um dicionário {’nome1’:xvezes, ’nome2’: yvezes, ....}'''

A=['abacaxi','abacaxi','abacaxi',2,2,2,4,4,5]

print(dict((i, A.count(i)) for i in set (A)))

def ex2():
'''2.Crie um Python Script que realize o mesmo procedimento da questão anterior. No entanto, ao invés do conteúdo da 
lista nomes ser atribuído no próprio script, faça uma estrutura de repetição na qual ela leia uma string do usuário e adicione 
os nomes digitados por ele, um de cada vez, na lista nomes. O término da adição de nomes deve ser indicado quando o usuário 
inserir uma string vazia (”)'''

name = " "

List=[]

while name != None:
    name = (input('Digite um nome para adicionar a lista: '))

    if len(name) > 0:
        List.append(name)
    else:
        name = None

print(List)

def ex3():
"""3.Elabore um algoritmo que leia um número de entrada que indicará a quantidade de registros a serem lidos (N). 
Em seguida algoritmo deve solicitar o nome e idade de N pessoas e ao final apresentar o nome da pessoa mais velha."""

list_tupla= []
Qtd=int(input('Digite a quantidade de registros: '))

for i in range(Qtd):

    name=str(input('Digite o Nome da pessoa: '))
    age=int(input('Digite a idade da pessoa: '))
    tupla=(name,age)
    list_tupla.append(tupla)

    if(i == 0):
         older = list_tupla[i]
    elif(list_tupla[i][1] > older[1]):
        older = list_tupla[i]
    elif(list_tupla[i][1] == older[1]):
        print(older[0], ' e ', list_tupla[i][0], ' tem a mesma idade')

print(older[0], ' é a pessoa mais velha e tem ', older[1], ' anos')

if __name__ == "__main__":
ex1()
ex2()
ex3()