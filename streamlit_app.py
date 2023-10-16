import streamlit as st

# Banco de dados de grupos e afirmações
grupos = {
    'Grupo A'  - 'Idealista': [
        "Abrimos mão do material para entender nossos valores",
        "Ainda acreditamos que é possível viver no paraíso",
        "Buscamos a paz e tranquilidade agora",
        "Não negamos nada a ninguém e incentivamos a liberdade",
        "Gostamos de confiança",
        "Somos satisfeitos pela beleza e as maravilhas da vida"
    ],
    'Grupo B' - 'Caminhante': [
        "Não pertencemos a ninguém nem a lugar algum",
        "Gostamos de explorar experiências",
        "Vivemos em busca do melhor",
        "Gostamos de novidades",
        "Estamos sempre em movimento",
        "Somos Independentes e curiosos",
        "Somos inconformados e incansáveis",
        "Buscamos nossa própria espécie"
    ],
    'Grupo C - Sapiente': [
        "Buscamos experiências que nos faça crescer",
        "Entendemos que liberdade depende de escolhas certas e consciência",
        "Ajudamos a alcançar prosperidade através da liberdade",
        "Precisamos de informações para tomar decisões",
        "Acreditamos que a felicidade é resultado da educação",
        "Buscamos aprendizado e sabedoria"
    ],
    'Grupo D' - 'Valente': [
        "Também somos vistos como guerreiros",
        "Somos competitivos e competentes",
        "Protegemos valores e ideais",
        "Queremos fazer do mundo um lugar melhor",
        "Somos corajosos e cheios de energia",
        "Somos disciplinados, focados e determinados",
        "Nos arriscamos para defender o mal contra a sociedade"
    ],
    'Grupo E' - 'Rebelde': [
        "Somos uma força disruptiva",
        "Desobediência é a nossa estratégia para a mudança",
        "Estamos sempre prontos para uma revolução",
        "Violamos leis e normas em benefício do bem-estar alheio",
        "Somos o fruto proibido",
        "Encontramos nossos valores fora do status quo",
        "Também somos vistos como rebeldes, iconoclastas",
        "Quebramos regras por aventura"
    ],
    'Grupo F' - 'Alquimista': [
        "Transformamos sonhos em realidade",
        "Buscamos as leis fundamentais do universo",
        "Também somos vistos como shamans, bruxos, alquimistas, cientistas",
        "Gostamos de rituais, momentos simbólicos",
        "Trazemos magia e encantamento para a vida",
        "Somos catalisadores de transformação",
        "Gostamos do exótico, do antigo, do misterioso"
    ],
    'Grupo G' - 'Habitante': [
        "Exaltamos as virtudes de ser comum",
        "Todos têm direitos, assim como nós e você",
        "Nos esforçamos apenas o suficiente para pertencer a um grupo",
        "Acreditamos que coisas e momentos bons é um direito de todos",
        "Queremos participar, através da empatia e do realismo",
        "Entendemos que o fundamento da democracia é o indivíduo",
        "Acreditamos que todos são importantes, exatamente como são"
    ],
    'Grupo H' - 'Entusiasta': [
        "Buscamos a satisfação dos desejos pessoais",
        "Valorizamos todos os tipos de amor",
        "Ajudamos a tornar desejável, atraente",
        "Despertamos desejo, sensualidade, erotismo",
        "Evocamos beleza, romantismo",
        "Incentivamos o desenvolvimento de gênero sexual",
        "Gostamos de uma relação profunda com o que amamos",
        "Desenvolvemos habilidades emocionais"
    ],
    'Grupo I' - 'Comediante': [
        "Também somos vistos como comediantes, palhaços, travessos",
        "Somos a vida da festa",
        "Ajudamos a lidar com os absurdos do mundo moderno",
        "Sabemos que é possível ser você mesmo e aceito pelos outros",
        "Gostamos de nos divertir uns com os outros",
        "Vivemos o momento sem se importar com o que os outros pensam",
        "Pensamos fora da caixa",
        "Sabemos que todos estão sedentos por mais diversão",
        "Somos brincalhões e espontâneos"
    ],
    'Grupo J' - 'Altruísta': [
        "Somos altruístas, movidos por compaixão e generosidade",
        "Nos identificamos com sentimentos maternais e paternais",
        "Temos consciência sobre a vulnerabilidade do ser humano",
        "Somos provedor, o sentido da vida é servir os outros",
        "Nos sacrificamos pelos outros",
        "Estamos mais preocupados com o bem estar alheio do que com o nosso",
        "Antecipamos as necessidades das pessoas"
    ],
    'Grupo K' - 'Artista': [
        "Autenticidade e curiosidade são a base da alma",
        "Adoramos o processo de descontruir e reconstruir",
        "Somos sonhadores, buscamos a imortalidade através das nossas criações",
        "Temos espírito empreendedor, inconformado",
        "Temos mente e coração abertos",
        "Nos empenhamos na criação de cultura, inovação, visão e valores",
        "Gostamos de nos expressar em formas materiais",
        "Estruturamos experiência em uma obra de arte",
        "Criamos coisas com valores atemporais"
    ],
    'Grupo L' - 'Regente': [
        "Temos como objetivo tornar a vida estável e previsível",
        "Acreditamos que as coisas precisam ser duráveis",
        "Organizamos estruturas para entregar qualidade",
        "Temos tudo sob controle",
        "Sabemos que eficiência existe quando cada um cumpre o seu papel",
        "Assumimos o controle das situações",
        "Nos preocupamos com imagem pessoal, status e prestígio",
        "Reforçamos a ordem através de políticas, costumes e hábitos",
        "Assumimos a liderança, somos responsáveis"
    ]
}

# Função para calcular a correspondência com os polos
def calcular_correspondencia(respostas):
    polos = {
        'Singularidade': ['Grupo D', 'Grupo F', 'Grupo K'],
        'Liberdade': ['Grupo B', 'Grupo E', 'Grupo I'],
        'Coletividade': ['Grupo G', 'Grupo H', 'Grupo J'],
        'Regularidade': ['Grupo A', 'Grupo C', 'Grupo L']
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
    st.subheader("Resultado da correspondência com os polos:")
    for polo, pontos in pontos_por_polo.items():
        porcentagem = (pontos / len(respostas)) * 100
        st.write(f"{polo}: {porcentagem:.2f}%")
    
    st.write(f"Grupo com mais afirmações escolhidas: {grupo_mais_escolhido}")

# Título do aplicativo
st.title("Questionário Interativo")

# Pergunte ao usuário
respostas = {}

for grupo, afirmações in grupos.items():
    respostas_grupo = []
    
    for afirmação in afirmações:
        resposta = st.checkbox(afirmação)
        if resposta:
            respostas_grupo.append(afirmação)
    
    if respostas_grupo:
        respostas[grupo] = respostas_grupo

# Calcule a correspondência e exiba os resultados
pontos_por_polo, grupo_mais_escolhido = calcular_correspondencia(respostas)
exibir_resultados(pontos_por_polo, grupo_mais_escolhido)
