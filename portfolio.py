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
st.write("<div align='center'><h2><i>| Ciência de Dados | Machine Learning | IA | Análise de Dados | Python |</i></h2></div>", unsafe_allow_html=True)
st.write("")
st.write("")
tab0, tab1, tab2, tab3, tab4 = st.tabs(["Início", "Sobre Mim", "Curriculo","Projetos", "Posts e Estudos"])

with tab0:
    st.markdown("<h2 style='text-align: center;'>Soluções em Dados e Tecnologia </h2>", unsafe_allow_html=True)
    st.write("""
            """)
    st.write("""
            Bem-vindos e muito obrigado pela visita! 
            """)
    st.write("""
            Aqui, você encontrará soluções e serviços voltados para pequenos empreendedores, empresas, estudantes e qualquer pessoa que 
            necessite utilizar a tecnologia para resolver seus problemas. 
            """)
    st.write("""
            Minha proposta é fazer a ponte entre a tecnologia e você, oferencendo uma gama abrangente de serviços, que vão desde tarefas simples 
            de abertura e manipulação de arquivos e trabalhos de média complexidade como análises, manipulação e visualização de dados, criação 
            e gerenciamento de bancos de dados e raspagem de dados (webscraping) para dar o suporte necessário que o seu negócio precisa. 
            """)
    st.write("""
            Além disso, ofereço soluções mais avançadas, utilizando modelos de aprendizado de máquina, inteligência artificial, processamento 
            de linguagem natural e extração de informações, visão computacional e muito mais. 
            """)
    st.write("""
            Seja qual for a sua necessidade, estou comprometido em utilizar a tecnologia para encontrar as melhores soluções e ajudá-lo a 
            alcançar seus objetivos. Estou ansioso para colaborar e transformar desafios em resultados reais e que façam a diferença!
            """)

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
               Formado em Ciência de dados & Machine Learning pela TERA (Ensino Superior) e atualmente aprimorando meus conhecimentos focando no aprofundamento
               em visualização de dados, machine learning e deep learning e visão computacional.
               """)           
    col2.write("""
               Cachorreiro, amante da música, literatura, calistenia, queijos, cerveja, café e fotografia. Difundindo conhecimento e buscando 
               ser sempre melhor do que ontem.
               """)

with tab2:
    col1, col2, col3 = st.columns([.13, .11, 1])   
    col1.markdown('<a href="https://www.linkedin.com/in/bruno-de-sousa-donato/" target="_blank">'
            '<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank">'
            '</a>', unsafe_allow_html=True)
    col2.markdown('<a href="https://github.com/Bruno-Donato" target="_blank">'
            '<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" target="_blank">'
            '</a>', unsafe_allow_html=True)
    with col3:
        with open("data/bruno_donato_ciencia_de_dados_CV.pdf", "rb") as pdf_file:
            b64_pdf = base64.b64encode(pdf_file.read()).decode()
            href = f'<a href="data:application/pdf;base64,{b64_pdf}" download="Bruno_Donato_Ciencia_de_Dados_CV.pdf">Download CV</a>'
            st.markdown(href, unsafe_allow_html=True)

    st.header("**Experiência Profissional**")
    st.subheader("**_CIENTISTA DE DADOS - Autônomo (01/2022 - Atual)_**")
    st.write("""
             Trabalho com empreendedores locais com análise e visualização de dados (Pandas, Numpy, Matplotlib, Seaborn, Plotly,
             Yellowbrick) e business intelligence, utilizando modelos supervisionados - previsão (regressão linear, Decision Tree Regressor,
             Random Forest Regressor, XGBoost), classificação (regressão logística, KNN, SVM, Decision Tree/Árvore de decisão, Random
             Forest, XGBoost, LightGBM) séries temporais (AR, MA, ARMA, ARIMA), e não supervisionados - sistemas de recomendação e
             clusterização (K-means, DBSCAN, Kprototypes, Kmodes, Gaussian Mixture, Hierarchical/Agglomerative) utilizando as principais
             bibliotecas (Scikit-learn, PyCaret, Scipy, StatsModels, Optuna, XGBoost, LightGBM) para extração de insights e orientar tomadas
             de decisão. Aprofundamento e utilização em deep learning/redes neurais e NLP para solução de problemas como extração de dados
             e processamento de imagens e linguagem (Keras, TensorFlow, Pytorch, Spacy, NLTK, Gensim, REGEX,
             HuggingFace/Transformers). Utilização de webapps e dashboards para deploy e monitoramento (Streamlit, MLFow).
             """)
    st.subheader("")
    st.subheader("**_CONSULTORIA ACADÊMICA - Autônomo (09/2019 - Atual)_**")
    st.write("""
             Consultorias de trabalhos acadêmicos para elaboração e análise estatística exploratória/descritiva e inferencial. Aplicação e
             conhecimento em testes de correlação, modelos lineares e não-lineares, teste chi-quadrado, testes paramétricos (teste-t, ANOVA)
             e seus correlatos não paramétricos. Aulas e tutorias de fundamentos de estatística e pesquisa para área da saúde.
    """)
    st.subheader("")
    st.subheader("**_CONSULTOR EM DADOS/FISIOTERAPEUTA - SUS Paulínia/SP (06/2019 - 03/2022)_**")
    st.write("""
             Responsável pela criação, gerenciamento e análise de banco de dados do serviço de reabilitação da cidade de Paulínia e seus
             usuários, orientando políticas públicas de saúde, promovendo direcionamento apropriado para atendimento e cuidado precoce
             (redução de 50% do tempo de espera para avaliação/atendimento), através de processo de triagem e classificação, baseada em
             dados epidemiológicos e estatística local e implementação de atendimentos em grande escala (aumento de 20% de capacidade de
             atendimento). Atendimento, avaliação, diagnóstico e reabilitação de pacientes ortopédicos e dor crônica, e trabalho com equipes
             multi e interdisciplinares do sistema de saúde público.
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
            Aprofundamento em banco de dados, análise e visualização de dados, computação paralela e distribuída (Databricks/Spark),
            pipelines, modelos supervisionados e não supervisionados, deep learning, inteligência artificial (IA), deploy de projetos
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
    
    col3.write("__NLP Transformers(HuggingFace)__")
    image3 = Image.open("data/huggingface_logo.png")
    col3.image(image3, use_column_width=True)
    with col3:
        link3 = "https://github.com/Bruno-Donato/projeto_tera"
        text3 = "Detecção de discurso de ódio - Twitter"
        markdown3 = f'<a href="{link3}" target="_blank">{text3}</a>'
        st.markdown(markdown3, unsafe_allow_html=True)
    
    col5.write("__Análise Estatística | Webscraping__")
    image5 = Image.open("data/artigos_fisio.png")
    col5.image(image5, use_column_width=True)
    with col5:
        link5 = "https://bruno-donato-artigosfisio-pedro.streamlit.app/"
        text5 = "Produção científica na fisioterapia - PEDro"
        markdown5 = f'<a href="{link5}" target="_blank">{text5}</a>'
        st.markdown(markdown5, unsafe_allow_html=True)

    st.write("")
    
    col6, col7, col8, col9, col10 = st.columns([3, 0.5, 3, 0.5, 3])
    col6.write("__Análise Descritiva | Webapp Deploy__")
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
        link8 = "https://github.com/Bruno-Donato/desafio_gastos_saude/tree/main"
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
    