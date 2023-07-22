# Week 11

"""
Algorithm 74 Naive suffix array construction
1: function SUFFIX_ARRAY(S[1..n])
2:      SA[1..n] = [1..n]
3:      sort(SA[1..n], SUFFIX_COMPARE(S,...)) // Use suffix_compare as the comparison operator
4:      return SA
5:
6: // Compare the suffixes at position i and j
7: function SUFFIX_COMPARE(S[1..n], i, j)
8:      return (S[i..n] < S[j..n])


Algorithm 75 Prefix-doubling suffix array construction
1: function SUFFIX_ARRAY(S[1..n])
2:      SA[1..n] = [1..n]
3:      rank[1..n] = [ord(S[1..n])]
4:      for k = 1 to n, stepping k ×= 2 do
5:          sort(SA[1..n], suffix_compare(rank, k, ...))
6:          // Update the rank array to account for the new sorted order
7:      temp[1..n] = 0
8:      for i = 1 to n − 1 do
9:          temp[SA[i+1]] = temp[SA[i]] + suffix_compare(rank[1..n], k, SA[i], SA[i + 1])
10:     swap(temp, rank)
11:     return SA
12:
13: // Compare the suffixes of length 2k beginning at positions i and j
14: function SUFFIX_COMPARE(rank[1..n], k, i, j)
15:     if rank[i] 6= rank[j] then // Compare by first halves
16:         return rank[i] < rank[j]
17:     else if i + k ≤ n and j + k ≤ n then // Compare by second halves
18:         return rank[i + k] < rank[j + k]
19:     else // Second half is empty
20:         return j < i

Algorithm 76 Suffix array: Pattern matching
1: function FIND_PATTERN(SA[1..n], T[1..n], P[1..m])
2:      // Binary search to find the first occurrence of P
3:      // Invariant: T[SA[lo]..n] < P and T[SA[hi]..n] ≥ P
4:      lo = 0, hi = n
5:      while lo < hi - 1 do
6:          mid = b(lo + hi)/2c
7:          if T[SA[mid]..n] < P[1..m] then
8:              lo = mid
9:          else
10:             hi = mid
11:     begin = hi
12:     // Binary search to find the final occurrence of P
13:     // Invariant: T[SA[lo]..n] ≤ P and T[SA[hi]..n] < P
14:     lo = 1, hi = n + 1
15:     while lo < hi - 1 do
16:         mid = b(lo + hi)/2c
17:         if T[SA[mid]..n] ≤ P[1..m] then
18:             lo = mid
19:         else
20:             hi = mid
21:     end = lo
22:     return begin, end
"""

if __name__ == '__main__':
    pass