def reason(df):
    df["Reason"]="Wait"
    df.loc[df["Signal"]=="BUY","Reason"]="Because: MA50 > MA200 & MACD > signal line"
    df.loc[df["Signal"]=="SELL","Reason"]="Because: MA50 < MA200 & MACD < signal line"
    
    return df