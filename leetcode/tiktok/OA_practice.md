
# 210. Course Schedule II

Topo sort + queue

```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
            adj = [[] for _ in range(numCourses)]
            # create adjacent list to see the neighbors
            for edge in prerequisites:
                adj[edge[1]].append(edge[0]) # [[1]]
            # get the in degree array 
            in_degree = [0] * numCourses # [0, 0]
            for node in range(numCourses):
                for neighbor in adj[node]:
                    in_degree[neighbor] += 1 # [0, 0]
            # put in degree 0 to queue
            q = deque()
            for i in range(len(in_degree)):
                if in_degree[i] == 0:
                    q.append(i) # [0]
            # ans array
            ans = []
            # logic to put eleemnt in ans 
            while q: # [1]
                # pop the element from the queue
                curr = q.popleft()
                ans.append(curr)
                # find the neighbor
                for neighbor in adj[curr]:
                # remove in degree of the neighbors
                    in_degree[neighbor] -= 1

                    if in_degree[neighbor] == 0:
                        q.append(neighbor)

            # if length of ans == numsCourse
            if len(ans) == numCourses:
                return ans
                # return ans 

            # return []
            return []
```



## 2334. Subarray With Elements Greater Than Varying Threshold

1. In the subarray, if the `smallest element` is greater than or equal to the threshold, then the subarray will have all elements greater than or equal to the threshold.

2. So for each element in the array, we can find the left and right boundary for each element, where that element is the smallest element in the subarray.

2.5 First we assume every element is the smallest element in the subarray, so we set the left and right boundary to be the current index.

3. In order to get boundaries, we can use a monotonic stack to find the next smaller element on the left and right of the current element.

Why? because while building monotonic stack, when you reach the element that is smaller than top of the stack, you pop the stack until you find the element that is smaller than the current element. `And this is exactly what we want to find the left boundary of the current element.`

4. Same logic applies to the right boundary.

5. Once we have the left and right boundary, we can calculate the number of subarrays that have all elements greater than or equal to the threshold.

```python
class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        left = [i for i in range(len(nums))]
        right = [i for i in range(len(nums))]
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] >= nums[i]:
                left[i] = left[stack.pop()]
            stack.append(i)
        
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                right[i] = right[stack.pop()]
            stack.append(i)

        for i in range(len(nums)):
            n = right[i] - left[i] + 1
            if nums[i] > threshold / n:
                return n

        return -1
            
```

## TikTok Server Optimization

1. Create an array that store the next invalid end point for each start point. Why min? because say if 1 cannot go to 5, then 1 cannot go to 6, 7, 8, 9, 10, etc.

2. Loop through the possible end points. And then check `if` the next invalid end point is greater than the current end point. If it is, then we can increase the count. `Else`, that means you have to move the start point.

3. Count the segment that ends at the current end point.

Note: we can move start point, and never have to move it back is because say if 1 cannot go to 5, then 1 cannot go to 6, 7, 8, 9, 10, etc.


```python
class Solution:
  def optimizeTikTokRoutes(self, numServers: int, numDisconnectedPairs: int, disconnectedPairs: List[List[int]]) -> int:
      
      next_invalid = [numServers + 1] * (numServers + 1)

      for pair in disconnectedPairs:
          s = pair[0]
          e = pair[1]
          next_invalid[s] = min(next_invalid[s], e)

      good = 0

      start = 1

      for end in range(1, numServers + 1):

          while start < end and next_invalid[start] <= end:
              start += 1


          good += end - start + 1

      return good
```

## Tiktok Viral Challenge

```python
a = ord("a")
z = ord("z")
# z - a = 25
```

- Loop through the `end`

    - Check if current character is non viral, if so, increase the count of non viral character.

    - If non viral character is greater than `k`, then we have to move the start pointer.


    - Add the valid subarray to the answer.

```python

class Solution:
  def countViralCombinations(self, video: str, engagementArray: List[int], k: int) -> int:
      non_viral_count = 0
      n = len(video)
      ans = 0
      start = 0
      for end in range(n):
          if engagementArray[ord(video[end]) - ord('a')] == 0:
              non_viral_count += 1
          while non_viral_count > k:
              if engagementArray[ord(video[start]) - ord('a')] == 0:
                  non_viral_count -= 1
              start += 1
          ans += end - start + 1


      return ans 
```




## Optimize TikTok Reels Viewing

