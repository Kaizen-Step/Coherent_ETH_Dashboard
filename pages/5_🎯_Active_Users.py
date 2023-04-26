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
st.set_page_config(page_title='Active Users - Ethereum After Shanghai Update',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🎯 Active Users')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache_data()
def get_data(query):
    if query == 'ETH_Users':
        return pd.read_csv('Data/Users/ETH_Data_USer_TX.csv')
    elif query == 'ETH_TX_Heatmap_After':
        return pd.read_csv('Data/Users/Heatmaps_after.csv')
    elif query == 'ETH_TX_Heatmap_Before':
        return pd.read_csv('Data/Users/HeatMap_Before.csv')
    return None


ETH_Users = get_data('ETH_Users')
ETH_TX_Heatmap_After = get_data('ETH_TX_Heatmap_After')
ETH_TX_Heatmap_Before = get_data('ETH_TX_Heatmap_Before')

df = ETH_Users
df2 = ETH_TX_Heatmap_After
df3 = ETH_TX_Heatmap_Before


#################################################################################################
st.write(""" ### Active Users On Ethereum ##  """)

st.write("""
Active users in the Ethereum network refer to individuals or entities who engage in transactions on the Ethereum blockchain within a certain period. These users interact with the Ethereum network by sending or receiving Ethereum tokens or interacting with smart contracts deployed on the network.
Transactions on the Ethereum blockchain can include a wide range of activities, such as buying and selling cryptocurrencies, participating in initial coin offerings (ICOs), transferring digital assets, and executing smart contracts.
The number of active users on the Ethereum network is an important metric to track because it reflects the level of adoption and usage of the network. The more active users there are on the network, the more valuable and useful the Ethereum blockchain becomes.
Active users can be measured using different metrics, such as daily active addresses, daily transaction volume, or unique wallets interacting with decentralized applications (DApps) on the Ethereum network.
  """)


st.info(""" ##### In This Employment Rates Section you can find: ####

* Active Users Before and After Shanghai Update
* Active Users Activity Pattern Before And After Upgrade





""")


#################################################################################################

st.write(""" ## Active Users Before and After Shanghai Update
""")

st.write(""" The conflict began in 2014, and since then, it has escalated into a full-blown military and diplomatic crisis, affecting many countries around the world.
One way that the Russia-Ukraine War has affected the employment rate in the United States is through the imposition of economic sanctions. In response to Russia's actions in Ukraine, the United States and the European Union imposed a series of economic sanctions on Russia. These sanctions have targeted key sectors of the Russian economy, such as energy, finance, and defense.
Numerous American businesses who conduct business with Russia have been harmed as a result of these restrictions. For instance, businesses that export items to Russia have experienced a sharp fall in sales, which has resulted in the loss of jobs in some sectors. Employer possibilities have decreased as a result of the impact on businesses that rely on Russian imports. Yet, these circumstances had no impact on the growth of the US labor force, which, as you can see, was unaffected by the conflict and continued to increase gradually beyond February 2022.

""")
# Employment Rate In the Unite State Before and After War
fig = px.bar(df, x="DATE", y="NUMBER_OF_USERS", color="STATUS",
             title='Daily Numner of Active Users Before and After Shanghai Update')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of Users')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

#####################################################
st.write(""" ## Active Users Activity Pattern Before And After Upgrade
""")

c1, c2 = st.columns(2)

with c2:
    # User per minute on hour of day (UTC)
    fig = px.density_heatmap(df2, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="User per minute on hour of day (UTC)",
                             histfunc='avg', title="User per minute on hour of day (UTC)".title(), nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
        'dtick': 1}, coloraxis_colorbar=dict(title="User per minute on hour of day (UTC)"))
    fig.update_yaxes(categoryorder='array')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


with c1:

    # User per minute on hour of day (UTC)
    fig = px.density_heatmap(df3, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="User per minute on hour of day (UTC)",
                             histfunc='avg', title="User per minute on hour of day (UTC)".title(), nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
        'dtick': 1}, coloraxis_colorbar=dict(title="User per minute on hour of day (UTC)"))
    fig.update_yaxes(categoryorder='array')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


##########################################################################


st.text(" \n")

st.info(""" #### SnowFlake Query: #### """)

st.image(Image.open('Images/SQL_Transactions.jpg'))
