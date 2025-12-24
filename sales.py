import pandas as pd

print("Program Started")

df = pd.read_csv("sales_data.csv")
print("Data Loaded Successfully")

print(df.head())

# Monthly sales
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.month

monthly_sales = df.groupby('Month')['Sales'].sum()

print("Monthly Sales:")
print(monthly_sales)

# Import matplotlib only when needed and handle initialization errors to avoid hangs
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    ax = monthly_sales.plot()
    plt.title("Monthly Sales Trend")
    plt.savefig("monthly_sales.png")
    print("Plot saved to monthly_sales.png")
except Exception as e:
    print("Plotting skipped due to matplotlib error:", e)
