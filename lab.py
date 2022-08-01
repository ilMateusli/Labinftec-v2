import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer, set_seed
import torch
import re

torch.set_default_tensor_type(torch.cuda.FloatTensor)

model = AutoModelForCausalLM.from_pretrained("bigscience/bloom-1b3", use_cache=True)
tokenizer = AutoTokenizer.from_pretrained("bigscience/bloom-1b3")

set_seed(424242)

model.__class__.__name__

#prompt = ''

#print(tokenizer.decode(sample[0], truncate_before_pattern=[r"\n\n^#", "^'''", "\n\n\n"]))



st.title("Labinftec")

#keyopenai = st.text_input("Coloque a chave da OpenAI aqui", "")
texto0 = st.text_area("Escreva sintomas causados por algum vírus, ou o nome dele.", "")

texto_quebrado = texto0.replace(',', '\n')
if st.button("Detalhar"):
    if texto0 == "":
        st.write("Você precisa escrever algo na caixa de texto.")
    else:

        sample = model.generate(**input_ids, max_length=50, top_k=0, temperature=0.7)
        
        prompt = "Lista:\n"+texto_quebrado+"\n'''\nFale sobre as características do vírus da lista (nome científico ou a qual família pertence, envelope, diametro, se é RNA ou DNA, sua replicação, informações do genoma, em qual hospedeiro parasita - animais, planta, bacterias, fungos etc, qual sua classe/tamanho), se for sintomas, escolha o vírus que mais se aproxima aos sintomas dados na lista e mostre os motivos da escolha:\n\n'''"
        input_ids = tokenizer(prompt, return_tensors="pt").to(0)
        texto = tokenizer.decode(sample[0], truncate_before_pattern=[r"\n\n^#", "^'''", "\n\n\n"])
        t.write("Detalhes obtidos:")
        
        #content = texto
        #explicação0 = "Lista:\n"+texto_quebrado+"\n'''\nDescreva os vírus da lista:\n\n"+content+"\nCite vírus relacionado e explique: Além desse,",
        #input_ids = tokenizer(explicação0, return_tensors="pt").to(0)
        #sample = model.generate(**input_ids, max_length=100, top_k=0, temperature=0.7)
        
        #explicação = tokenizer.decode(sample[0], truncate_before_pattern=[r"\n\n^#", "^'''", "\n\n\n"])
        st.write(texto)#+".\n\n"+"Além desse,"+explicação)
        st.write("[Você não pode confiar 100% nessa resposta. O programa ainda está em fase de desenvolvimento e pode conter erros.]")
