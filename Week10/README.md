# Genome-scale Algorithms Week 10 — exercises

## Suffix-tree search

At the lecture, we saw an examplie of how to find all 1-mismatch matches of the pattern ATT in the text TATAT$ using a depth-first traversal of the suffix of TATAT$. Formulate how to adapt this approach to find matches of a  pattern p in a text x within a given edit distance k. Explain your procedure by showning how to find all matches of CT in TATAT$ within edit-distance 1. Compare your procedure to the one sketched on slides 27 in the lecture slides about BWT search for occurrences within a given edit distance.

## Running time of Suffix-tree and BWT search

What is the worst-case running time for the BWT/Suffix-tree search approach for approximation pattern matching, i.e. how long does it take to find all positions where the pattern matches within within a given edit distance *k*? Think about what the size of the "*k* edit distance" cloud of the pattern is, i.e. the number of strings within edit distance *k* from the pattern. Can you give a tighter bound, or determine cases where the BWT/Suffix-tree search approach is faster than explicitly searching for all strings in the "*k* edit distance" cloud (maybe using the Aho-Corasick approach)?

Consider algorithm 7.41 in the textbook, which contains an optimisation of the algorithm. Do exercises 7.9.10 and 7.9.11

## K-mer matching

This is an open-ended exercise, so be inventive.

Assume we want to build an approximative pattern matching based on k-mers. Then, we would split our pattern, of length *m* into *b = n/k* k-mers, where we will assume we have chosen *k* such that *k* divides *m*. Let's further assume that we do exact matching on the k-mers and get *b* lists of positions back, such that list *j* contains the positions where k-mere *j*, i.e. `pattern[k*j:((k+1)*j + 1]`, matches the text.

Derive an algorithm that takes these *b* lists as input as well as an edit distance, *d*, and output sequences of indices (*k<sub>j</sub>*,*i<sub>j</sub>*) where *k<sub>j</sub>* denotes a k-mer index and *i<sub>j</sub>* an index where k-mer *k<sub>j</sub>* matches, and where *k<sub>j</sub>* - *k<sub>j-1</sub>* < *d* and *i<sub>j</sub>* - *i<sub>j-1</sub>* < *d* - *k<sub>j</sub>* - *k<sub>j-1</sub>*, i.e. a list of sequences that can potentially be made into an approximative match to the pattern with no more than *d* edits (potentially because we do not know how many edits there are in k-mers that are left out).

For extra fun: implement your algorithm and test it using one of your exact pattern matching implementations.

For extra fun: how would you go about translating such a sequence of k-mer matchings into a local alignment, i.e. produce a hit position and a CIGAR you could output in a SAM file?