```python
def optimizeTikTokWatchTime(n, initialWatch, repeatWatch, m):
    # Step 1: Calculate the time for the first complete watch of each reel
    first_complete_watch_times = [initialWatch[i] + repeatWatch[i] for i in range(n)]
    
    # Step 2: Find the total time for the first complete watch of all reels
    min_first_watch_time = min(first_complete_watch_times)

    # Step 3: Sort the repeatWatch times in ascending order for the most efficient rewatchings
    repeat_watch_times = sorted(repeatWatch)

    # Step 4: If m > n, calculate how many rewatches are needed
    rewatch_count_needed = m - 1  # Subtract 1 because one reel is watched completely in step 2

    # Calculate the total time: add the smallest rewatch times for rewatch_count_needed viewings
    total_time = min_first_watch_time
    for i in range(rewatch_count_needed):
        total_time += repeat_watch_times[i]  # Select the smallest rewatch times
    
    return total_time
```


## TikTok Shopping Spree

- Use max heap to store the price of the items.

- Loop through the items and for the number of vouchers count, pop the max price from the heap and add the price to the answer.

```python
def getMinimumTotalCost( vouchersCount, prices) -> int:
    max_heap = [-price for price in prices]

    heapq.heapify(max_heap)

    while vouchersCount > 0:
        price = - heapq.heappop(max_heap)

        price = price // 2

        heapq.heappush(max_heap, -price)

        vouchersCount -= 1

    return -sum(max_heap)
      
```


## Viral Content Balancer

```python

def getMinimumOperations(content: str) -> int:
    # Step 1: Count the frequency of each character
    freq = Counter(content)
    frequencies = list(freq.values())
    
    # Step 2: Sort frequencies in descending order
    frequencies.sort(reverse=True)
    
    # Step 3: Calculate the target frequency
    total_length = len(content)
    unique_chars = len(frequencies)
    
    # Target frequency is the total length divided by the number of unique characters
    target_frequency = total_length // unique_chars
    remainder = total_length % unique_chars
    
    # Step 4: Calculate minimum operations
    operations = 0

    
    for f in frequencies:
        if remainder > 0:
            operations += abs(f - target_frequency - 1)

        else:
            operations += abs(f - target_frequency)

    return operations
```


## TikTok Credits Distribution Challenge

Use DP


```python
def canDistributeCredits(participants: int, credits: list) -> int:
    dp = [0] * participants

    if credits[0] % participants == 0:
        dp[0] = 1

    ans = 0
    prefix_sum = credits[0]
    for credit in range(1, len(credits)):
        prefix_sum += credits[credit]
        if prefix_sum % participants == 0:
            dp[credit] = dp[credit - 1] + 1
        else:
            dp[credit] = dp[credit - 1]
        
    # calculate the factorials of dp[len(credits) - 1]
    count = dp[len(credits) - 1]
    for i in range(1, count + 1):
        ans += comb(count, i)
    return ans
```


## Sort Social Media Feed

```python
def sortSocialMediaFeed(feed):
    # Split each entry into its components: timeStamp, userId, and post
    parsed_feed = [entry.split(",") for entry in feed]
    
    # Sort by userId (lexicographically) and then by timeStamp (numerically)
    sorted_feed = sorted(parsed_feed, key=lambda x: (x[1], int(x[0])))

    print(sorted_feed)
    
    # Join the sorted components back into the original format
    result = [",".join(entry) for entry in sorted_feed]
    
    return result
```


# Multiple choice

1. Handling High Concurrency in Web Server

Your web server at TikTok needs to handle a high number of concurrent connections efficiently.
Which server architecture would best support high concurrency?

Pick ONE option:

Multi-threaded server

Event-driven server (selected)

Forking server

Single-threaded server


> Event-driven server: This architecture is designed to handle multiple connections in an asynchronous, non-blocking way. It allows a single thread to manage many connections by using events or callbacks to respond when data is ready to be processed, which minimizes the overhead of creating and managing multiple threads or processes. This makes it ideal for high-concurrency scenarios, such as TikTok's web servers.


2. TikTok uses a binary search tree (BST) to store user IDs for quick access. Choose the correct pseudo-code to insert a new user ID, userID, into the BST.

```
if (root == null) { 
    root = newNode(userID); 
} else { 
    current = root; 
    while (true) { 
        if (userID < current.value) { 
            if (current.left == null) { 
                current.left = newNode(userID); 
                break; 
            } else { 
                current = current.left; 
            } 
        } else { 
            if (current.right == null) { 
                current.right = newNode(userID); 
                break; 
            } else { 
                current = current.right; 
            } 
        } 
    } 
}
```


3. TikTok Comment Moderation

