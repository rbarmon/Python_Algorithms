# Week 10

"""
Algorithm 63 Cuckoo hashing: Lookup
1: function LOOKUP(k)
2:      if T1[f (k)].key = k then return T1[f (k)]
3:      if T2[g (k)].key = k then return T2[g (k)]
4:      return null
"""

"""
Algorithm 64 Cuckoo hashing: Deletion
1: function DELETE(item)
2: if T1[f (item.key)] = item then T1[f (item.key)] = null
3: else if T2 [g (item.key)] = item then T2[g (item.key)] = null
"""

"""
Algorithm 65 Cuckoo hashing: Insertion
1: function INSERT(item)
2: if not LOOKUP(item.key) then // Ignore if the key is already present
3:      for i = 1 to MaxLoop do
4:          swap(item, T1[f (item.key)])
5:          if item = null then return
6:          swap(item, T2[g (item.key)])
7:          if item = null then return
8:      REHASH() // Resize and start from scratch
9:      INSERT(item) // Try again
"""

if __name__ == '__main__':
    pass