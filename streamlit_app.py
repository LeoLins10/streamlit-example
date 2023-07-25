import pandas as pd
import streamlit as st

# Definir a tabela de correspondência
correspondencia = {
   "Lógico": [2, 0],
    "Intuitivo": [1, 0],
    "Dedicado": [0, 2],
    "Flexível": [0, 1],
    "Líder": [0, 2],
    "Colaborativo": [1, 0],
    "Criativo": [2, 1],
    "Aventureiro": [1, 0],
    "Planejador": [2, 0],
    "Espontâneo": [1, 0],
    "Comunicativo": [2, 0],
    "Empático": [1, 1],
    "Analítico": [2, 0],
    "Assertivo": [0, 2],
    "Resiliente": [2, 0],
    "Tranquilo": [0, 1],
    "Ambicioso": [2, 0],
    "Equilibrado": [0, 1]
}

# Definir as perguntas e as opções de resposta
perguntas = [
    "Quando se trata de tomar decisões, você é mais:",
    "Como você lida com desafios e adversidades?",
    "Quando se trata de trabalhar em equipe, você é mais:",
    "Quais são suas principais fontes de inspiração?",
    "Como você lida com mudanças e incertezas?",
    "Quando se trata de se comunicar com outras pessoas, você é mais:",
    "Quais são suas principais habilidades?",
    "Como você se relaciona com outras pessoas em seu ambiente pessoal e profissional?",
    "Quando se trata de lidar com o estresse, você é mais:",
    "Quais são suas principais motivações e objetivos na vida?"
]

opcoes = [
     ["Lógico e racional", "Intuitivo e emocional"],
    ["Com determinação e perseverança", "Com flexibilidade e adaptabilidade"],
    ["Líder e assertivo", "Colaborativo e cooperativo"],
    ["Arte e cultura", "Natureza e aventura"],
    ["Com resiliência e inovação", "Com segurança e estabilidade"],
    ["Comunicativo e expressivo", "Empático e compreensivo"],
    ["Criatividade e imaginação", "Análise e lógica"],
    ["Sociável e extrovertido", "Reservado e introvertido"],
    ["Resiliente e determinado", "Relaxado e tranquilo"],
    ["Realização pessoal e profissional", "Conexão emocional e bem-estar"]
]

# Função para calcular os resultados com base nas respostas
def calcular_resultados(respostas):
    resultados = {}
    for atributo in correspondencia:
        resultados[atributo] = 0
        for i, resposta in enumerate(respostas):
            resultados[atributo] += correspondencia[atributo][int(resposta == "a")]
    return resultados

# Aplicativo web interativo com Streamlit
def main():
    st.title("Questionário de Personalidade")
    
    # Criar um dicionário para armazenar as respostas
    respostas = {}
    
    # Perguntar ao usuário todas as questões
    for i, pergunta in enumerate(perguntas):
        st.write(f"**Pergunta {i+1}:** {pergunta}")
        opcao_selecionada = st.radio("", opcoes[i], key=i)
        respostas[i] = "a" if opcao_selecionada == opcoes[i][0] else "b"
    
    # Calcular os resultados com base nas respostas
    resultados = calcular_resultados(list(respostas.values()))
    
    # Exibir os resultados em uma tabela interativa
    df_resultados = pd.DataFrame(list(resultados.items()), columns=["Atributo", "Pontuação"])
    st.write("**Resultados:**")
    st.dataframe(df_resultados)

    # Gerar a tabela de resultados em formato CSV
    st.download_button("Download CSV", data=df_resultados.to_csv(index=False), file_name="resultados.csv")

# Executar o aplicativo
if __name__ == "__main__":
    main()
