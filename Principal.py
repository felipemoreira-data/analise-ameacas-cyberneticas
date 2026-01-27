import streamlit as st


st.set_page_config(
    page_title="Análise de Ameaças Cibernéticas",
    page_icon= "💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)
st.markdown("""
    <style>
        /* Muda a cor de fundo da sidebar */
        [data-testid="stSidebar"] {
            background-color: #c3d5db;
        }
    </style>
""", unsafe_allow_html=True)


with open("styles/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.markdown('<div class="titulo-principal">Análise Exploratória de Ameaças Cibernéticas 💻</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo">2015 – 2024</div>', unsafe_allow_html=True)

st.write("---")


st.markdown("""
<div class="box">            
<div class="s-texto">
<b>Autor:</b> Felipe Moreira<br>           
<b>Curso:</b> Ciência de Dados e Inteligência Artificial <br>
</div>
</div>            
""", unsafe_allow_html=True)

st.write("---")


st.markdown("""
<div class="box">
<p>
Esta análise explora os dados globais sobre ameaças cibernéticas ocorridas entre os anos de 2015 e 2024. 
O objetivo é compreender os padrões dos tipos de ataques, o tamanho prejuízo financeiro, a proporção de usúarios atingidos e a relação (tempo x impacto causado).
Através da análise estatística e visual dos dados, buscamos extrair insights que contribuam para o entendimento e prevenção de riscos digitais em escala global.
</p>
</div>
""", unsafe_allow_html=True)

st.write("---")

st.markdown('<div class="box-ajustada"><a href="https://www.kaggle.com/datasets/sprasad018/global-cybersecurity-threats-2015-2024">Acesso ao Banco de Dados Utlizado</a></div>', unsafe_allow_html=True)


st.markdown('<div class="rodape">Use o menu lateral para navegar pelas seções da análise</div>', unsafe_allow_html=True)
