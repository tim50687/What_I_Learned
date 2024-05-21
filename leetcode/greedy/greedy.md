# Greedy 

## Fractional Knapsack Problem

### Step 1

#### How to prove divide and conquer?

- The optimal solution for the problem is the `combination of the optimal solutions for the subproblems`.

- Using `fraction knapsack` as an example. Say you have `a, b, c, d` items in the knapsack, limit is `100 lb`.

- Assuming God given solution(`We use this solution to infer the possible structure of the sub-problem`). We have 10 lb of `a` item, 20 lb of `b` item, 30 lb of `c` item, and 40 lb of `d` item.

- Now, we can make it into sub-problems.
    - We cut the `a` portion from the solution, apart from the rest of the items(`b, c, d`).

    - We have two sub-problems now. `Can we get the optimal solution for the sub-problems?`
        - We know the solution for `a` part sub-problem.
        - What is the optimal solution for 10 lb of only `a` item?
            - We can get the answer from question.

    - Now, what about the optimal solution for `b, c, d` items?
        - For 90lb, and `b, c, d` items, can we get the optimal solution?
        - `Here, use logic to prove`. `There must be a optimal solution for it`. Say if not, so that you can find a better solution for this part of the sub-problem. But, this is not possible. Because if you combine with the `a` part, you will get a better solution. It's `contradictory`. Therefore, there must exist an optimal solution for this part of the sub-problem.


## 55. Jump Game

- Use DP bottom up, Dp array meaning if you can reach the end from that index.
    - loop through backwards
        - For each element, loop through again to see if you can reach any `TRUE` element from that index.

> However, while you are marking TRUE, this means that if you can get to that index, you can reach the end. So, you can update the current goal to that index. So we can have a variable to update `current goal`, and see if your max step can `greater or equal than` the current goal.
- Greedy approach (`I think it's more like DP optimization`).
    - We will have a current goal, which is the last index.
    - loop through backwards, if you can reach the current goal from that index, update the current goal to that index.


## 881. Boats to Save People

Max is 2, if the heaviest person can't fit with the lightest person, then the heaviest person can not fit with anyone else, which means we need to use a boat for the heaviest person. So, we can use `two pointers` to solve this problem.