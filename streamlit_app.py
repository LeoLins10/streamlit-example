```python
# Crie uma matriz de correspondência com as perguntas, opções de resposta e atributos de marca correspondentes
correspondencia = [
    {"pergunta": "Qual dessas palavras melhor descreve a abordagem da sua marca em relação à aventura?",
     "opcoes": ["Aventureira", "Conservadora", "Criativa", "Responsável"],
     "atributo": "Aventureira"},
    {"pergunta": "Qual dessas palavras melhor descreve a personalidade da sua marca em relação à liderança?",
     "opcoes": ["Animados", "Confiáveis", "Inspirados", "Seguros"],
     "atributo": "Inspiradora"},
    {"pergunta": "Qual dessas palavras melhor descreve a abordagem da sua marca em relação à inovação?",
     "opcoes": ["Inovação", "Qualidade", "Sustentabilidade", "Tradição"],
     "atributo": "Inovadora"},
    {"pergunta": "Qual dessas palavras melhor descreve a personalidade da sua marca em relação à colaboração?",
     "opcoes": ["Colaborativa", "Direta", "Empática", "Objetiva"],
     "atributo": "Empática"},
    {"pergunta": "Qual dessas palavras melhor descreve a abordagem da sua marca em relação à modernidade?",
     "opcoes": ["Moderna", "Sofisticada", "Tradicional", "Vibrante"],
     "atributo": "Moderna"},
    {"pergunta": "Qual dessas palavras melhor descreve a abordagem da sua marca em relação à competição?",
     "opcoes": ["Competitiva", "Cooperativa", "Inovadora", "Respeitosa"],
     "atributo": "Competitiva"},
    {"pergunta": "Qual dessas palavras melhor descreve a personalidade da sua marca em relação à inspiração?",
     "opcoes": ["Direta", "Divertida", "Inspiradora", "Persuasiva"],
     "atributo": "Inspiradora"},
    {"pergunta": "Qual dessas palavras melhor descreve a abordagem da sua marca em relação à sustentabilidade?",
     "opcoes": ["Ativista", "Consciente", "Generosa", "Sustentável"],
     "atributo": "Sustentável"},
    {"pergunta": "Qual dessas palavras melhor descreve a abordagem da sua marca em relação à disrupção?",
     "opcoes": ["Arrojada", "Conservadora", "Disruptiva", "Tradicional"],
     "atributo": "Disruptiva"},
    {"pergunta": "Qual dessas palavras melhor descreve a personalidade da sua marca em relação ao carisma?",
     "opcoes": ["Ambiciosa", "Carismática", "Forte", "Inspiradora"],
     "atributo": "Carismática"},
    {"pergunta": "Qual dessas palavras melhor descreve a abordagem da sua marca em relação aos detalhes?",
     "opcoes": ["Detalhista", "Inovadora", "Precisa", "Tradicional"],
     "atributo": "Detalhista"},
    {"pergunta": "Qual dessas palavras melhor descreve a abordagem da sua marca em relação à imaginação?",
     "opcoes": ["Imaginativa", "Inovadora", "Moderna", "Tradicional"],
     "atributo": "Imaginativa"},
    {"pergunta": "Qual dessas palavras melhor descreve a abordagem da sua marca em relação à consciência social?",
     "opcoes": ["Consciente", "Inovadora", "Responsável", "Tradicional"],
     "atributo": "Consciente"},
    {"pergunta": "Qual dessas palavras melhor descreve a abordagem da sua marca em relação à confiabilidade?",
     "opcoes": ["Confiável", "Honesto", "Seguro", "
     "atributo": "Confiável"}
]

# Crie um dicionário para armazenar a pontuação de cada atributo de marca
pontuacao = {}
for item in correspondencia:
    pontuacao[item["atributo"]] = 0

# Faça as perguntas ao usuário e atribua pontos aos atributos de marca correspondentes
for item in correspondencia:
    print(item["pergunta"])
    for i, opcao in enumerate(item["opcoes"]):
        print(f"{i+1}. {opcao}")
    resposta = int(input("Escolha uma opção: "))
    atributo = item["atributo"]
    pontuacao[atributo] += resposta

# Determine o atributo de marca com a pontuação mais alta
atributo_mais_alto = max(pontuacao, key=pontuacao.get)
print(f"A personalidade da sua marca é {atributo_mais_alto}")


# Crie uma matriz de correspondência com as perguntas, opções de resposta e atributos de marca correspondentes
correspondencia = [
    {"pergunta": "Qual dessas palavras melhor descreve a abordagem da sua marca em relação à aventura?",
     "opcoes": ["Aventureira", "Conservadora", "Criativa", "Responsável"],
     "atributo": "Aventureira"},
    {"pergunta": "Qual dessas palavras melhor descreve a personalidade da sua marca em relação à liderança?",
     "opcoes": ["Animados", "Confiáveis", "Inspirados", "Seguros"],
     "atributo": "Inspiradora"},
    {"pergunta": "Qual dessas palavras melhor descreve a abordagem da sua marca em relação à inovação?",
     "opcoes": ["Inovação", "Qualidade", "Sustentabilidade", "Tradição"],
     "atributo": "Inovadora"},
    {"pergunta": "Qual dessas palavras melhor descreve a personalidade da sua marca em relação à colaboração?",
     "opcoes": ["Colaborativa", "Direta", "Empática", "Objetiva"],
     "atributo": "Empática"},
    {"pergunta": "Qual dessas palavras melhor descreve a abordagem da sua marca em relação à modernidade?",
     "opcoes": ["Moderna", "Sofisticada", "Tradicional", "Vibrante"],
     "atributo": "Moderna"},
    {"pergunta": "Qual dessas palavras melhor descreve a abordagem da sua marca em relação à competição?",
     "opcoes": ["Competitiva", "Cooperativa", "Inovadora", "Respeitosa"],
     "atributo": "Competitiva"},
    {"pergunta": "Qual dessas palavras melhor descreve a personalidade da sua marca em relação à inspiração?",
     "opcoes": ["Direta", "Divertida", "Inspiradora", "Persuasiva"],
     "atributo": "Inspiradora"},
    {"pergunta": "Qual dessas palavras melhor descreve a abordagem da sua marca em relação à tradição?",
     "opcoes": ["Clássica", "Inovadora", "Luxuosa", "Tradicional"],
     "atributo": "Tradicional"},
    {"pergunta": "Qual dessas palavras melhor descreve a personalidade da sua marca em relação à autenticidade?",
     "opcoes": ["Autêntica", "Criativa", "Elegante", "Simples"],
     "atributo": "Autêntica"},
    {"pergunta": "Qual dessas palavras melhor descreve a abordagem da sua marca em relação à sustentabilidade?",
     "opcoes": ["Comprometida", "Inovadora", "Responsável", "Tradicional"],
     "atributo": "Comprometida"}
]

# Crie um dicionário para armazenar a pontuação de cada atributo de marca e polo arquetípico
pontuacao = {}
for item in correspondencia:
    pontuacao[item["atributo"]] = 0
polos_arquetipicos = ["Herói", "Mago", "Explorador", "Fora da Lei", "Comediante", "Amante", "Rei", "Cuidador"]

# Faça as perguntas ao usuário e atribua pontos aos atributos de marca e polos arquetípicos correspondentes
for item in correspondencia:
    print(item["pergunta"])
    for i, opcao in enumerate(item["opcoes"]):
        print(f"{i+1}. {opcao}")
    resposta = int(input("Escolha uma opção: "))
    atributo = item["atributo"]
    pontuacao[atributo] += resposta

# Determine o atributo de marca com a pontuação mais alta e o polo arquetípico correspondente
atributo_mais_alto = max(pontuacao, key=pontuacao.get)
polo_arquetipico = polos_arquetipicos[pontuacao[atributo_mais_alto] % len(polos_arquetipicos)]
print(f"A personalidade da sua marca é {atributo_mais_alto} e o polo arquetípico é {polo_arquetipico}")
```
