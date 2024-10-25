import heapq
class Solution:
  def minCostToConnectServers(self, x, y) -> int:

    points = []

    for i in range(len(x)):
      points.append((x[i], y[i]))

    def cal_diff(u1, u2, v1, v2):
      return min(abs(u1 - u2), abs(v1 - v2))
    
    heap = [ (0, points[0])]

    seen = set()

    ans = 0

    while heap:
      print(heap)
      print(seen)
      u = heapq.heappop(heap)

      if u[1] in seen:
        continue
      
      seen.add(u[1])
      ans += u[0]

      if len(seen) == len(x):
        return ans

      for i in points:
        if i not in seen:
          weight = cal_diff(u[1][0], i[0], u[1][1], i[1])
          heapq.heappush(heap, (weight, i))
        
a = Solution()

print(a.minCostToConnectServers([2, 4, 8],[6, 10, 9]))