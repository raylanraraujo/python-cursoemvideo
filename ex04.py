algo = input('\nDigite algo: ')

# será exibido na tela o tipo primitivo armazenado na variável bem como 
print(f"\nO tipo primitivo de algo é: {type(algo)}") # para verificar o tipo do valor amazenado pela variável
print(f"Somente espaços? {algo.isspace()}") # para saber se o valor armazenado na variável é apenas espaços em branco
print(f"É numérico? {algo.isnumeric()}") # para saber se o valor armazenado na variável é algo numérico
print(f"É alfabético? {algo.isalpha()}") #para saber se o o valor armazenado na variável é alfabético
print(f"É alfanumérico? {algo.isalnum()}") # para verificar se o valor é alfanumérico
print(f"Está minúscula? {algo.islower()}")
print(f"Está maiúscula? {algo.isupper()}")
print(f"Está capitalizada? {algo.istitle()}") # verificar se está capitalizada, o primeiro caractere em maiúscula e todo o resto minúsculo.
print()

# No código, algo é o nosso objeto e portanto ele tem caracterísitcas e realiza ações, ou seja, atributos e métodos. Todo objeto do tipo string possui os métodos vistos acima.