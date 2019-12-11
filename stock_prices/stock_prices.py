#!/usr/bin/python

import argparse

def find_max_profit(prices):
  current_min_price_so_far = None
  min_price_index = None
  max_profit_so_far = None

  for p in range(0, len(prices)):
    if current_min_price_so_far != None and prices[p] < current_min_price_so_far and p != len(prices) - 1:
      current_min_price_so_far = prices[p]
      min_price_index = p
    elif current_min_price_so_far == None:
      current_min_price_so_far = prices[p]
      min_price_index = p

  for i in range(min_price_index, len(prices) - 1):
    if max_profit_so_far == None and i != len(prices) - 1:
      #  i + 1 because the index points to the position of the current_min_price_so_far, we need to start checking profit at the next price in the index
      max_profit_so_far = prices[i + 1] - current_min_price_so_far
    elif prices[i] - current_min_price_so_far >= max_profit_so_far and i != len(prices) - 1:
      max_profit_so_far = prices[i] - current_min_price_so_far

  return max_profit_so_far
  # return prices[len(prices) - 1] - prices[min_price_index], 

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))