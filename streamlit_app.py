# Banco de dados de grupos e afirmações
grupos = {
    'A - Idealista': [
        "Abrimos mão do material para entender nossos valores",
        "Ainda acreditamos que é possível viver no paraíso",
        # Adicione as outras afirmações do Grupo A aqui
    ],
    'B - Caminhante': [
        "Não pertencemos a ninguém nem a lugar algum",
        "Gostamos de explorar experiências",
        # Adicione as outras afirmações do Grupo B aqui
    ],
    # Adicione outros grupos aqui
}

# Função para calcular a correspondência com os polos
def calcular_correspondencia(respostas):
    polos = {
        'Singularidade': ['D', 'F', 'K'],
        'Liberdade': ['B', 'E', 'I'],
        'Coletividade': ['G', 'H', 'J'],
        'Regularidade': ['A', 'C', 'L']
    }
    
    pontos_por_polo = {polo: 0 for polo in polos}
    grupo_mais_escolhido = None
    maior_contagem = 0
    
    for grupo, respostas_grupo in respostas.items():
        for resposta in respostas_grupo:
            for polo, grupos_polo in polos.items():
                if grupo[0] in grupos_polo:
                    pontos_por_polo[polo] += 1
                    if pontos_por_polo[polo] > maior_contagem:
                        maior_contagem = pontos_por_polo[polo]
                        grupo_mais_escolhido = polo

    return pontos_por_polo, grupo_mais_escolhido

# Função para exibir resultados
def exibir_resultados(pontos_por_polo, grupo_mais_escolhido):
    print("Resultado da correspondência com os polos:")
    for polo, pontos in pontos_por_polo.items():
        porcentagem = (pontos / len(grupos)) * 100
        print(f"{polo}: {porcentagem:.2f}%")
    
    print(f"Grupo com mais afirmações escolhidas: {grupo_mais_escolhido}")

# Pergunte ao usuário
respostas = {}

for grupo, afirmações in grupos.items():
    print(f"\n{grupo}")
    respostas_grupo = []
    
    for afirmação in afirmações:
        resposta = input(f"Você se identifica com a afirmação: '{afirmação}'? (S/N): ").strip().lower()
        if resposta == 's':
            respostas_grupo.append(afirmação)
    
    respostas[grupo] = respostas_grupo

# Calcule a correspondência e exiba os resultados
pontos_por_polo, grupo_mais_escolhido = calcular_correspondencia(respostas)
exibir_resultados(pontos_por_polo, grupo_mais_escolhido)
