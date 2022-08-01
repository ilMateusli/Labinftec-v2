import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer, set_seed
import torch
import re

#torch.set_default_tensor_type(torch.cuda.FloatTensor)

#model = AutoModelForCausalLM.from_pretrained("bigscience/bloom-1b3", use_cache=True)
#tokenizer = AutoTokenizer.from_pretrained("bigscience/bloom-1b3")

#set_seed(424242)

#model.__class__.__name__

#prompt = ''

#print(tokenizer.decode(sample[0], truncate_before_pattern=[r"\n\n^#", "^'''", "\n\n\n"]))



st.title("Labinftec")

#keyopenai = st.text_input("Coloque a chave da OpenAI aqui", "")
texto0 = st.text_area("Escreva sintomas causados por algum vírus, ou o nome dele.", "")

texto_quebrado = texto0.replace(',', '\n')
