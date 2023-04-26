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
st.set_page_config(page_title='Miners - Ethereum After Shanghai Update',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('⛏️ Miners ')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache_data()
def get_data(query):
    if query == 'ETH_Miners':
        return pd.read_csv('Data/Miners/ETH_miner.csv')
    elif query == 'ETH_Miners':
        return pd.read_csv('Data/Miners/ETH_miner.csv')
    return None


ETH_Miners = get_data('ETH_Miners')


df = ETH_Miners

#################################################################################################
st.write(""" ### Ethereum Miners after Proof of Stake ##  """)

st.write(""" Ethereum miners are individuals or groups who participate in the process of verifying transactions and adding new blocks to the Ethereum blockchain. They are responsible for maintaining the security and integrity of the network, as well as earning rewards for their efforts.
Miners use powerful computers to solve complex mathematical algorithms and validate transactions on the Ethereum blockchain. This process is known as proof of work (PoW), and it requires a significant amount of computational power to complete successfully.
In exchange for their work, miners are rewarded with a certain amount of Ether (ETH), the native cryptocurrency of the Ethereum network. This reward serves as an incentive for miners to continue supporting the network and ensuring its reliability.
However, Ethereum is planning to shift from proof of work to proof of stake (PoS), a more energy-efficient and less computationally intensive consensus mechanism. Under PoS, instead of miners, users who hold a certain amount of ETH can participate in the process of validating transactions and adding new blocks to the blockchain.
Overall, Ethereum miners play a crucial role in maintaining the security and decentralization of the network. However, with the planned shift to PoS, their role is likely to change significantly in the future.


  """)


st.info(""" ##### In This Miner Section you can find: ####

* Can You Still Mine Ethereum?
* Ethereum Miners after Proof of Stake [Imact of Ukraine War]




""")
#########################################################################
st.write(""" ## Can You Still Mine Ethereum?  """)

st.write(""" If you’re considering Ethereum mining, keep in mind that it’s no longer possible to get into the game. This is a result of a pivotal time of foundation-level blockchain transition from Ethereum to what many refer to as Ethereum 2.0. 
It’s not just a name change. 
Known simply as “the merge,” the transition has transformed how the Ethereum blockchain operates, how it’s maintained and how tokens are generated.   
On Sept. 15, NextAdvisor reported that “the Ethereum merge is complete.” Two days later, the Ethereum blockchain converted from a proof-of-work (PoW) consensus mechanism to a proof-of-stake (PoS) consensus mechanism. 
The merge replaced Ethereum miners with validators who maintain the network by staking Ether (ETH). The change was necessitated by the unsustainable energy requirements that are inherent to traditional blockchain mining. The shift to PoS greatly improves energy efficiency by using investor capital locked up in validating nodes to validate transactions instead of the energy-hogging hardware that the mining trade relied on to function.[[3]](https://www.nasdaq.com/articles/can-you-still-mine-ethereum-after-the-merge)
    """)

#################################################################################################
st.write(""" ## Ethereum Miners after Ukraine War  """)

st.write("""  Ethereum, the second-largest cryptocurrency by market capitalization, has been affected by the conflict in several ways. One of the most significant impacts of the war on Ethereum is the disruption of the crypto mining industry. Ukraine is home to many large mining farms, and these facilities have been targeted by Russian-backed separatists, leading to power outages and damage to mining equipment. This has resulted in a significant reduction in the hashrate of the Ethereum network, making it more difficult for miners to earn rewards.       
Furthermore, the conflict has also led to increased scrutiny of the cryptocurrency industry by governments and regulatory bodies. Many countries are concerned about the potential for cryptocurrencies to be used for illicit activities, including trading illicit military equipment, funding terrorism, and money laundering. As a result, there has been a push for stricter regulations and greater oversight of the industry.    
The war has also had a psychological impact on the cryptocurrency market, with many investors becoming more risk-averse and opting to invest in more traditional assets such as gold and stocks. This has led to a decline in the value of Ethereum and other cryptocurrencies.
Despite the challenges posed by the conflict, there are also some positive developments for Ethereum. Some experts predict that the geopolitical tensions could drive greater adoption of cryptocurrencies in Ukraine, as citizens look for alternative ways to store their wealth and protect themselves from economic instability.
In addition, Ethereum's underlying technology, blockchain, has the potential to be used for humanitarian purposes in conflict zones. For example, blockchain can be used to distribute aid and resources more efficiently, providing transparency and accountability in a region where corruption is rampant.
The impact of the Ukraine-Russia conflict on Ethereum and the wider cryptocurrency industry is complex and multifaceted. While the conflict has presented significant challenges, it has also highlighted the potential of blockchain technology to drive positive change in the world.[Extracted From Writer Ukraine War Impact Dashboard](https://kaizen-step-ru-the-impact-of-the-russia-ukraine-conflict-nfpw8h.streamlit.app/) https://kaizen-step-ru-the-impact-of-the-russia-ukraine-conflict-nfpw8h.streamlit.app/
    """)

# Daily Number of Distinct Miners Before and After Shanghai Update
fig = px.bar(df, x="DATE", y="NUMBER_OF_MINERS", color="STATUS",
             title='Daily Number of Distinct Miners Before and After Shanghai Update')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Daily Number of Miners')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Daily Number of Distinct Miners Before and After Shanghai Update
fig = px.area(df, x="DATE", y="DAILY_BLOCK", color="STATUS",
              title='Daily Block Before and After Shanghai Update')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Daily Block')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


#####################################################

st.text(" \n")

st.info(""" #### SnowFlake Query: #### """)

st.image(Image.open('Images/SQL_Miners.jpg'))
