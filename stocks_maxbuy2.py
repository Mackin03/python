
##### Insert Parameters #####
stock_code = "APX"
balance = 23316.02
lot_size = 100
stock_price = 6.11
#############################


class Stock:
    
    def __init__(self, stock_code: str, balance: float, lot_size: int, stock_price: float):
        self.stock_code = stock_code
        self.balance = balance
        self.lot_size = lot_size
        self.stock_price = stock_price
        
    @property
    def price_per_lot(self) -> float:
        #Total cost of one lot
        price_per_lot = self.lot_size * self.stock_price
        return price_per_lot
    
    @property    
    def max_buy(self) -> int:
        #Maximum number of shares you could buy based on the available balance
        max_buy = (self.balance // self.price_per_lot) * self.lot_size
        return max_buy
    
    @property
    def max_buy_price(self) -> float:
        #Total price if you buy the maximum shares
        max_buy_price = self.max_buy * self.stock_price
        return max_buy_price

    @property
    def remaining_balance(self) -> float:
        #Remaining balance after you buy the maximum shares
        remaining_balance = self.balance - self.max_buy_price
        return remaining_balance
    
    def print_stock_information(self) -> None:
        print(f"Stock Code:          {self.stock_code}")
        print(f"Stock Price:         {self.stock_price:.2f}")
        print(f"Lot Size:            {self.lot_size}")
        print(f"Price per Lot:       {self.price_per_lot:.2f}")
        print(f"Max Shares Amount:   {self.max_buy:.0f}")
        print(f"Total Amount Price:  {self.max_buy_price:.2f}")
        print(f"Remaining Balance:   {self.remaining_balance:.2f}")

stock_parameters = Stock(stock_code, balance, lot_size, stock_price)
stock_parameters.print_stock_information()