# Intervals

- If you sorted by start time, if first one doesn't overlap with second one, then first one would not overlap with any other intervals.


## 452. Minimum Number of Arrows to Burst Balloons

- Sort it first.

- We know that if no overlap, we need to shoot an arrow.

- If there's overlap, we know we want to shoot an arrow within the overlap.
    - But, we want to keep checking if the next one overlaps with the current one.

- At the end, we + 1 for either last one is non-overlapping or the last overlapping one.
