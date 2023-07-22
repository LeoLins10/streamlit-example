import pandas as pd
import streamlit as st

# Definir a tabela de correspondência
correspondencia = {
    # ... (código omitido para brevidade)
}

# Definir as perguntas e as opções de resposta
perguntas = [
    # ... (código omitido para brevidade)
]

opcoes = [
    # ... (código omitido para brevidade)
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
