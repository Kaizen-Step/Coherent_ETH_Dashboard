# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image


# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Aknowledgement - Russia Ukraine Conflict',
                   page_icon=':bar_chart:', layout='wide')
st.title('🪔 References')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# SQL Codes
st.write(""" ## Acknowledgement ## """)

st.write("""
We are grateful to all who helped us develop this project specially [**Mr. Ali Taslimi**](https://twitter.com/AliTslm) with comprehensive streamlit open source project [Cross chain Monitoring](https://github.com/alitslm/cross_chain_monitoring) that provides streamlit functions and tools.
And also ****Coherent**** with Ethereum Raw databases and last but not least ****MetricsDao**** that is the reason behind this project.


""")

st.text(" \n")
st.text(" \n")

# Sources
st.write(""" ## Sources ## """)

st.write("""
Here are the reference numbers for all of the sources used in this project:
  


""")

st.write("""  
  1.https://sensoriumxr.com/articles/375   
2.https://cryptopotato.com/what-is-the-ethereum-shanghai-shapella-upgrade-everything-you-need-to-know/        
3. https://www.nasdaq.com/articles/can-you-still-mine-ethereum-after-the-merge      
4. https://finance.yahoo.com/crypto/     
5. https://www.coindesk.com/tech/2023/04/12/ethereums-shanghai-upgrade-activates-starting-new-era-of-staking-withdrawals/    


""")
