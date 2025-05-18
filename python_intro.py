print('Hello, Django girls!')
if 3 < 2:
    print('Funciona!')
    
if 5 > 2:
    print('5 é maior que 2')
else:
    print('5 não é maior que 2')
name = 'Sonja'
if name == 'Ola':
    print('Olá Ola!')
elif name == 'Sonja':
    print('Olá Sonja!')
else:
    print('Olá estranho!')


volume = 57
if volume < 20: 
    print("Está um pouco baixo")
elif 20 <= volume < 40: 
    print("Está bom para música ambiente")
elif 40 <= volume < 60: 
    print("Perfeito, posso ouvir todos os detalhes")
elif 60 <= volume < 80: 
    print("Ótimo para festas!")
elif 80 <= volume < 100: 
    print("Está muito alto!")
else: 
    print("Meus ouvidos doem! :(")
    # Mudar o volume se estiver muito alto ou muito baixo
if volume < 20 or volume > 80:
    volume = 50
    print("Bem melhor!")
    def hi():
      print('Olá!')
      print('Tudo bem?')


def hi(name):
    if name == 'Ola':
        print('Olá Ola!')
    elif name == 'Sonja':
        print('Olá Sonja!')
    else:
        print('Olá estranho!')

hi('Carol')
hi("Ola")
hi("Sonja")
hi("Mary")
def hi(name):
    print('Olá ' + name + '!')

hi("Rachel")
girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'você']
for name in girls:
    def hi(name):
        print('Olá ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'você']
for name in girls:
    hi(name)
    print('Próxima')
for i in range(1, 6):
    print(i)