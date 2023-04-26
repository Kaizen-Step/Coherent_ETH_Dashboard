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
st.set_page_config(page_title='Transaction Fees - Ethereum After Shanghai Update',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('💸 Transaction Fees & Gas Usage ')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache_data()
def get_data(query):
    if query == 'ETH_Transaction':
        return pd.read_csv('Data/Users/ETH_Data_USer_TX.csv')
    elif query == 'ETH_TX_Heatmap_After':
        return pd.read_csv('Data/Users/Heatmaps_after.csv')
    elif query == 'ETH_TX_Heatmap_Before':
        return pd.read_csv('Data/Users/HeatMap_Before.csv')
    return None


ETH_Transaction = get_data('ETH_Transaction')
ETH_TX_Heatmap_After = get_data('ETH_TX_Heatmap_After')
ETH_TX_Heatmap_Before = get_data('ETH_TX_Heatmap_Before')

df = ETH_Transaction
df2 = ETH_TX_Heatmap_After
df3 = ETH_TX_Heatmap_Before
#################################################################################################
st.write(""" ### Transaction Fee on Ethereum ##  """)

st.write("""  Gas is a measure of the computational effort required to execute a transaction or contract on the Ethereum network. Every operation on the network, from transferring Ether (ETH) to executing smart contracts, requires a certain amount of gas. Gas fees are paid in ETH, the native cryptocurrency of the Ethereum network.    
The amount of gas required for a transaction or contract execution is determined by its complexity and the current demand on the network. The higher the demand for network resources, the higher the gas fee required to ensure that transactions are processed in a timely manner.   
Gas fees are paid to the miners who process and validate transactions on the network. Miners prioritize transactions with higher gas fees, so users who want their transactions processed quickly must pay a higher fee.   
In summary, gas usage and transaction fees are an essential part of the Ethereum network. They help ensure the security and stability of the network by incentivizing miners to process transactions and execute contracts.  


  """)


st.info(""" ##### In This Transaction Fees And Gas Usage Section you can find: ####

* After The Upgrade, Will Ethereum Fees Decrease?
* Ethereum Transaction Pattern After Shanghai Upgrade




""")


#################################################################################################
st.write(""" ## After The Upgrade, Will Ethereum Fees Decrease?  """)

st.write(""" After the Shanghai improvement, Ethereum fees will indeed fall. This is due to the upgrade's equalization of block size and overall improvement in call-data efficiency throughout the Ethereum network.
"When specialized chains can build on a layer-2 like Polygon and lower the cost of communicating with the base chain Ethereum, that reduces gas prices for users everywhere in the ecosystem by making it more efficient to scale horizontally in a way that spreads demand." Gelen Moore
The network will last longer overall because to the lower transaction prices. A WARM coinbase is also anticipated to be included with the Ethereum Shanghai upgrade, which will slightly reduce the fees paid by well-known constructors like Flashbots and BloXroute.
    """)

# Daily Transactions Before and After Shanghai Update
fig = px.bar(df, x="DATE", y="DAILY_TRANSACTION", color="STATUS",
             title='Daily Transactions Before and After Shanghai Update')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Daily Number of Transactions')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Daily Average Gas Used Before and After Shanghai Update
fig = px.area(df, x="DATE", y="AVERAGE_GAS_USED", color="STATUS",
              title='Daily Average Gas Used Before and After Shanghai Update [Log Value]')
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_type="log",
                  yaxis_title='Daily Number of Transactions')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


#####################################################
st.write(""" ## Ethereum Transaction Pattern After Shanghai Upgrade """)

st.write(""" One significant change that the Shanghai upgrade brought to Ethereum transactions is the reduction in gas fees. Gas fees are the fees paid by users to miners to process transactions on the Ethereum network. Before the upgrade, gas fees were often high, making it expensive to execute transactions on the network. However, the Shanghai upgrade introduced a new pricing algorithm that reduced gas fees by up to 50%, making transactions more affordable for users.
Another pattern that emerged after the Shanghai upgrade is the increased speed of transaction processing. The upgrade included several optimizations that reduced the time it takes to validate and confirm transactions on the network. This has resulted in faster transaction confirmation times and improved overall network throughput.
The Shanghai upgrade also introduced new features that have impacted Ethereum transaction patterns. One such feature is the introduction of a new transaction type called "access list transactions." Access list transactions provide a more efficient way to execute certain types of smart contracts and reduce the cost of executing those contracts.""")


c1, c2 = st.columns(2)

with c2:
    st.write(""" ### After Shanghai Upgrade """)
    # Block per minute on hour of day (UTC)
    fig = px.density_heatmap(df2, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="block per minute on hour of day (UTC)",
                             histfunc='avg', title="Block per minute on hour of day (UTC)".title(), nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
        'dtick': 1}, coloraxis_colorbar=dict(title="block per minute on hour of day (UTC)"))
    fig.update_yaxes(categoryorder='array')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # transactions per minute on hour of day (UTC)
    fig = px.density_heatmap(df2, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="transactions per minute on hour of day (UTC)",
                             histfunc='avg', title="transactions per minute on hour of day (UTC)".title(), nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
        'dtick': 1}, coloraxis_colorbar=dict(title="transactions per minute on hour of day (UTC)"))
    fig.update_yaxes(categoryorder='array')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c1:
    st.write(""" ### Before Shanghai Upgrade """)
    # Block per minute on hour of day (UTC)
    fig = px.density_heatmap(df3, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="block per minute on hour of day (UTC)",
                             histfunc='avg', title="Block per minute on hour of day (UTC)".title(), nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
        'dtick': 1}, coloraxis_colorbar=dict(title="block per minute on hour of day (UTC)"))
    fig.update_yaxes(categoryorder='array')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # transactions per minute on hour of day (UTC)
    fig = px.density_heatmap(df3, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="transactions per minute on hour of day (UTC)",
                             histfunc='avg', title="transactions per minute on hour of day (UTC)".title(), nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
        'dtick': 1}, coloraxis_colorbar=dict(title="transactions per minute on hour of day (UTC)"))
    fig.update_yaxes(categoryorder='array')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
##########################################################################

st.text(" \n")

st.info(""" #### SnowFlake Query: #### """)

st.write(""" I know joining tables with the Block Hash is not the best choice, but due to the Coherent Ethereum Raw Data limited columns, it is the only choice.""")
st.image(Image.open('Images/SQL_Heatmap.jpg'))
