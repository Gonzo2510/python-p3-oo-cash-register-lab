#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0.0
    self.items = []
    self.price_history = []
    self.quantity_history = []


  def add_item(self, item, price, quantity=1):
    self.quantity_history.append(quantity)
    for i in range(quantity):
      self.items.append(item)
      self.price_history.append(price)
      self.total += price

  def apply_discount(self):
    if self.discount == 0:
      print('There is no discount to apply.')
    else:
      self.total = self.total - (self.total * self.discount / 100)
      print(f"After the discount, the total comes to ${int(self.total)}.")

  def void_last_transaction(self):
    if self.quantity_history[-1] > 1:
      for i in range(self.quantity_history[-1]):
        self.total -= self.price_history[-1]
      self.quantity_history.pop()
      self.items.pop()
      self.price_history.pop()

    else:
      self.total -= self.price_history[-1]
      self.items.pop()
      self.price_history.pop()
      self.quantity_history.pop()
      

# test = CashRegister(20)
# print(test.discount)