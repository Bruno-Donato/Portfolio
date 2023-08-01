import streamlit as st
from PIL import Image
import base64
from base64 import b64encode

st.set_page_config(
    page_title = "Brundo Donato - Portifolio Data Science",
    layout = "wide"
)


st.write("<div align='center'><h1><b>Bruno de Sousa Donato</b></h1></div>", unsafe_allow_html=True)

st.markdown("""<div style='text-align: center;'><hr style='border-top: 5px solid black'></div>""", unsafe_allow_html=True)

st.write("<div align='center'><h2><i>| Ciência de dados | Machine Learning | IA | Python | SQL |</i></h2></div>", unsafe_allow_html=True)

st.write("")
st.write("")

tab1, tab2, tab3, tab4 = st.tabs(["Sobre Mim", "Curriculo","Projetos Ciência de Dados", "Posts e Estudos"])

with tab1:
    col1, col2 = st.columns([2, 5])
    image = Image.open("data/eu_felizao.jpeg")
    
    col1.write("")
    col1.write("")
    col1.write("")
    col1.image(image, caption='Eu felizão', width = 250)
    
    
    col1.write("")

    col2.write("")
    col2.write("")
    col2.write("""
               Sou cientista de dados, graduado em fisioterapia e mestre em ciências pela UNICAMP. Desde sempre curioso sobre ciência, 
               na adolescência me tornei leitor assíduo de autores como Carl Sagan, Isaac Asimov, Frank Herbert, Bertrand Russel, Karl Popper, 
               e muitos outros que me direcionaram a vida acadêmica.
               """)
    
    col2.write("""
               No mestrado tive o primeiro contato mais aprofundado com estatística e me apaixonei logo de cara. Sempre gostei de aprender novas coisas, temas 
               e habilidades, e de maneira autodidata, com muita paciência, horas de dedicação e muito mais curiosidade, aprendi SPSS, e linguagens 
               de programação R, Python, SQL e ferramentas como Power BI/Excel. Sempre procurando aprimorar meus conhecimentos.
               """)
    
    col2.write("""
               Atuei como fisioterapeuta, atendendo diretamente pessoas e públicos de perfis diversos em diferentes instituições, por quase 10 anos 
               e decidi entrar no mundo dos dados para seguir meus objetivos de vida, pois procuro liberdade, possibilidade de crescimento profissional 
               e pessoal, e novos desafios.
               """)
    
    col2.write("""
               Atualmente aprimorando meus conhecimentos em ciência de dados e machine learning na TERA, consequentemente e felizmente absorvendo 
               novos conhecimentos.
               """)           
    
    col2.write("""
               Cachorreiro, amante da música, literatura, calistenia, queijos, cerveja, café e fotografia. Difundindo conhecimento e buscando 
               ser sempre melhor do que ontem.
               """)


