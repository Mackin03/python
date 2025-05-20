#insert your purchasing budget

balance = 23316.02


print("balance: ", balance)

#parameters
lot_size = float(input("lot size: " ))
stock_price = float(input("stock price: "))

price_per_lot = stock_price * lot_size
print("price per lot: ", price_per_lot)

max_buy = (balance // price_per_lot) * lot_size
print("max buy quantity: " , max_buy)

max_buy_price = (max_buy * stock_price)
print("max buy price: ", round(max_buy_price,2))

remaining_balance = balance - max_buy_price
print("remaining balance: ", round(remaining_balance, 2))



    
