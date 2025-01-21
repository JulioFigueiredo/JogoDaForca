def game(palavra): 
    tam_palavra = len(palavra)
    espacos = list('_' * tam_palavra)
    tentativas = 6

    print('Bem vindo ao jogo da forca! \nAdivinhe a palavra abaixo:')
    
    while tentativas > 0:
        print(' '.join(espacos))
        escolha = input('Digite uma letra: ')
        
        if escolha in palavra:
            for i in range(tam_palavra):
                if palavra[i] == escolha:
                    espacos[i] = escolha
            print(' '.join(espacos))
            
            if '_' not in espacos: 
                print('Parabéns, você venceu!')
                return  
        else:
            tentativas -= 1
            print('Erro!')

        if tentativas <= 4:
            tentativa_final = input('Já sabe a palavra? S/N: ').upper()
            if tentativa_final == 'S':
                resposta = input('Digite a palavra final: ')
                if resposta == palavra:
                    print('Você venceu!')
                    return
                else:
                    print('Você perdeu!')
                    return
        
        print(f'Tentativas restantes: {tentativas}')
    
    print('Suas tentativas acabaram! Você perdeu.')

game('teste')