with tab2:
    col1, col2, col3 = st.columns([.13, .10, 1])
    with col1:
        with open("data/bruno_donato_ciencia_de_dados_CV.pdf", "rb") as pdf_file:
            b64_pdf = base64.b64encode(pdf_file.read()).decode()
            href = f'<a href="data:application/pdf;base64,{b64_pdf}" download="Bruno_Donato_Ciencia_de_Dados_CV.pdf">Download CV</a>'
            st.markdown(href, unsafe_allow_html=True)
    
    col2.markdown('[LinkedIn](https://www.linkedin.com/in/bruno-de-sousa-donato/)')
    col3.markdown('[GitHub](https://github.com/Bruno-Donato)')

    st.header("**Experiência Profissional**")
    st.subheader("**_CIENTISTA DE DADOS - Autônomo (01/2022 - Atual)_**")
    st.write("""
             Trabalho junto a empreendedores locais com análise de dados e business intelligence abordando as principais métricas e KPIs,
             implementando pipelines e modelos de machine learning, utilizando webapps e dashboards para deployment e acompanhamento de 
             projetos. Usando criatividade para adequar o serviço ao perfil de cada cliente e tornar insights acessíveis e compreensíveis
             para orientar tomadas de decisões.
             """)
    
    st.subheader("")
    st.subheader("**_CONSULTORIA ACADÊMICA - Autônomo (09/2019 - Atual)_**")
    st.write("""
             Consultorias de trabalhos acadêmicos para elaboração e análise estatística exploratória/descritiva e inferencial. Aplicação e
             conhecimento em testes de correlação, modelos lineares e não-lineares, teste chi-quadrado, testes paramétricos (teste-t, ANOVA)
             e seus correlatos não paramétricos. Aulas e tutorias de fundamentos de estatística e pesquisa para área da saúde.
    """)
    
    st.subheader("")
    st.subheader("**_FISIOTERAPEUTA/CONSULTOR - SUS Paulínia/SP (06/2019 - 03/2022)_**")
    st.write("""
            Avaliação, diagnóstico e reabilitação de pacientes ortopédicos e dor crônica, e trabalho com equipes multi e interdisciplinares do
            sistema de saúde público. Criação, gerenciamento e análise de banco de dados do serviço de reabilitação da cidade de Paulínia e
            seus usuários, orientando políticas públicas de saúde, promovendo direcionamento apropriado para atendimento e cuidado precoce 
            (redução de 50% do tempo de espera para avaliação/atendimento), através de processo de triagem e classificação, baseada em dados 
            epidemiológicos e estatística local e implementação de atendimentos em grande escala (aumento de 20% de capacidade de atendimento).
    """)
    
    st.subheader("")
    st.subheader("**_FISIOTERAPEUTA - Autônomo (01/2014 - 2022)_**")
    st.write("""
             - Atendimento em clínica e domiciliar em ortopedia e traumatologia (pré e pós operatório).
             - Experiência em reabilitação e cuidado ao idoso.
             - Atenção e manejo da dor em pacientes com dor crônica.
    """)
    
    st.subheader("")
    st.subheader("**_PESQUISADOR - UNICAMP (01/2017 - 08/2019)_**")
    st.write("""
            Atendimento e coleta de dados dos usuários do ambulatório de reabilitação do hospital de clínicas, gerenciamento e análise
            (descritiva e inferencial) de dados do setor e projetos associados, com 2 anos de experiência em otimização de fluxo de pacientes,
            coleta e armazenamento de dados para fins de pesquisa clínica/acadêmica.,
    """)
    
    st.header("")
    st.header("**Educação**")
    st.subheader("**_CIÊNCIA DE DADOS & MACHINE LEARNING - TERA Ensino Superior (09/2022 - 07/2023)_**")
    st.write("""
            Aprofundamento em banco de dados, análise e visualização de dados (Pandas, Numpy, Matplotlib, Seaborn, Plotly, Yellowbrick),
            computação paralela e distribuída (Databricks/Spark), pipelines, modelos supervisionados - previsão (regressão linear, Decision
            Tree Regressor, Random Forest Regressor), classificação (regressão logística, KNN, SVM, Decision Tree/Árvore de decisão, Random 
            Forest, XGBoost) séries temporais (AR, MA, ARMA, ARIMA), e não supervisionados - sistemas de recomendação e clusterização (K-means, 
            DBSCAN, Kprototypes, Kmodes, Gaussian Mixture, Hierarchical/Agglomerative), ML/IA, deep learning/redes neurais e NLP (Scikit-learn, 
            PyCaret, Scipy, StatsModels, Optuna, XGBoost, LightGBM, Keras, TensorFlow, Pytorch, Spacy, NLTK, Gensim, REGEX, HuggingFace/transformers), 
            deploy de projetos (Streamlit, MLFow).
    """)
    
    st.subheader("")
    st.subheader("**_MESTRADO - UNICAMP (01/2017 - 08/2019)_**")
    st.write("""
             - Metodologia de pesquisa cientifica, didática acadêmica 
             - Análise estatística: descritiva e inferencial para produção científica
             - Implementação e gerenciamento de banco de dados para usuários do sistema de saúde do setor de reabilitação 
             - Análise descritiva e inferencial para trabalhos acadêmicos
             - Experiencia em coleta, gerenciamento, limpeza, análise e visualização de dados, estatística descritiva e testes de hipótese - correlações, 
             regressão linear/logística (simples/múltipla), modelos não lineares, teste chi-quadrado, paramétricos (teste t, ANOVA) e não paramétricos.
             """)
    
    st.subheader("")
    st.subheader("**_FISIOTERAPIA - PUCCAMP (01/2009 - 12/2013)_**")
    st.write("""
             - Iniciação científica: coleta, análise de dados e produção científica em linha de pesquisa de variabilidade da frequência cardíaca
             - Monitor de disciplinar cinesioterapia, anatomia e neuroanatomia
    """)

