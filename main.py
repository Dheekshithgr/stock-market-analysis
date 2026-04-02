from src.fetch_data import *
from src.indicators import *
from src.stratergy import *
from src.backtest import *
from src.visualization import *



while True:
    ticker = input("Enter ticker: ").strip().upper()
    period = input("Enter period: ").strip()
    initial_balance=float(input("Enter initial balance (₹): ") or 10000)
    df = fetch_stock_data(ticker, period)

    if df is not None:
        break

    print("Try again.\n")
    
    
df = add_moving_averages(df)

df = add_rsi(df)

df=add_macd(df)

df = df.dropna(subset=['MA50', 'MA200', 'RSI'])

df=df.reset_index(drop=True)

df = generate_strategy(df)

full_analysis_plot(df)

latest = df.iloc[-1]

price = latest['Close']
signal = latest['Signal']

print("\n===== TODAY'S DECISION =====")
print(f"Price: {price}")

if signal == "BUY":
    print("📈 Suggestion: Consider BUYING today")
elif signal == "SELL":
    print("📉 Suggestion: Consider SELLING today")
else:
    print("⏳ Suggestion: HOLD (no action)")

final_value=backtest(df,initial_balance)

print(f"\nFinal Value: {final_value}")

print("\n===== STRATEGY SUMMARY =====")

print(f"Total BUY signals: {(df['Signal'] == 'BUY').sum()}")
print(f"Total SELL signals: {(df['Signal'] == 'SELL').sum()}")
print(f"Total HOLD signals: {(df['Signal'] == 'HOLD').sum()}")

save_data(df,ticker)