Assumptions:

-input file contains corporate and government bonds listed in ascending order
of the term years, otherwise, it would make less sense to list bonds in a non-
chronological order of returns. 

-However, given I cannot assume the above, I would opt to sort it myself in the
code to allow for runtime of O(nlogn) using my modified binary search
 rather than the naive approach of o(n^2)

-Given assumption is that there is at least one government bond lower and one 
larger than any given corporate bond, and thus I can assume, that either there
are no bonds given as input or at least 2 or more

-Due to the previous assumption, I cover more than one edge case in my binary 
search algorithms


Given enough time, I would try to construct better automated test cases