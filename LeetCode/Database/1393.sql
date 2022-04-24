Select stock_name, Sum(If(operation = 'Sell', price, -price)) as capital_gain_loss
From Stocks
Group By stock_name;