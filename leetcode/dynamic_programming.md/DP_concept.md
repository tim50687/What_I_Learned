# Dynamic Programming

## Steps to solve a DP problem

1. **Divide and Conquer**  
See if you can **Divide** problem into subproblems, solve subproblems, and combine (**Conquer**) the results.  
$$SOL(PB) = COMB(SOL(SPB))$$

> $\textcolor{red}{\text{God given answer!}}$ Can you break it down into subproblems, combine them, and then solve it?

> $\textcolor{red}{\text{Subproblem solutions must be combinable into the overall solution.}}$  


2. **(A)**  
   **Define the Objective in English & Write down the Recurrence**  
   $C[\text{PB input}] = COMB(C[\text{SPB input}])$

   **(B)**  
   **Problem <-> SubProblem, Dependency Visualization (Draw Table)**

> Usually, for `PB input`, $n$ variables will result in an $n-D$ array.

3. **Bottom-Up Computation**  

- Fill entire $C[ ]$ table in proper order given by step 2B.  
    - For $C[PB]$, the required $C[SPB]$ are already completed.

> $\textcolor{blue}{\text{Alternative: Memoization}}$

4. **Trace Solution**  
This is different from `Objective`.  
For example, for the Activity problem, `Objective` is to find max duration. To `Trace the solution` is to find which activity.

5. **Run Time/ Memory analysis**