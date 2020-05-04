# Importing CryptoCurrency price data into python notebooks using the CryptoCompare API

Note: The code in this repo should be pip-installable and usable with a one-line import in iPython notebooks, per the following:

I read a blog post by Alex Galea (github: agalea91) in 2017 that gave a really simple overview of how to access data in jupyter notebooks from the CryptoCompare API.

Having read that, and having a crew of co-workers at the time who were incredibly bullish on just about all cryptos (right before the first major crash...) I decided to have some additional fun and see if I could package together repeatable calls to the API using his code, such that I could easily get a few types of data back at various resolutions in single-line commands.

It's been a while since I updated any of this code and it's likely to have bugs - I may work on ironing things soon...

Original blog post: https://medium.com/@galea/cryptocompare-api-quick-start-guide-ca4430a484d4
aglea91's "cryptocompare-api" repo: https://github.com/agalea91/cryptocompare-api


In your terminal:
clone this repo to your computer: git clone [remote for this repo]
install this repo as a package locally: python -m pip install [file path for this repo on your local computer]

In iPython notebook:
import getcryptoprices.getprices as getprices
df = getprices.[function call here]
