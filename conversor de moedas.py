real = float(input('Quanto de dinheiro eu tenho na carteira? R$'))
dolar = real / 5.49
euro = real / 6.36
print('Com R${} , se compra US${:.2f} dolares, e se compra {:.2f} euros'.format(real, dolar,euro))

