# Day 10: Factory

## Problem Summary

**Part 1:** Toggle indicator lights using XOR operations. Find minimum button presses.

**Part 2:** Increment counters to reach target joltage levels. Find minimum button presses.

## Solution Approach

### Part 1: XOR Combinations
Each button toggles specific lights. Try all combinations of buttons (each pressed 0 or 1 times) and find the smallest set that reaches the target state.

### Part 2: Integer Linear Programming (ILP)

This is a classic optimization problem:
- **Variables:** `x[i]` = number of times to press button `i`
- **Objective:** Minimize `x[0] + x[1] + ... + x[n]`
- **Constraints:** Each counter must reach its target

#### Example

For `{3,5,4,7}` with buttons `(3) (1,3) (2) (2,3) (0,2) (0,1)`:

```
Minimize: x₀ + x₁ + x₂ + x₃ + x₄ + x₅

Subject to:
  x₄ + x₅ = 3           (counter 0)
  x₁ + x₅ = 5           (counter 1)
  x₂ + x₃ + x₄ = 4      (counter 2)
  x₀ + x₁ + x₃ = 7      (counter 3)

  All x ≥ 0, integer
```

#### Why ILP?

Brute force is too slow - some buttons can be pressed 200+ times, creating a massive search space.

ILP solvers use smart algorithms:

**Branch and Bound:**
1. Solve allowing decimals (fast)
2. Branch: try rounding up/down
3. Bound: skip branches that can't improve the best solution found

**Cutting Planes:**
- Add constraints that eliminate decimal solutions without removing valid integer ones

## Dependencies

```
scipy  # for milp solver
```
