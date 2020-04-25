#import/dependencies
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

#NOTE: data may be slightly delayed in current version of Hoodwink, as logging-in is not yet supported!

#webdriver options
chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(executable_path="assets\chromedriver.exe", options=chrome_options)

#get full name from ticker symbol
def getFullName(ticker):
    try:
        browser.get("https://robinhood.com/stocks/"+ticker)
        return browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/header/h1").text
    except:
        raise Exception("ERROR: Couldn't get full name.")
    browser.close()

#get description
def getDescription(ticker):
    try:
        browser.get("https://robinhood.com/stocks/"+ticker)
        return browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[3]/div[1]/h3").text
    except:
        raise Exception("ERROR: Couldn't get description.")
    browser.close()

#get list of tags/collections
def getCollections(ticker):
    try:
        browser.get("https://robinhood.com/stocks/"+ticker)
        collections_div = browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[4]/div")
        collections_a_tags = collections_div.find_elements_by_tag_name('a')
        collections = []
        for a in collections_a_tags:
            try:
                collection = a.get_attribute('href')
                collections.append(collection)
            except:
                pass
        return collections
    except:
        raise Exception("ERROR: Couldn't get collections.")
    browser.close()
         

#get number of owners of stock on RH
def getOwnerCount(ticker):
    try:
        browser.get("https://robinhood.com/stocks/"+ticker)
        return int(browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/header/div/a/div/div/span/span/span").text.replace(',',''))
    except:
        raise Exception("ERROR: Couldn't get owner count.")
    browser.close()
    
#get current price
def getPrice(ticker):
    try:
        browser.get("https://robinhood.com/stocks/"+ticker)
        price = browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[2]/div/div[1]/div/div/div[1]/div[2]/span[2]").text
        return float(price[1:])
    except:
        raise Exception("ERROR: Couldn't get current price.")
    browser.close()

#get percentage change in price (periods: daily, weekly, monthly, 3-month, annual, 5-year)
def getPercentChange(ticker, period="daily"):
    try:
        browser.get("https://robinhood.com/stocks/"+ticker)
        if period == "daily" or period == "1d" or period == "today":
            change = browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[2]/span/span/span[2]").text
            change = change.replace('%','')
            change = change.replace('(','')
            change = change.replace(')','')
            return float(change)
        elif period == "weekly" or period == "1w" or period == "week":
            browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/nav/a[2]").click()
            time.sleep(0.5)
            change = browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[2]/span[1]/span/span[2]").text
            change = change.replace('%','')
            change = change.replace('(','')
            change = change.replace(')','')
            return float(change)
        elif period == "monthly" or period == "1m" or period == "1-month":
            browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/nav/a[3]").click()
            time.sleep(0.5)
            change = browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[2]/span[1]/span/span[2]").text
            change = change.replace('%','')
            change = change.replace('(','')
            change = change.replace(')','')
            return float(change)
        elif period == "3-month" or period == "3m":
            browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/nav/a[4]").click()
            time.sleep(0.5)
            change = browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[2]/span[1]/span/span[2]").text
            change = change.replace('%','')
            change = change.replace('(','')
            change = change.replace(')','')
            return float(change)
        elif period == "annual" or period == "year" or period == "1-year" or period == "1yr" or period == "yr":
            browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/nav/a[5]").click()
            time.sleep(0.5)
            change = browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[2]/span[1]/span/span[2]").text
            change = change.replace('%','')
            change = change.replace('(','')
            change = change.replace(')','')
            return float(change)
        elif period == "5-year" or period == "5yr":
            browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/nav/a[6]").click()
            time.sleep(0.5)
            change = browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[2]/span[1]/span/span[2]").text
            change = change.replace('%','')
            change = change.replace('(','')
            change = change.replace(')','')
            return float(change)
    except:
        raise Exception("ERROR: Couldn't get percentage price change.")
    browser.close()

#get numeric price change in USD (periods: daily, weekly, monthly, 3-month, annual, 5-year)
def getNumericChange(ticker, period="daily"):
    try:
        browser.get("https://robinhood.com/stocks/"+ticker)
        if period == "daily" or period == "1d" or period == "today":
            change = browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[2]/span[1]/span/span[1]").text
            change = change.replace('$','')
            return float(change)
        elif period == "weekly" or period == "1w" or period == "week":
            browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/nav/a[2]").click()
            time.sleep(0.75)
            change = browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[2]/span[1]/span/span[1]").text
            change = change.replace('$','')
            return float(change)
        elif period == "monthly" or period == "1m" or period == "1-month":
            browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/nav/a[3]").click()
            time.sleep(0.75)
            change = browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[2]/span[1]/span/span[1]").text
            change = change.replace('$','')
            return float(change)
        elif period == "3-month" or period == "3m":
            browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/nav/a[4]").click()
            time.sleep(0.75)
            change = browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[2]/span[1]/span/span[1]").text
            change = change.replace('$','')
            return float(change)
        elif period == "annual" or period == "year" or period == "1-year" or period == "1yr" or period == "yr":
            browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/nav/a[5]").click()
            time.sleep(0.75)
            change = browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[2]/span[1]/span/span[1]").text
            change = change.replace('$','')
            return float(change)
        elif period == "5-year" or period == "5yr":
            browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/nav/a[6]").click()
            time.sleep(0.75)
            change = browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[2]/span[1]/span/span[1]").text
            change = change.replace('$','')
            return float(change)
    except:
        raise Exception("ERROR: Couldn't get numeric price change.")
    browser.close()

#get market cap (AS STRING)
def getMarketCap(ticker):
    try:
        browser.get("https://robinhood.com/stocks/"+ticker)
        return browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[3]/div[2]/div[1]/div[3]").text
    except:
        raise Exception("ERROR: Couldn't get market cap.")
    browser.close()
        
#get today's open price (AS FLOAT IN USD)
def getOpen(ticker):
    try:
        browser.get("https://robinhood.com/stocks/"+ticker)
        return float(browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[3]/div[2]/div[7]/div[3]").text[1:])
    except:
        raise Exception("ERROR: Couldn't get open price.")
    browser.close()

#get high (periods: today, 52w)
def getHigh(ticker, period="today"):
    try:
        browser.get("https://robinhood.com/stocks/"+ticker)
        if period == "today" or period == "day" or period == "daily" or period == "1d":
            high = float(browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[3]/div[2]/div[5]/div[3]").text[1:])
        elif period == "52w" or period == "1yr" or period == "annual" or period == "year":
            high = float(browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[3]/div[2]/div[9]/div[3]").text[1:])
        return high
    except:
        raise Exception("ERROR: Couldn't get high for "+period+".")
    browser.close()

#get low (periods: today, 52w)
def getLow(ticker, period="today"):
    try:
        browser.get("https://robinhood.com/stocks/"+ticker)
        if period == "today" or period == "day" or period == "daily" or period == "1d":
            return float(browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[3]/div[2]/div[6]/div[3]").text[1:])
        if period == "52w" or period == "1yr" or period == "annual" or period == "year":
            return float(browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[3]/div[2]/div[10]/div[3]").text[1:])
    except:
        raise Exception("ERROR: Couldn't get low for "+period+".")
    browser.close()

#get P/E ratio
def getPE(ticker):
    try:
        browser.get("https://robinhood.com/stocks/"+ticker)
        return float(browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[3]/div[2]/div[2]/div[3]").text)
    except:
        raise Exception("ERROR: Couldn't get P/E ratio.")
    browser.close()

#get dividend yield
def getDivYield(ticker):
    try:
        browser.get("https://robinhood.com/stocks/"+ticker)
        return float(browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[3]/div[2]/div[3]/div[3]").text)
    except:
        raise Exception("ERROR: Couldn't get dividend yield.")
    browser.close()


ticker = "bac"
print("1D: $"+str(getNumericChange(ticker,"daily"))+" ("+str(getPercentChange(ticker,"daily"))+"%)")
print("1W: $"+str(getNumericChange(ticker,"weekly"))+" ("+str(getPercentChange(ticker,"weekly"))+"%)")
print("1M: $"+str(getNumericChange(ticker,"monthly"))+" ("+str(getPercentChange(ticker,"monthly"))+"%)")
print("3M: $"+str(getNumericChange(ticker,"3-month"))+" ("+str(getPercentChange(ticker,"3-month"))+"%)")
print("1Y: $"+str(getNumericChange(ticker,"annual"))+" ("+str(getPercentChange(ticker,"annual"))+"%)")
print("5Y: $"+str(getNumericChange(ticker,"5-year"))+" ("+str(getPercentChange(ticker,"5-year"))+"%)")

