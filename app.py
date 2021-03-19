import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.title("Analyser votre Dataset avec Pandas-profiling")
st.subheader("Insérer votre Dataset au format csv, Pandas-profiling s'occupe de l'analyser !")
st.write("""Pour chaque colonne, les statistiques suivantes - si elles sont pertinentes pour le type de colonne - sont présentées dans un rapport HTML interactif: \n

	- Inférence de type: détecte les types de colonnes dans un dataframe. \n
	Essentiels: type, valeurs uniques, valeurs manquantes \n
	Statistiques quantiles telles que valeur minimale, Q1, médiane, Q3, maximum, intervalle, intervalle interquartile \n
	Statistiques descriptives comme la moyenne, le mode, l'écart type, la somme, l'écart absolu médian, le coefficient de variation, l'aplatissement, l'asymétrie
	Valeurs les plus fréquentes \n
	Histogramme \n
	Corrélations mettant en évidence des variables hautement corrélées, matrices de Spearman, Pearson et Kendall \n
	Matrice des valeurs manquantes, nombre, carte thermique et dendrogramme des valeurs manquantes \n
	L'analyse de texte apprend les catégories (majuscules, espace), les scripts (latin, cyrillique) et les blocs (ASCII) de données textuelles. \n
	L'analyse des fichiers et des images extrait la taille des fichiers, les dates de création et les dimensions et recherche les images tronquées ou celles contenant des informations EXIF.""")

file_upload = st.file_uploader("Uploader votre csv à analyser", type=["csv"])
#file_upload = st.file_uploader("Uploader votre json à analyser", type=["json"])
#file_upload = st.file_uploader("Uploader votre csv à analyser")

#print(type(file_upload))

if file_upload is not None:
     df = pd.read_csv(file_upload)
     #df = pd.read_json(file_upload)

else:
	
	df = pd.DataFrame(
		np.random.rand(100, 5),
		columns=['a', 'b', 'c', 'd', 'e']
	)

pr = ProfileReport(df, explorative=True)


st.write(df)
st_profile_report(pr)
