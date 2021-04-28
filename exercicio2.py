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



def extrai_naipe(carta):
    if carta[1] == '0':
        naipe = carta[2]
    
    if carta[1] != '0':
        naipe = carta[1]
    
    return (naipe)
    
  

def extrai_valor(carta):
    if carta[1] == '0':
        valor = 10

    if carta[1] != '0':
        valor = carta[0]

    return valor
    
    


