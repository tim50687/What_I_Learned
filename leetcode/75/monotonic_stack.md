# Monotonic stack

## 739 Daily Temperatures *

- Say we are at first temperature, if the following temperature is always higher, then it's easy.

- What about the next day is cold? We need to keep the day in some data structure.
    - Say we have 72, 71, 70 and the next day is 74. 
    - We know for 70 is 1 day, 71 is 2 days, 72 is 3 days. So it's Last In First Out (`Stack`).

- We use stack to store the cold days. If the next day is warmer, we pop the cold days and calculate the days.


## 901 Online Stock Span *

- If we loop backwards for every price, it will be very slow. O(n^2).

- Use example, say if we have 100, 80, 60, 70, 100, 75, 85
    - Curr price is 60.
    - If the next price is `smaller`, we know the span for next price is 1.
    - If the next price is `higher`, we need to check previous price x's span. 
        - If the next next price is higher, we konly check the previous's span, and we can just jump backwards `span` time. 
        - (`Thus here we know that if span of stock > 1, the stock less than or equal to the current stock can be ignored`)

- Thus, if you do this, 
    - sometimes you will have O(1) `next stock less than current stock`.
    - sometimes you will have O(n) `next stock higher than current stock`.

    - Time complexity is O(1) if amortized.