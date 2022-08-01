import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer, set_seed
import torch
import re
import urllib.request
from PIL import Image

torch.set_default_tensor_type(torch.cuda.FloatTensor)
model = AutoModelForCausalLM.from_pretrained("bigscience/bloom-1b3", use_cache=True)
tokenizer = AutoTokenizer.from_pretrained("bigscience/bloom-1b3")

set_seed(424242)

model.__class__.__name__

#prompt = ''
texto0 = st.text_area("Escreva sintomas causados por algum vírus, ou o nome dele.", "")

input_ids = tokenizer(prompt, return_tensors="pt").to(0)

sample = model.generate(**input_ids, max_length=100, top_k=0, temperature=0.7)



#print(tokenizer.decode(sample[0], truncate_before_pattern=[r"\n\n^#", "^'''", "\n\n\n"]))



st.title("Labinftec")

#keyopenai = st.text_input("Coloque a chave da OpenAI aqui", "")

texto_quebrado = texto0.replace(',', '\n')
if st.button("Detalhar"):
    if texto0 == "":
        st.write("Você precisa escrever algo na caixa de texto.")
    else: 
        
        prompt = "Lista:\n"+texto_quebrado+"\n'''\nFale sobre as características do vírus da lista (nome científico ou a qual família pertence, envelope, diametro, se é RNA ou DNA, sua replicação, informações do genoma, em qual hospedeiro parasita - animais, planta, bacterias, fungos etc, qual sua classe/tamanho), se for sintomas, escolha o vírus que mais se aproxima aos sintomas dados na lista e mostre os motivos da escolha:
        texto = tokenizer.decode(sample[0], truncate_before_pattern=[r"\n\n^#", "^'''", "\n\n\n"])
        t.write("Detalhes obtidos:")
        padrao = re.compile(r'\w+[dae]$')
        familia = padrao.findall(texto)
        link = 'https://www.gettyimages.com.br/fotos/' #-
        link2 ='-virus?assettype=image&phrase'

        def pesquisar(familia):
            url = link + familia + link2
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            html = urllib.request.urlopen(req).read()

            for i in re.findall(r'<img.*?src="(.*?)"', str(html)):
                if i.startswith('http') and not i.endswith('.gif'):
                    urllib.request.urlretrieve(i, 'imagem.jpg')
                    break
        if len(familia) == 0:
            st.write("Não foi possível encontrar uma imagem para mostrar.")
        else:
            pesquisar(familia[0])
            st.image('imagem.jpg', use_column_width=True)
            os.remove('imagem.jpg')
            st.write("Imagem do vírus encontrado pela internet.")
            
        content = texto
        explicação0 = "Lista:\n"+texto_quebrado+"\n'''\nDescreva os vírus da lista:\n\n"+content+"\nCite vírus relacionado e explique: Além desse,",
        input_ids = tokenizer(explicação0, return_tensors="pt").to(0)
        sample = model.generate(**input_ids, max_length=100, top_k=0, temperature=0.7)
        
        explicação = tokenizer.decode(sample[0], truncate_before_pattern=[r"\n\n^#", "^'''", "\n\n\n"])
        st.write(content+".\n\n"+"Além desse,"+explicação)
        st.write("[Você não pode confiar 100% nessa resposta. O programa ainda está em fase de desenvolvimento e pode conter erros.]")
