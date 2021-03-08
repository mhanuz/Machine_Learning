import streamlit as st
import spacy_streamlit

import spacy_streamlit
import spacy
nlp=spacy.load('en_core_web_sm')

def main():

	st.title('Tokenization and Named Entity Recognition APP')

	menu=['Home','NER']
	choice= st.sidebar.selectbox('Selection Menu',menu)



	if choice =='Home':
		st.subheader('Tokenization')
		raw_text=st.text_area('Please enter your text below')
		docx=nlp(raw_text)
		if st.button('Tokenize'):
			spacy_streamlit.visualize_tokens(docx)



	elif choice=='NER':
		st.subheader('Named Entity Recognition')
		raw_text=st.text_area('Please enter your text here')
		docx=nlp(raw_text)
		if st.button('Show NER'):
			spacy_streamlit.visualize_ner(docx,labels=nlp.get_pipe('ner').labels)

if __name__ == '__main__':
	main()