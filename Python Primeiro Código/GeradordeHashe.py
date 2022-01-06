import hashlib

string = input('Digite o texto a ser gerado a Hash:\n>>>')
print('#' * 20, 'MENU - ESCOLHA O TIPO DE HASH', '#' * 20)
print('[1] - Digite 1 para MD5')
print('[2] - Digite 2 para SHA1')
print('[3] - Digite 3 para SHA256')
print('#' * 71)

menu = int(input('Digite a opção desejada:'))


if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print('O Hash MD5 da String:', string, ' é: ', resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print('O Hash SHA1 da String: ', string,'é: ', resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print('O Hash SHA256 da String: ', string, 'é: ', resultado.hexdigest())
else:
    print('Tente Novamente.....')






