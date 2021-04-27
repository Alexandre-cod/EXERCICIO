def cria_baralho():
    lista = []
    
    i=2
    lista.append('A{}'.format(espadas))
    while i<=10:
        espadas = '♠'
        lista.append('{}''{}'.format(i,espadas))
        i+=1
    lista.append('J{}'.format(espadas))
    lista.append('Q{}'.format(espadas))
    lista.append('K{}'.format(espadas))
    
