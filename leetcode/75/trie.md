# Trie

- For each word inserting, we insert each char as a child of the previous char.
    - Mark end of word with a boolean.

- For each word searching, we see if the end of the word is marked.


## `Startwith` 
- This is the main reason to use Trie, because if we just want to search for word, we can use `hashset`.
- If we check `Startwith` on the list or set, we need to check every word in the list or set. But, with Trie, we can just check the first char and go down the tree `O(1)`.



## Implementation 

- For initialization
    - It's easier to use `dictionary` to represent the `children` of the node.
        - Because fast lookup and insertion. O(1)
    - We can also use `fixed size array`. But
        - Limit flexibility (`Cannot add more children than the size of the array`)
        - What if alphabet size is large but only sparsely populated? (`waste of space`)
    - We can also use `dynamic array` (list in python)
        - But, slow look up. `O(n)` for lookup.
        - For insertion, we need to check if the element is already in the list. `O(n)` for insertion.
        - But, it's more space efficient than fixed size array.

## Time complexity 

`w` is number of words, `l` is average length of the word.

### Create a trie 

- For each word, we push each char to the trie. `O(l)`, then we do this for `w` words. So, `O(wl)`

### Search a word

- We need to go through each char of the word. `O(l)`

### Search a prefix

- We need to go through each char of the prefix. `O(l)`

### Insert a word

- We need to go through each char of the word. `O(l)`

### Space complexity

- For each char, we need to store it as a node. So, `O(wl)`



## 1268. Search Suggestions System *