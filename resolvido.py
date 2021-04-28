def cria_baralho():
    lista = []
    espadas = '♠'
    i=2
    lista.append('A{}'.format(espadas))
    while i<=10:
        lista.append('{}''{}'.format(i,espadas))
        i+=1
    lista.append('J{}'.format(espadas))
    lista.append('Q{}'.format(espadas))
    lista.append('K{}'.format(espadas))
    copas = '♥'
    j=2
    lista.append('A{}'.format(copas))
    while j<=10:
        lista.append('{}''{}'.format(j,copas))
        j+=1
    lista.append('J{}'.format(copas))
    lista.append('Q{}'.format(copas))
    lista.append('K{}'.format(copas))
    ouros = '♦'
    k=2
    lista.append('A{}'.format(ouros))
    while k<=10:
        lista.append('{}''{}'.format(k,ouros))
        k+=1
    lista.append('J{}'.format(ouros))
    lista.append('Q{}'.format(ouros))
    lista.append('K{}'.format(ouros))
    paus = '♣'
    m=2
    lista.append('A{}'.format(paus))
    while m<=10:
        lista.append('{}''{}'.format(m,paus))
        m+=1
    lista.append('J{}'.format(paus))
    lista.append('Q{}'.format(paus))
    lista.append('K{}'.format(paus))
    return lista
#///////
def extrai_naipe(carta):
    if carta[1] == '0':
        naipe = carta[2]
    
    if carta[1] != '0':
        naipe = carta[1]
    
    return (naipe)
#///////
def extrai_valor(carta):
    if carta[1] == '0':
        valor = '10'
    else:
        valor = carta[0]
    return valor
#//////
def lista_movimentos_possiveis(lista,i):
    lista_result = []
    if i > 0:
        if (extrai_naipe(lista[i]) == extrai_naipe(lista[i-1])) or extrai_valor(lista[i]) == extrai_valor(lista[i-1]):
            lista_result.append(1)
    if i>2:
        if (extrai_naipe(lista[i]) == extrai_naipe(lista[i-3])) or extrai_valor(lista[i]) == extrai_valor(lista[i-3]):
            lista_result.append(3)
    return lista_result
#///////
def empilha(lista,ori,des):
    valor = lista[ori]
    lista.remove(valor)
    lista[des] = valor
    return lista
#//////
def possui_movimentos_possiveis(baralho):
    cartasmov = []
    j = 0
    while j<len(baralho):
        if (lista_movimentos_possiveis(baralho,j)) != []:
            cartasmov.append(baralho[j])
        j+=1
    if cartasmov == []:
        return False
    if cartasmov != []:
        return True
#//////

input('vamos jogar?')
import random
ordenadas = cria_baralho()
random.shuffle(ordenadas)

ponto = '.  '
espaço = ' '
k = 0
while k<len(ordenadas):
    if k<10:
        string = '0'+str(k+1)+ponto +ordenadas[k] 
    else:
        string = str(k+1)+ponto +ordenadas[k]
    
    print(string)
    k+=1


if possui_movimentos_possiveis(ordenadas):
    escolha = int(input('Escolha uma carta (digite um numero entre 1 e {0})'.format(len(ordenadas))))

indice = (escolha - 1)

if len(lista_movimentos_possiveis(ordenadas,indice)) == 2:
    print ('Sobre qual carta gostaria de empilhar o {}'.format(ordenadas[indice]))
    print (('1. {}'.format(ordenadas[indice-1])))
    print (('2. {}'.format(ordenadas[indice-3])))
    resp = 0
    while resp != 1 and resp!=2:
        resp = input('Escolha uma carta. digite um número entre 1 e {}'.format(len(ordenadas)))
