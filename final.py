import streamlit as st
import gtts
import time
from translate import Translator
dic={'en':"English",'mr':"Marathi",'hi':"Hindi",'ar':"Arabic","bn":"Bengali","zh":"Chinese","fr":"French","de":"German","gu":"Gujrati","he":"Hebrew",'IT':"Italian",'ja':"Japnese",'kn':"Kannada"}
st.markdown("<h1 style='text-align: center;'>Hello World</h1>", unsafe_allow_html=True)
st.success("Play audio for info")
audio_file = open('now.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/mp3')
ll=st.selectbox("In which language you want your audio file ?",['English','Marathi','Hindi','Arabic','Bengali','Chinese','French','German','Gujrati','Hebrew','Italian','Japnese','Kannada'])
t=st.text_input("Enter your text here")
dest=list(dic.keys())[list(dic.values()).index(ll)]
translator = Translator(to_lang=dest)
translations = translator.translate(t)
if st.button("SUBMIT"):
    with st.spinner('Wait for it... '):
        time.sleep(3)
    try:
        st.success("Your translated text is "+str(translations))    
        s=gtts.gTTS(text=translations,lang=dest,slow=False)
        s.save('result.mp3')
        a=open('result.mp3', 'rb')
        b = a.read()
        st.audio(b, format='audio/mp3')
    except ValueError:
        st.markdown("<h1 style='text-align: center;'>Sorry dear..My Boss is not able to convert your text in this language audio file please try another language.</h1>", unsafe_allow_html=True)
        
   
