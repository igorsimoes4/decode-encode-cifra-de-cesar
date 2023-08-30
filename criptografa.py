key = 20
result = ''
frase = "uma frase qualquer que foi criada"

for bola in frase:
    if bola.islower():  # Verifica se é uma letra minúscula
        urubu = ord(bola)
        enc = (urubu - ord('a') + key) % 26 + ord('a')  # Realiza o deslocamento apenas entre as minúsculas
        result = result + chr(enc)
    else:
        result = result + bola  # Mantém espaços e outros caracteres inalterados

print(result)
