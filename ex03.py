# faça um programa que leia dois valores inteiros e mostre o resultado na tela
n1 = int(input('\nDigite um valor inteiro: '))
n2 = int(input('Digite um valor inteiro: '))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2

print('\nRESULTADOS')
print('Os números digitados foram: {} e {}'.format(n1, n2))
print('Soma:{}'.format(soma))
print('Subtração:{}'.format(sub))
print('Multiplica:{}'.format(mult))
print('Divisão:{}\n'.format(div))
