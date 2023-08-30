
def quebrar_cifra_cesar(cifra):
    # Definindo o alfabeto minúsculo #
    letras = 'abcdefghijklmnopqrstuvwxyz'
    
    # Loop para testar cada possível deslocamento (de 0 a 25) #
    for deslocamento in range(0, 26):
        texto_decifrado = ''  # Crio a string para armazenar o texto decifrado #
        
        # Loop para percorrer cada caractere na cifra #
        for letra in cifra:
            if letra in letras:  # Verificando se o caractere é uma letra minúscula #
                index = letras.index(letra)  # Obtendo o índice da letra no alfabeto #
                index_decifrado = (index - deslocamento) % 26  # Calculando o índice decifrado #
                letra_decifrada = letras[index_decifrado]  # Obtendo a letra decifrada #
                texto_decifrado += letra_decifrada  # Adicionando a letra decifrada ao texto resultante #
            else:
                texto_decifrado += letra  # Mantendo espaços e outros caracteres inalterados #
        
        # Imprimindo o resultado para o deslocamento atual #
        print(f"Deslocamento {deslocamento}: {texto_decifrado}")
        
        # Perguntando ao usuário se o texto decifrado faz sentido #
        resposta = input("Esse é o texto original? (s/n): ")
        if resposta.lower() == 's':
            print("Texto decifrado:", texto_decifrado)
            break  # Encerrando o loop se o usuário confirmar que o texto está correto #

# Exemplo de uso
cifra = "ogu zlumy koufkoyl koy zic wlcuxu"
quebrar_cifra_cesar(cifra)  # Chamando a função com a cifra dada #
