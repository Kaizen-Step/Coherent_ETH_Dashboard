# Libraries
import streamlit as st
from PIL import Image

# Layout
st.set_page_config(page_title=' Ethereum After Shanghai Update',
                   page_icon=':bar_chart:📈', layout='wide')
st.title(' Ethereum After Shanghai Update ')
st.text(" \n")
# Content
c1, c2, c3 = st.columns(3)


with c1:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/Shanghai2.jpeg'))

with c2:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/Shanghai4.jpg'))
with c3:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/Shanghai3.jpeg'))


st.write("""


### Why Ethereum Shanghai Update (Shapella) Is Important ###  
Ethereum’s Shanghai upgrade, also commonly referred to as Shapella (we’ll explain why below), took place on April 12th.
It was a major upgrade following Ethereum’s transition to Proof-of-Stake (a.k.a The Merge), and it introduced a major mechanic change.
The upgrade consists of a few Ethereum Improvement Proposals (EIPs), although most of the focus is on one particular.
With that in mind, let’s take a closer look and understand why the Shanghai upgrade is so important. The Shanghai Upgrade transition is the network's next upgrade of the Ethereum mainnet. It primarily aims to transition to proof of stake, consequently allowing validators to finally withdraw their staked ETH both partially and fully.
This is a major improvement and will further incentivize the crypto community to shift towards ETH accelerating network participation. As of yet, the pre Shanghai testnet allows for both complete and partial validations to be withdrawn.
The upgrade also introduces Layer 2 fee reductions with the implementation of proto-danksharding aiding in the network's overall scalability and sustainability while also reducing gas fees. Moreover, the upgrade will also introduce EOF, separating code and data, which is significantly helpful for code validation.    
The release date of the Shanghai Upgrade is expected to be around March and April.However, there's no confirmation and developers agreed that this date may be pushed forward to as late as September 2023, especially with EIP-4844 (proto-danksharding) already being delayed to a March 2023 update.  [[1]](https://sensoriumxr.com/articles/375)    
      
### What is EIP-4895 in the Shanghai Upgrade? ###
While it’s currently running on PoS, Ethereum was using the proof-of-work consensus algorithm well before The Merge took place, But the plans to transition were in play for many years when developers created the so-called Beacon Chain.
The Beacon Chain was (and still is) secured by PoS. To maintain its integrity, allow it to function as intended, and carry out transactions and smart contracts, it needed validators – just like any other PoS-based blockchains where miners do not exist.
Therefore, those who wanted to partake in the future of the so-called Ethereum 2.0 were able to stake 32 ETH to secure the Beacon chain. The ETH was staked in the Beacon Depositor contract. Validators would then earn interest on their ETH – a reward for securing the network during this development stage.
The only catch? Well, they weren’t allowed to unstake their 32 ETH until a later, undetermined date. It’s taken years for the team to successfully deliver The Merge, and now, the Shanghai upgrade, through EIP-4895, finally allowed validators to unlock their ETH.
This guide is not intended as a technical walkthrough, so if you want to learn more about how the mechanic will become possible, please take a look at the official website page for EIP-4895.
In essence, the goal was to:
Introduce a system-level “operation” to support validator withdrawals that are “pushed” from the beacon chain to the EVM. These operations create unconditional balance increases to the specified recipients.
The Beacon depositor contract, as mentioned above, contained about 18 million ETH, which accounted for roughly 15% of the total circulating supply.
Validators are now free to withdraw, albeit with some considerations, their stake and do whatever they decide with it – it becomes entirely liquid. That made this particular EIP very important.[[2]](https://cryptopotato.com/what-is-the-ethereum-shanghai-shapella-upgrade-everything-you-need-to-know/)


""")


st.write("""
## Methodology ##  

We used Coherent Ethereum Raw Data Sets for our dashboard, which, as their name implies, only include hexadecimal raw data. Additionally, the block table's hexadecimal parameters were converted to integers using the Coherent Block Decoded Algorithm. The raw data tables only supply a limited number of columns and data, and the analyst did his best to develop dashboards that sound helpful and provide insight, which is quite difficult with a limited quantity of data and also takes a lot of time. Using the coherent "ETHEREUM_RAW_DATA.RAW.TRANSACTIONS" database and joining "DBT_DB.DEVELOPMENT.DECODED_BLOCKS," we first look into Ethereum transactions before and after the Shanghai upgrade, average gas usage, and hourly and weekly patterns. This table joins on block hashes because the number of columns for raw data is limited.   
Then, using the "Total_Difficulty" column of the raw data, we looked at the network difficulty, the situation of the ETH miners, and the effect of the Ukraine war on mining Ethereum. The number of users who are actively using Ethereum has been analyzed, as well as their hourly and daily activity patterns. The ETH price before and after Shanghai was examined to arrive at the final price.



""")


st.text(" \n")
st.write("""   
#### Sources ####  """)
st.write("""    1.https://sensoriumxr.com/articles/375   
        2.https://cryptopotato.com/what-is-the-ethereum-shanghai-shapella-upgrade-everything-you-need-to-know/    
        3. Image source:https://invezz.com/news/2023/04/10/ethereum-sees-spike-in-one-time-eth-depositors-ahead-of-shanghai-upgrade/

            """)


st.text(" \n")
c1, c2 = st.columns(2)
with c1:
    st.info(
        '**Twitter:  [Ludwig.1989](https://flipsidecrypto.xyz/)**', icon="🕊️")
    st.info(
        '**Project Supervisor:  [MetricsDao](https://github.com/Kaizen-Step/Russia_Ukraine_Conflict)**', icon="👨🏻‍💼")


with c2:
    st.info(
        '**Project Github:  [Ethereum After Shanghai Update](https://github.com/Kaizen-Step/Russia_Ukraine_Conflict)**', icon="💻")
    st.info(
        '**Data Set:  [Coherent Ethereum Raw Data Base](https://docs.coherent.xyz/coherent/getting-started/guide-for-ethereum-data)**', icon="🧠")
