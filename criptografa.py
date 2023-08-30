key = 20
result = ''
frase = "uma frase qualquer que foi criada"

for letra in frase:
    if letra.islower():  # Verifica se é uma letra minúscula
        index_letra = ord(letra)
        enc = (index_letra - ord('a') + key) % 26 + ord('a')  # Realiza o deslocamento apenas entre as minúsculas
        result = result + chr(enc)
    else:
        result = result + letra  # Mantém espaços e outros caracteres inalterados

print(result)
