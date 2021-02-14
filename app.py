import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report




#file_upload = st.file_uploader("Uploader votre csv à analyser", type=["csv"])
file_upload = st.file_uploader("Uploader votre json à analyser", type=["json"])
#file_upload = st.file_uploader("Uploader votre csv à analyser")

#print(type(file_upload))

if file_upload is not None:
    # df = pd.read_csv(file_upload)
     df = pd.read_json(file_upload)

else:
	
	df = pd.DataFrame(
		np.random.rand(100, 5),
		columns=['a', 'b', 'c', 'd', 'e']
	)

pr = ProfileReport(df, explorative=True)

st.title("Pandas Profiling in Streamlit")
st.write(df)
st_profile_report(pr)
