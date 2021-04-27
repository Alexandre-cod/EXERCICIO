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
    while i<=10:
        lista.append('{}''{}'.format(i,copas))
        j+=1
    lista.append('J{}'.format(copas))
    lista.append('Q{}'.format(copas))
    lista.append('K{}'.format(copas))
    
