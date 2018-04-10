# Genome-scale Algorithms Week 10 — exercises

## BWT search

What is the worst-case running time for the BWT/Suffix-tree based approach for approximation pattern matching, i.e. how long does it take to find all positions where the pattern matches within within a given distance k? Think about what the size of the k-distance cloud of a string is, i.e. the number of strings within a certain distance k from a given string. Can you give a tighter bound or determine cases where the BWT/Suffix-tree approach is faster than explicitly searching for all strings in the k-distance cloud?

Consider algorithm 7.41 in the textbook, which contains an optimisation of the algorithm. Do exercises 7.9.10 and 7.9.11

## K-mer matching

This is an open-ended exercise, so be inventive.

Assume we want to build an approximative pattern matching based on k-mers. Then, we would split our pattern, of length *n* into *m = n/k* k-mers, where we will assume we have chosen *k* such that *k* divides *n*. Let's further assume that we do exact matching on the k-mers and get *m* lists of positions back, such that list *j* contains the positions where k-mere *j*, i.e. `pattern[k*j:((k+1)*j + 1]`, matches.

Derive an algorithm that takes these lists as input as well as a distance, *d*, and output sequences of indices (*k<sub>j</sub>*,*i<sub>j</sub>*) where *k<sub>j</sub>* denotes a k-mer index and *i<sub>j</sub>* an index where k-mer *k<sub>j</sub>* matches, and where *k<sub>j</sub>* - *k<sub>j-1</sub>* < *d* and *i<sub>j</sub>* - *i<sub>j-1</sub>* < *d* - *k<sub>j</sub>* - *k<sub>j-1</sub>*, i.e. a list of sequences that can potentially be made into an approximative match to the pattern with no more than *d* edits (potentially because we do not know how many edits there are in k-mers that are left out).

For extra fun: implement your algorithm and test it using one of your exact pattern matching implementations.

For extra fun: how would you go about translating such a sequence of k-mer matchings into a local alignment, i.e. produce a hit position and a CIGAR you could output in a SAM file?
