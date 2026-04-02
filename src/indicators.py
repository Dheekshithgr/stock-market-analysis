import pandas as pd


# Moving Average
def add_moving_averages(df):
    df['MA50'] = df['Close'].rolling(window=50).mean() #last 50 days
    df['MA200'] = df['Close'].rolling(window=200).mean() #last 200 days
    
    return df

#RSI
def add_rsi(df):
    df["delta"] = df["Close"].diff()
    df["gain"] = df["delta"].where(df["delta"]>0,0)
    df["loss"] = -df["delta"].where(df["delta"]<0,0)
    df["avg_gain"] = df["gain"].rolling(window=14).mean()
    df["avg_loss"] = df["loss"].rolling(window=14).mean()
    df["RS"] = df["avg_gain"] / df["avg_loss"]
    df["RSI"] = 100 - (100 / (1 + df["RS"]))

    return df

#MACD
def add_macd(df):
    df["EMA12"] = df["Close"].ewm(span=12,adjust=False).mean()
    df["EMA26"] = df["Close"].ewm(span=26,adjust=False).mean()
    
    df["MACD"]=df["EMA12"]-df["EMA26"]
    df["Signal_Line"] = df["MACD"].ewm(span=9, adjust=False).mean()
    
    return df

