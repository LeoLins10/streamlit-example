import streamlit as st

# Dicionário de grupos e suas características
grupos = {
    "Grupo A - Idealista": ["Abrimos mão do material para entender nossos valores", "Ainda acreditamos que é possível viver no paraíso", "Buscamos a paz e tranquilidade agora"],
    "Grupo B - Caminhante": ["Não pertencemos a ninguém nem a lugar algum", "Gostamos de explorar experiências", "Estamos sempre em movimento"],
    "Grupo C - Sapiente": ["Buscamos experiências que nos fazem crescer", "Acreditamos que a felicidade é resultado da educação", "Buscamos aprendizado e sabedoria"],
    "Grupo D - Valente": ["Somos competitivos e competentes", "Queremos fazer do mundo um lugar melhor", "Somos corajosos e cheios de energia"],
    "Grupo E - Rebelde": ["Desobediência é a nossa estratégia para a mudança", "Violamos leis e normas em benefício do bem-estar alheio", "Quebramos regras por aventura"],
    "Grupo F - Alquimista": ["Transformamos sonhos em realidade", "Gostamos de rituais, momentos simbólicos", "Trazemos magia e encantamento para a vida"],
    "Grupo G - Habitante": ["Exaltamos as virtudes de ser comum", "Acreditamos que coisas e momentos bons é um direito de todos", "Acreditamos que todos são importantes, exatamente como são"],
    "Grupo H - Entusiasta": ["Buscamos a satisfação dos desejos pessoais", "Valorizamos todos os tipos de amor", "Desenvolvemos habilidades emocionais"],
    "Grupo I - Comediante": ["Somos a vida da festa", "Sabemos que é possível ser você mesmo e aceito pelos outros", "Somos brincalhões e espontâneos"],
    "Grupo J - Altruísta": ["Somos altruístas, movidos por compaixão e generosidade", "Nos sacrificamos pelos outros", "Estamos mais preocupados com o bem-estar alheio do que com o nosso"],
    "Grupo K - Artista": ["Autenticidade e curiosidade são a base da alma", "Temos espírito empreendedor, inconformado", "Gostamos de nos expressar em formas materiais"],
    "Grupo L - Regente": ["Temos como objetivo tornar a vida estável e previsível", "Temos tudo sob controle", "Assumimos a liderança, somos responsáveis"]
}

# Dicionário de polos
polos = {
    "Polo Singularidade": ["Grupo D - Valente", "Grupo F - Alquimista", "Grupo K - Artista"],
    "Polo Liberdade": ["Grupo B - Caminhante", "Grupo E - Rebelde", "Grupo I - Comediante"],
    "Polo Coletividade": ["Grupo G - Habitante", "Grupo H - Entusiasta", "Grupo J - Altruísta"],
    "Polo Regularidade": ["Grupo A - Idealista", "Grupo C - Sapiente", "Grupo L - Regente"]
}

# Função para fazer uma pergunta e obter a resposta do usuário
def fazer_pergunta(pergunta):
    while True:
        resposta = input(pergunta + " (Sim/Não): ").strip().lower()
        if resposta in ["sim", "não"]:
            return resposta
        else:
            print("Por favor, responda com 'Sim' ou 'Não'.")

# Função para calcular o polo com base nas respostas
def calcular_polo(respostas):
    contador_polos = {"Polo Singularidade": 0, "Polo Liberdade": 0, "Polo Coletividade": 0, "Polo Regularidade": 0}
    for grupo, perguntas in grupos.items():
        for pergunta in perguntas:
            resposta = fazer_pergunta(f"Você concorda com a afirmação: {pergunta}")
            if resposta == "sim":
                for polo, grupos_polo in polos.items():
                    if grupo in grupos_polo:
                        contador_polos[polo] += 1

    polo_final = max(contador_polos, key=contador_polos.get)
    return polo_final

# Perguntas e respostas
polo_resultante = calcular_polo(polos)

# Exibir o resultado final
print("\nVocê se encaixa no", polo_resultante)

