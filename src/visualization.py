import matplotlib.pyplot as plt

def full_analysis_plot(df):
    plt.figure(figsize=(12,10))

    # Price + MA
    plt.subplot(3,1,1)
    plt.plot(df['Close'], label='Price')
    plt.plot(df['MA50'], label='MA50')
    plt.plot(df['MA200'], label='MA200')

    # BUY markers
    buy_signals = df[df['Signal'] == 'BUY']
    plt.scatter(buy_signals.index, buy_signals['Close'], marker='^', label='BUY')

    # SELL markers
    sell_signals = df[df['Signal'] == 'SELL']
    plt.scatter(sell_signals.index, sell_signals['Close'], marker='v', label='SELL')

    plt.title("Price + Moving Averages + Signals")
    plt.legend()

    # RSI
    plt.subplot(3,1,2)
    plt.plot(df['RSI'], label='RSI')
    plt.axhline(70, linestyle='--')
    plt.axhline(30, linestyle='--')
    plt.title("RSI")
    plt.legend()

    # MACD
    plt.subplot(3,1,3)
    plt.plot(df['MACD'], label='MACD')
    plt.plot(df['Signal_Line'], label='Signal Line')
    plt.axhline(0, linestyle='--')
    plt.title("MACD")
    plt.legend()

    plt.tight_layout()
    plt.show()