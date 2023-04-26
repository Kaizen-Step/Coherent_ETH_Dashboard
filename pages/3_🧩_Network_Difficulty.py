# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

# Theme
theme_plotly = None  # None or streamlit


# Layout
st.set_page_config(page_title=' Network Difficulty -  Ethereum After Shanghai Update',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🧩 Network Difficulty')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache_data()
def get_data(query):
    if query == 'ETH_Diff':
        return pd.read_csv('Data/Difficulty/ETH_Difficulty.csv')
    elif query == 'ETH_Diff2':
        return pd.read_csv('Data/Difficulty/ETH_Difficulty2.csv')
    elif query == 'ETH_Diff':
        return pd.read_csv('Data/Difficulty/ETH_Difficulty.csv')
    return None


ETH_Diff = get_data('ETH_Diff')
ETH_Diff2 = get_data('ETH_Diff2')

df = ETH_Diff
df2 = ETH_Diff2
#################################################################################################
st.write(""" ### Network Difficulty Concept ##  """)

st.write(""" Network difficulty in crypto refers to the level of complexity involved in the process of validating new transactions and adding them to the blockchain ledger. In other words, it measures how hard it is to find a new block in the blockchain network.
In most cryptocurrency networks, such as Bitcoin, the difficulty level is adjusted regularly to maintain a stable rate of block creation. This adjustment ensures that the block creation rate remains roughly constant, regardless of changes in the network's computational power.
The difficulty level is typically expressed as a numerical value that represents the number of hashes required to find a new block. As the computational power of the network increases, the difficulty level also increases to maintain a stable block creation rate. Conversely, if the computational power of the network decreases, the difficulty level decreases as well.
Higher network difficulty levels make it more difficult for miners to find new blocks and receive block rewards, which can have a significant impact on the profitability of mining operations.
  """)


st.info(""" ##### In Network Difficulty Section you can find: ####


* ETH Total Difficulty
* ETH Daily Average Difficulty



""")


#################################################################################################
st.write(""" ### Ethereum Network Difficulty After Shanghai """)
st.write("""  Ethereum used a difficulty adjustment algorithm known as the "Ice Age," which was originally introduced as a way to encourage the network to transition to a Proof of Stake (PoS) consensus mechanism.
However, the Ice Age algorithm had become outdated and no longer served its original purpose, leading to issues with block times and transaction throughput. The Shanghai upgrade replaced the Ice Age with a new difficulty adjustment algorithm known as Ethereum Improvement Proposal (EIP) 3554.
EIP-3554 adjusts the network's difficulty based on the average block time over the past 1,024 blocks, rather than the previous algorithm's fixed block time. This means that the network's difficulty will adjust more quickly in response to changes in hash rate, leading to more stable block times and a more reliable network.
Since the implementation of the Shanghai upgrade and the EIP-3554 algorithm, the Ethereum network has seen a significant increase in its hash rate, indicating increased mining activity. This has resulted in a corresponding increase in the network's difficulty, as the algorithm adjusts to maintain a consistent block time.
""")
# Europian House Price Index
fig = px.bar(df2, x="DATE", y="TOTAL_DAILY_DIFFICULTY", color="STATUS",
             title='ETH Total Difficulty')
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_type="log",
                  yaxis_title='Difficulty')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Europian House Price Index
fig = px.area(df2, x="DATE", y="DAILY_DIFFICULTY", color="STATUS",
              title='ETH Daily Difficulty')
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_type="log",
                  yaxis_title='Difficulty')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

#####################################################

##########################################################################


st.text(" \n")

st.info(""" #### SnowFlake Query: #### """)

st.image(Image.open('Images/SQL_Difficulty.jpg'))