with tab3:
    st.subheader("")
    col1, col2, col3, col4, col5 = st.columns([3, 0.5, 3, 0.5, 3])
    col1.write("__NLP | Webscraping__")
    image1 = Image.open("data/o_mundo_assombrado.png")
    col1.image(image1, use_column_width=True)
    with col1:
        link1 = "https://github.com/Bruno-Donato/nlp_reviews_livro/blob/main/nlp_reviews_o_mundo_assombrado.ipynb"
        text1 = "Análise de Reviews - Carl Sagan"
        markdown1 = f'<a href="{link1}" target="_blank">{text1}</a>'
        st.markdown(markdown1, unsafe_allow_html=True)
    
    col3.write("__Análise Estatística | Webscraping__")
    image3 = Image.open("data/artigos_fisio.png")
    col3.image(image3, use_column_width=True)
    with col3:
        link3 = "https://bruno-donato-artigosfisio-pedro.streamlit.app/"
        text3 = "Produção científica na fisioterapia - PEDro"
        markdown3 = f'<a href="{link3}" target="_blank">{text3}</a>'
        st.markdown(markdown3, unsafe_allow_html=True)
    
    col5.write("__Modelos de Classificação__")
    image5 = Image.open("data/fraude2.jpg")
    col5.image(image5, use_column_width=True)
    with col5:
        link5 = "https://github.com/Bruno-Donato/classificacao_desafio_tera/blob/main/desafio_classificacao.ipynb"
        text5 = "Detecção de Fraudes - Desafio TERA"
        markdown5 = f'<a href="{link5}" target="_blank">{text5}</a>'
        st.markdown(markdown5, unsafe_allow_html=True)

    st.write("")
    
    col6, col7, col8, col9, col10 = st.columns([3, 0.5, 3, 0.5, 3])
    col6.write("__Análise Descritiva | NLP | Webapp Deploy__")
    image6 = Image.open("data/dashboard_loja.png")
    col6.image(image6, use_column_width=True)
    with col6:
        link6 = "https://bruno-donato-loja-virtual-instrumentos-musicais.streamlit.app/"
        text6 = "Dashboard loja virtual - Projeto Real"
        markdown6 = f'<a href="{link6}" target="_blank">{text6}</a>'
        st.markdown(markdown6, unsafe_allow_html=True)
        
    col8.write("__Modelos de Previsão__")
    image8 = Image.open("data/gastos_saude.png")
    col8.image(image8, use_column_width=True)
    with col8:
        link8 = "https://github.com/Bruno-Donato/desafio_gastos_saude/blob/main/regress_gastos_saude.ipynb"
        text8 = "Previsão de gastos em saúde"
        markdown8 = f'<a href="{link8}" target="_blank">{text8}</a>'
        st.markdown(markdown8, unsafe_allow_html=True)
        
    col10.write("__Modelos de Clusterização__")
    image10 = Image.open("data/ifood.png")
    col10.image(image10, use_column_width=True)
    with col10:
        link10 = "https://bruno-donato-cluster-ifood.streamlit.app/"
        text10 = "Segmentação Clientes ifood"
        markdown10 = f'<a href="{link10}" target="_blank">{text10}</a>'
        st.markdown(markdown10, unsafe_allow_html=True)

    
with tab4:
    col1, col2, col3, col4 = st.columns([0.25, 3, 5, 0.25])
    col2.subheader("O que é ciência de dados?")
    image = Image.open("data/zeca_dados.jpg")
    col2.image(image, use_column_width=True)
    
    col3.header("")
    col3.header("")
    col3.write("""
               Primeiro de uma série e posts que tem como objetivo explicar a ciência de dados de maneira acessível 
               e desmistificada, com foco naqueles que assim como eu querem ou estão fazendo transição de carreira.
               """)
    with col3:
        link = "https://medium.com/p/9b71108b6060"
        text = "Leia o post"
        markdown = f'<a href="{link}" target="_blank">{text}</a>'
        st.markdown(markdown, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([0.25, 8, 0.25])
    col2.markdown("""<div style='text-align: center;'><hr style='border-top: 1px solid black'></div>""", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns([0.25, 3, 5, 0.25])
    col2.subheader("O que é ciência de dados II? ")
    image = Image.open("data/terminator_captcha.png")
    col2.image(image, use_column_width=True)
    
    col3.header("")
    col3.header("")
    col3.write("""
               Continuação do post anterior com objetivo explicar a ciência de dados de maneira acessível desmistificada, 
               com foco naqueles que assim como eu querem ou estão fazendo transição de carreira. Dessa vez abordaremos 
               o aprendizado supervisionado.
               """)
    with col3:
        link = "https://medium.com/@bruno.sousadonato/que-diabos-é-ciência-de-dados-parte-2-aprendizado-supervisionado-9f8ad27b2f57"
        text = "Leia o post"
        markdown = f'<a href="{link}" target="_blank">{text}</a>'
        st.markdown(markdown, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([0.25, 8, 0.25])
    col2.markdown("""<div style='text-align: center;'><hr style='border-top: 1px solid black'></div>""", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns([0.25, 3, 5, 0.25])
    col2.subheader("O que é ciência de dados III? ")
    image = Image.open("data/bolo_dados.png")
    col2.image(image, use_column_width=True)
    
    col3.header("")
    col3.header("")
    col3.write("""
               Terceira e ultima parte do post de introdução conceitual amigável à ciência de dados, de maneira acessível desmistificada, 
               com foco naqueles que assim como eu querem ou estão fazendo transição de carreira. Nele abordamos o aprendizado não supervisionado.
               """)
    with col3:
        link = "https://medium.com/@bruno.sousadonato/que-diabos-é-ciência-de-dados-parte-3-aprendizado-não-supervisionado-e5a5dd23a28d"
        text = "Leia o post"
        markdown = f'<a href="{link}" target="_blank">{text}</a>'
        st.markdown(markdown, unsafe_allow_html=True)
    