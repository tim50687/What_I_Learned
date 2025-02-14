# Dynamic Programming


> Sometimes, we need to use two or more 1D arrays to store the states of the problem. Becuase some state might depend on other arrays.

## 790. Domino and Tromino Tiling

> Three 1 d array DP

## 714. Best Time to Buy and Sell Stock with Transaction Fee *

- At day i, you can either buy, sell or do nothing.
    - If you buy stock, the total profit is `dp[i-1] - prices[i]`
    - If you sell stock, the total profit is `dp[i-1] + prices[i] + fee`
    - If you do nothing, the total profit is `dp[i-1]`
    - The maximum of the three is the max profit at day i.

- However
    - If you want to buy stoick at day i, you must sell stock before day i.
    - If you want to sell stock at day i, you must buy stock before day i.
    
- Therefore, we need two states of dp array: `hold` and `not_hold`
    - `hold[i]` is the maximum profit at day i when you hold a stock.
    - `not_hold[i]` is the maximum profit at day i when you don't hold a stock.