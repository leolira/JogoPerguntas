#Sistema de perguntas
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções':['1','3','4','5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções':['25','55','10','51'],
        'Resposta':'25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4','5','2','1'],
        'Resposta':'5'
    },
]

acertos = 0

for pergunta in perguntas:
    
    print(pergunta['Pergunta'])
    for indice, questao in enumerate(pergunta['Opções']):
        print(f"{indice}) {questao}")
    resposta = input('Escolha uma opção:')
    if pergunta['Resposta'] == pergunta['Opções'][int(resposta)]:
        print(f"Acertou!\U0001F44D \n")
        acertos = acertos+1 
    else:
        print(f"Errou!\U0000274C \n")
       
print(f"Você acertou {acertos} de {len(perguntas)} perguntas.")
