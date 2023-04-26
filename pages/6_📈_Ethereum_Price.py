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
st.set_page_config(page_title=' Ethereum Price - Ethereum After Shanghai Update',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('📈 Ethereum Price')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache_data()
def get_data(query):
    if query == 'Bitcoin_Daily':
        return pd.read_csv('Data/Crypto/Bitcoin_Daily.csv')
    elif query == 'Bitcoin_Weekly':
        return pd.read_csv('Data/Crypto/Bitcoin_Weekly.csv')
    elif query == 'Eth_Daily':
        return pd.read_csv('Data/Crypto/Eth_Daily.csv')
    elif query == 'Eth_Weekly':
        return pd.read_csv('Data/Crypto/Eth_Weekly.csv')
    return None


Bitcoin_Daily = get_data('Bitcoin_Daily')
Bitcoin_Weekly = get_data('Bitcoin_Weekly')
Eth_Daily = get_data('Eth_Daily')
Eth_Weekly = get_data('Eth_Weekly')


df = Bitcoin_Daily
df2 = Bitcoin_Weekly
df5 = Eth_Daily
df6 = Eth_Weekly


#################################################################################################
st.write(""" ### Shanghai Upgrade Impact on Ethereum Price  ##  """)

st.write("""
 One such upgrade that has been the focus of much attention in the Ethereum community is the upcoming transition to Ethereum 2.0, which is expected to improve the scalability and security of the network, as well as introduce new features and functionality.
Given Shanghai's importance in the world of cryptocurrency and blockchain, it is widely believed that any advancements or developments in the city could have a ripple effect on the entire industry, including the price of Ethereum. As such, many investors and traders are closely monitoring the situation in Shanghai, looking for any signs that could signal a major shift in the market.
Of course, it's impossible to predict with certainty how any particular event or development will impact the price of Ethereum or any other cryptocurrency. However, with so much focus on Shanghai and its potential impact on the industry, it's clear that the city will continue to play an important role in shaping the future of blockchain and cryptocurrency.
  """)


st.info(""" ##### In This Ethereum Price Section you can find: ####

* Ethereum Price Hit a New High in 2023
* Price Prediction – Can ETH Hit An All-Time High in 2023?  
* ETH/BTC Index

The Data provided in this section scraped from [Yahoo finacial crypto section](https://finance.yahoo.com/crypto/)

""")


#####################################################
st.write(""" ## Ethereum Price Hit a New High in 2023 """)

st.write("""  Ether (ETH) is seeing a slight decline after reaching its highest level in a little under eight months on Wednesday in the mid-\$1,900s, and was most recently trading in the mid-\$1,800s.
According to TradingView, the second-most valuable cryptocurrency in the world by market capitalization, which runs the Ethereum blockchain, the most popular smart-contract platform in the world, is down little more than 2% for the day.    
However, the cryptocurrency's short-term technical prognosis remains favorable. The 21-Day Moving Average of Ethereum (ETH) has recently provided some dependable support, and all of its other significant moving averages are rising sequentially.
The fact that ETH is currently finding good support in the mid-\$1,800 range has encouraged hope that a short-term increase in price toward the highs slightly around \$2,000 in August 2022 is still very likely.
Additionally, the 14-Day Relative Strength Index (RSI) for ETH does not yet appear to be overbought, indicating a decreased chance of short-term profit-taking.   

 """)
# ETH Daily chart
fig = px.line(df5, x="Date", y="Open", color="Statues",
              title='ETH Daily Chart before and After Shanghai Upgrade')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='ETH Index')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# ETH Daily chart
fig = px.bar(df5, x="Date", y="Volume", color="Statues",
             title='ETH Daily Volume before and After Shanghai Upgrade')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='ETH Volume')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

################################################################################################################

st.write(""" ## Price Prediction – Can ETH Hit An All-Time High in 2023? """)
st.write(""" Many believe that even if ETH did fall after the Shapella upgrade, the decline would be minimal.
Last month, ETH experienced a significant bounce from its 200DMA, which is a powerful medium-term bullish indication.
Another encouraging development for ETH's medium-term technical outlook is the "golden cross" in early February, which occurs when the 50-Day Moving Average crosses above the 200-Day Moving Average.    
Additionally, economic tailwinds continue to provide strong support for the crypto markets, such as predictions that the Fed will lower interest rates later this year to prevent a bank crisis and recession.
The medium-to-long term outlook for ETH is undoubtedly optimistic, but predicting that the cryptocurrency will hit all-time highs this year is another matter.
In order for ether to reach new all-time highs this year, a 160% increase from present levels would be necessary.
The crypto market, however, is this. Since its lows in the \$800s last year, ETH has already increased by more than 100%.
Additionally, Ether increased by 600% between the months of November 2020 and April 2021.
Thus, a 160% rise this year shouldn't be completely discounted.
""")

# ETH Daily chart
fig = px.area(df5, x="Date", y="Open", color="Statues",
              title='ETH Price Trend before and After Shanghai Upgrade')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='ETH Index')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

######################################################

st.write(""" ##   ETH/BTC Index """)

st.write(""" The ETH/BTC index is a measure of the relative value of Ethereum (ETH) and Bitcoin (BTC), two of the largest and most widely traded cryptocurrencies in the world. This index is used by traders, investors, and analysts to track the performance of the ETH/BTC pair and make informed decisions about their investments in these cryptocurrencies.
The ETH/BTC index is calculated by comparing the prices of ETH and BTC in a given market, typically using a weighted average based on trading volumes. This provides a single number that represents the value of ETH relative to BTC, allowing traders to easily compare the performance of these two cryptocurrencies over time.
One of the key benefits of the ETH/BTC index is that it allows traders to take advantage of arbitrage opportunities between these two cryptocurrencies. For example, if the index shows that ETH is significantly undervalued relative to BTC, a trader could buy ETH and sell BTC, potentially profiting from the price difference between the two cryptocurrencies.
Overall, the ETH/BTC index is an important tool for anyone looking to invest in or trade cryptocurrencies. By providing a clear and objective measure of the relative value of ETH and BTC, this index can help traders make informed decisions and maximize their returns in the volatile and rapidly evolving world of cryptocurrency trading.
""")
# Bitcoin Daily chart
fig = px.line(df, x="Date", y="Open", color="Statues",
              title='Bitcoin Daily Chart before and After Shanghai Upgrade')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Bitcoin Index')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Bitcoin Daily chart
fig = px.bar(df, x="Date", y="Volume", color="Statues",
             title='Bitcoin Daily Volume before and After Shanghai Upgrade')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Bitcoin Volume')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


############################################################################
