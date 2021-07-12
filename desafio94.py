fichas = dict()
listaCadastro = list()
somaIdade = 0
media = 0
while True:
    # Limpar o dicionario "fichas"
    fichas.clear()
    fichas['nome'] = str(input('Nome da pessoa? '))
    while True:
        # Perguntando o sexo da pessoa, e caso a pessoa não escolha M (Masculino) ou F (Feminino), se não da a mensagem de erro e volta pro while
	fichas['sexo'] = str(input('Qual seu sexo? (M/F) ')).upper().strip()[0]
        if fichas['sexo'] in 'MF':
            break
        print('Erro! Por favor digite apenas M ou F. ')
    fichas['idade'] = int(input('Qual sua idade? '))
    somaIdade += fichas['idade']
    listaCadastro.append(fichas.copy())
    while True:
        escolha = str(input('Quer continuar? (S/N)')).upper().strip()[0]
        if escolha in 'SN':
            break
        print('Erro! Digite novamente')
    if escolha == 'N':
        break
print(f'Foram cadastradas {len(listaCadastro)} pessoas')
media = somaIdade / len(listaCadastro)
print(f'A media de idade do grupo {media:.2f}')
print('A lista com todas mulheres cadastradas: ', end='')
for p in listaCadastro:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('A lista das pessoas que estão acima da media da idade: ')
for p in listaCadastro:
    if p['idade'] >= media:
        print('         ')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('Fim')