```
if (target.prev != null) { target.prev.next = target.next; } if (target.next != null) { target.next.prev = target.prev; } target = null;
```


4. Scheduling in a High-Throughput Server

Correct Answer: Round Robin (RR)

Explanation:

Round Robin (RR): This scheduling algorithm gives each process a fixed time slice (quantum) in a cyclic order. It's well-suited for high-throughput servers because it ensures fairness and provides a quick response time to all concurrent requests. Each request gets a fair share of CPU time, preventing any single process from monopolizing the CPU, which is important for handling numerous concurrent requests.
Why other options are incorrect:

First-Come, First-Served (FCFS): In FCFS, processes are handled in the order they arrive. While simple, this can cause a problem known as the convoy effect, where longer tasks block shorter ones, leading to inefficient CPU utilization and increased response times.

Shortest Job Next (SJN): This algorithm selects the process with the shortest expected execution time. While it minimizes average waiting time, it requires knowledge of the future execution time, which is impractical for a high-throughput server handling diverse and dynamic requests. It also suffers from the starvation problem, where longer jobs may never get CPU time.

Multilevel Queue Scheduling: This scheduling algorithm partitions the processes into different queues based on priority, with different scheduling algorithms for each queue. While it can provide fine-grained control, it adds complexity and may lead to inefficiencies for dynamically fluctuating server loads. It’s more suitable for systems where processes have well-defined priority classes rather than high-throughput environments like TikTok’s.


5. Virtual Memory Management in a Resource-Intensive Application
Correct Answer: Multi-level paging
Explanation:

Multi-level paging: This strategy divides the page table into multiple levels, making it more efficient in handling large virtual address spaces. It reduces the memory overhead of storing large page tables and allows systems to efficiently manage virtual memory for large datasets, which is crucial for resource-intensive applications.
Why other options are incorrect:

Single-level paging: In single-level paging, a single page table maps virtual addresses to physical addresses. While simple, it’s inefficient for large address spaces because the page table can become very large, consuming significant memory.

Inverted page table: This strategy stores only one entry per physical page, rather than per virtual page. While it saves memory, it is slower for processes that require fast lookups, as it uses a hash-based approach for virtual-to-physical mapping. This could lead to performance issues for resource-intensive applications.

Segmentation with paging: This hybrid approach divides memory into segments, and each segment is paged. While it offers flexibility and can reduce fragmentation, it adds complexity and overhead in managing both segmentation and paging. It’s not as widely used in modern systems for virtual memory management as multi-level paging.


6. TikTok Video Playlist
Correct Answer:
pseudo
Copy code
current = head 
while current.next != null: 
    current = current.next 
current.next = newNode


7. Deadlock Prevention in Concurrent Systems
Correct Answer: Circular wait prevention


8. Disk Scheduling for Video Streaming Application
Correct Answer: Elevator (SCAN)
Explanation:
Elevator (SCAN): In this algorithm, the disk arm moves in one direction, servicing all requests along the way until it reaches the end, then reverses direction. This algorithm optimizes for high throughput and low latency by minimizing seek time, which is critical for a video streaming application where smooth, sequential data access is needed.


9. Inter-Process Communication in a Distributed System
Correct Answer: Message passing
Explanation:
Message passing is a widely used IPC mechanism in distributed systems where processes communicate by sending and receiving messages over a network. It is well-suited for distributed systems because it is scalable, and it abstracts away the underlying details of communication, allowing processes to communicate across different nodes.


10. TikTok File System
Correct Answer:
pseudo
Copy code
current = root 
for each char in filePath 
    if current.children[char] == null 
        current.children[char] = newNode() 
    current = current.children[char] 
current.isEnd = true


Here are the answers and explanations for each question:

---

### 1. **TikTok Video Title Manipulation**

- **Correct Answer**: 
  ```pseudo
  function trimSpaces(title):
      start = 0
      end = length(title) - 1
      while start <= end and title[start] == ' ':
          start = start + 1
      while end >= start and title[end] == ' ':
          end = end - 1
      return title[start:end + 1]
  ```

#### Explanation:
- This pseudo-code correctly trims leading and trailing spaces from the video title by using two pointers (`start` and `end`). It moves the `start` pointer forward to ignore leading spaces and moves the `end` pointer backward to ignore trailing spaces. Finally, it returns the substring of the title between `start` and `end + 1`.
  
#### Why other options are incorrect:
- **Option 1**: This code returns an incorrect substring range (`end - start + 1`), leading to off-by-one errors.
- **Option 2**: This relies on undefined functions `indexOfFirstNonSpace` and `indexOfLastNonSpace`.
- **Option 3**: This replaces **all** spaces in the title, not just leading and trailing spaces, which is not the correct behavior.

