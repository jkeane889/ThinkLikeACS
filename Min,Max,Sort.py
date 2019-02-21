stocks = {
    'GOOG': 520.23,
    'FB': 76.45,
    'YHOO': 39.28,
    'AMZN': 300.21,
    'AAPL': 99.56
}

print(min(zip(stocks.values(), stocks.keys())))
print(max(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.keys(), stocks.values())))
