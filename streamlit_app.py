import streamlit as st

# Dicionário de mapeamento de letras para respostas
mapeamento_letras_respostas = {
    'A': "Inocente",
    'B': "Explorador",
    'C': "Sábio",
    'D': "Herói",
    'E': "Fora da Lei",
    'F': "Mago",
    'G': "Cara Comum",
    'H': "Amante",
    'I': "Comediante",
    'J': "Prestativo",
    'K': "Criador",
    'L': "Governante"
}

def main():
    st.title("Questionário de Múltipla Escolha")

    afirmacoes = [
        "Somos satisfeitos pela beleza e as maravilhas da vida (A)",
        "Abrimos mão do material para entender nossos valores (A)",
        "Buscamos a paz e tranquilidade agora (A)",
        # Adicione todas as afirmações aqui
    ]

    respostas = []

    for afirmacao in afirmacoes:
        checkbox = st.checkbox(afirmacao)
        if checkbox:
            letra = afirmacao[-2]
            respostas.append(mapeamento_letras_respostas.get(letra, ""))

    if st.button("Calcular Resposta"):
        resultado = ', '.join(respostas)
        st.write(f"Respostas: {resultado}")

if __name__ == "__main__":
    main()