---

### 2. **TikTok Engagement Heatmap**

- **Correct Answer**:
  ```pseudo
  for i = 0 to 6
      totalEngagement = 0
      for j = 0 to 23
          totalEngagement = totalEngagement + engagements[i][j]
      print(totalEngagement)
  ```

#### Explanation:
- This pseudo-code correctly iterates over each day (`i` from 0 to 6) and sums the engagements for each hour (`j` from 0 to 23), printing the total engagement for each day.

#### Why other options are incorrect:
- **Option 2**: It calculates the total engagement for each hour across all days, not for each day.
- **Option 3 and 4**: These options subtract engagements instead of adding them, which is incorrect.

---

### 3. **TikTok Trending Videos**

- **Correct Answer**:
  ```pseudo
  if heap.size() < 10
      heap.insert(video)
  else if video.popularity > heap.peek().popularity
      heap.extractMin()
      heap.insert(video)
  ```

#### Explanation:
- This pseudo-code ensures the heap only contains the top 10 trending videos. If the heap size is less than 10, it inserts the video. If the heap is full, it checks if the new video's popularity is higher than the smallest element in the heap (which is at the top of a min-heap). If so, it removes the smallest element and inserts the new video.

#### Why other options are incorrect:
- **Option 2**: It inserts videos with **lower** popularity, which is incorrect since we want the top 10 videos by popularity.
- **Option 3**: It checks if the heap size is **greater than 10**, which is incorrect because we should ensure the heap size is **at most 10**.
- **Option 4**: This is the same as the correct option, so it’s redundant.

---

### 4. **TikTok Video Sorting**

- **Correct Answer**:
  ```pseudo
  function quickSort(arr, low, high)
      if low < high
          pi = partition(arr, low, high)
          quickSort(arr, low, pi - 1)
          quickSort(arr, pi + 1, high)

  function partition(arr, low, high)
      pivot = arr[high]
      i = low - 1
      for j = low to high - 1
          if arr[j].uploadTime <= pivot.uploadTime
              i = i + 1
              swap arr[i] and arr[j]
      swap arr[i + 1] and arr[high]
      return i + 1
  ```

#### Explanation:
- This pseudo-code implements the QuickSort algorithm to sort an array of videos based on their upload time. The `partition` function places the pivot element (last element in the array) in its correct position, with all smaller elements to its left and larger elements to its right. The `quickSort` function recursively sorts the subarrays.

#### Why other options are incorrect:
- There are no other options listed for this question, but the given pseudo-code is a correct implementation of QuickSort.

---

### 5. **TikTok Video Analytics**

- **Correct Answer**: **Counting the maximum consecutive ones in a binary array**

#### Explanation:
- This pseudo-code iterates through a binary array (`nums`), counting consecutive `1`s and keeping track of the maximum count (`maxCount`). Each time a `0` is encountered, it resets the count.

#### Why other options are incorrect:
- **Finding the maximum sum subarray**: This requires a different approach, like Kadane's algorithm, which tracks sums rather than counts of consecutive values.
- **Calculating the longest common subsequence in two arrays**: This involves comparing two arrays and requires dynamic programming.
- **Searching for the maximum element in an array**: This would involve a simple linear search for the maximum value, not counting consecutive `1`s.




## AI data set

```python

def minDaysToReachTarget(initialScore, targetScore, trainingScore):
    

    trainingScore.sort()
    seen = set()
    day = 0
    count = 0
    while initialScore < targetScore:
        if not trainingScore:
            return -1

        day += 1
        
        # use binary search to find the smallest element in the trainingScore that is greater than or equal to the day
        index = bisect.bisect_right(trainingScore, initialScore)
        if index != 0 and index - 1 not in seen:
            initialScore += trainingScore[index - 1]
            seen.add(index - 1)
        else:
            initialScore += day

        print(initialScore)
        count += 1

    return count

```

## Max gcd pairs

- Find hte max GCD possible from the array.

- Create a counter array for divisors, where len is max value in the array.

- GO through every element in the array and find the divisors of the element.

- Find if there is any element in the counter array that has more than 1.

```python
def findMaxGCD(arr, n):
    max_value = max(arr)
    
    counter = [0] * (max_value + 1)

    for num in arr:

        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                counter[i] += 1
                if i != num // i:
                    counter[num // i] += 1
        
    for i in range(max_value, 0, -1):
        if counter[i] > 1:
            return i

    return 1

```