def generate_strategy(df):
    df["Signal"]="HOLD"
    
    df.loc[(df['MA50'] > df['MA200']) & (df['RSI'] < 40) & (df['MACD'] > df['Signal_Line']),'Signal'] = "BUY"    #MA50<MA200 and RSI<40---> Indicates to buy
    df.loc[(df['MA50'] < df['MA200']) & (df['RSI'] > 60) & (df['MACD'] < df['Signal_Line']),'Signal'] = "SELL"   #MA50<MA200 and RSI>60---> Indicates to sell
    
    return df
