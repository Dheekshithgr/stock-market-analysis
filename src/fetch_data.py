import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker,period):
    # valid_periods = ["1d","5d","1mo","3mo","6mo","1y","2y","5y","max"]
    # if period not in valid_periods:
    #     print("Invalid period! Using default = 1y")
    #     period = "1y"
        
    try:
        stock = yf.Ticker(ticker)
        df = pd.DataFrame(stock.history(period=period))
        
        if df.empty:
            print(f"Invalid ticker: {ticker}")
            return None
        
        df.reset_index(inplace=True) #Date(Index to actual column)
        df.dropna(inplace=True)
    
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def save_data(df, ticker):
    df['Date'] = df['Date'].dt.tz_localize(None)
    df.to_excel(f"Stock Market Analysis\data\{ticker}.xlsx", index=False)
    



