def backtest(df, initial_balance):
    balance = initial_balance
    shares = 0
    position = "NONE"

    for i in range(len(df)):
        price = df.iloc[i]["Close"]
        signal = df.iloc[i]["Signal"]

        if signal == "BUY" and position == "NONE":
            shares = balance / price
            balance = 0
            position = "HOLD"

        elif signal == "SELL" and position == "HOLD":
            balance = shares * price
            shares = 0
            position = "NONE"

    final_value = balance + (shares * df.iloc[-1]["Close"])
    return final_value