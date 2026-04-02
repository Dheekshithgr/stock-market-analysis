def live_action(df):
    latest = df.iloc[-1]
    price=latest["Close"]
    signal = latest["Signal"] 