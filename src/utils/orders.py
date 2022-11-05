from binance.cm_futures import CMFutures
import pandas as pd
import numpy as np
import requests
from utils.util import Helper

class Order(Helper):
    def __init__(self,
                 type,
                 limit_price,
                 limit_stop,
                 leverage):
        self.type = type
        self.limit_price = limit_price
        self.limit_stop = limit_stop
        self.leverage = leverage
        self.calculated_difference = abs(limit_price - limit_stop) / limit_price
        
    def assess_and_send_order(self):
        if self.type == "buy":
            self.send_order_buy(self.limit_price, self.limit_stop, self.leverage, self.calculated_difference)

        elif self.type == "sell":
            self.send_order_sell(self.limit_price, self.limit_stop)
        
    def send_order_buy(self, 
                       limit_price, 
                       limit_stop, 
                       leverage, 
                       calculated_difference):
        pass

    def send_order_sell(self, 
                        limit_price, 
                        limit_stop, 
                        leverage, 
                        calculated_difference):
        pass

