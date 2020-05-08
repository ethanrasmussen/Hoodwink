# Hoodwink
###### Current Version: 0.4.5
###### [Click here for PyPI page!](https://pypi.org/project/Hoodwink/)
A simple Python package for snatching basic stock information from Robinhood. Please note that in the current iteration, Hoodwink may return values which are slightly delayed. This is due to it not requiring log-in information. There are plans to implement log-in functionality in the future to guarantee real-time data, as well as adding options data to Hoodwink.


## Usage:

#### After installing Hoodwink from PyPI, you can import it using:
```
from hoodwink import hoodwink
```
#### To begin using Hoodwink, you'll need to declare a HoodwinkDriver, like this:
```
CHROMEDRIVER_PATH = "assets\chromedriver.exe"
hw = hoodwink.HoodwinkDriver(CHROMEDRIVER_PATH)
```

## HoodwinkDriver Functions:

### getFullName(ticker):
* ###### Parameters: 'ticker' = String value of stock/security ticker symbol
* #### Returns: String value of the security's full name

### getDescription(ticker):
* ###### Parameters: 'ticker' = String value of stock/security ticker symbol
* #### Returns: String value describing the security

### getCollections(ticker):
* ###### Parameters: 'ticker' = String value of stock/security ticker symbol
* #### Returns: List of URL's for collections containing the referenced stock/security

### getOwnerCount(ticker):
* ###### Parameters: 'ticker' = String value of stock/security ticker symbol
* #### Returns: Integer value of total owners of stock/security on Robinhood

### getPrice(ticker):
* ###### Parameters: 'ticker' = String value of stock/security ticker symbol
* #### Returns: Float value of current price (in USD)

### getPercentChange(ticker, period):
* ###### Parameters: 'ticker' = String value of stock/security ticker symbol, 'period' = String value representing time-period for change
* ###### Possible Values for Period: 'daily', 'weekly', 'monthly', '3-month', 'annual', '5-year'
* #### Returns: Float value of percentage change in price during period (ex. 1.56% will be returned as 1.56, not 0.0156)

### getNumericChange(ticker, period):
* ###### Parameters: 'ticker' = String value of stock/security ticker symbol, 'period' = String value representing time-period for change
* ###### Possible Values for Period: 'daily', 'weekly', 'monthly', '3-month', 'annual', '5-year'
* #### Returns: Float value of numeric price change during period (in USD)

### getMarketCap(ticker):
* ###### Parameters: 'ticker' = String value of stock/security ticker symbol
* #### Returns: String value representing the market cap of the stock/security

### getOpen(ticker):
* ###### Parameters: 'ticker' = String value of stock/security ticker symbol
* #### Returns: Float value of the open price of the stock/security

### getHigh(ticker, period):
* ###### Parameters: 'ticker' = String value of stock/security ticker symbol, 'period' = String value representing time-period for change
* ###### Possible Values for Period: 'daily', 'annual'
* #### Returns: Float value of the high of the stock/security during the given period

### getLow(ticker, period):
* ###### Parameters: 'ticker' = String value of stock/security ticker symbol, 'period' = String value representing time-period for change
* ###### Possible Values for Period: 'daily', 'annual'
* #### Returns: Float value of the low of the stock/security during the given period

### getPE(ticker):
* ###### Parameters: 'ticker' = String value of stock/security ticker symbol
* #### Returns: Float value of the P/E ratio of the stock/security

### getDivYield(ticker):
* ###### Parameters: 'ticker' = String value of stock/security ticker symbol
* #### Returns: Float value of the dividend yield of the stock/security

