# Genome-scale Algorithms Week 7 — exercises

## Project 2

Hand in project 2. At the exercises we will discuss the results as described in the project description.

## Branching occurrences of tandem repeats

Recall the definition of a branching occurrence of a tandem repeat.

How many occurrences of branching tandem repeats can there be in a
string of length *n*? Can you give an example of a string that
contains the worst case number of occurrences of branching tandem
repeats?

## Finding all occurrences of branching tandem repeats

Recall the algorithm for finding all occurrences of branching tandem
repeats in a string of length *n* in time O(*n* log *n*),

What is the best case running time of this algorithm? Explain
and give an example of best case input?

What is the worst case running time? Explain and give an example of
worst case input?

## Finding all occurrenes of non-branching tandem repeats

Recall how any occurrence of a non-branching tandem repeat (*i*, *l*,
2) is a left-rotation of another occurrence of a tandem repeat (*i*+1,
*l*, 2).

Show that an occurrence of a branching tandem repeat (*i*, *l*,
2) is not a left rotation of another occurrence of a tandem repeat (*i*+1,
*l*, 2).

Write the pseudo-code for a function that given an occurrence of a branching tandem repeat (*i*, *l*,
2) in time O(*k*) finds all *k* ≥ 0 occurrences of tandem repeats that are the result of one
or more left rotations of this brancing occurrence. 

What is the worst case running time of running this function for all branching occurrences of tandem
repeats in a string of *n*? Why?

## Depth-first numbering

Recall how depth-first numbering of the leaves in the suffix tree are
used in the algorithm for finding all occurrences of branching tandem
repeats. Let DF(*l*) be the depth-first number of leaf *l*. Let *S* be
a string og length *n*. It is clear how we can make a table DF in time
O(*n*) by a depth-first travelse of the suffix tree T(*S*) in time
O(*n*) such that we can look-up DF(*l*) in time O(1). Let rDF be the
reverse, i.e. *l* = rDF(DF(*l*). Explain how to compute rDF in time
O(*n*). Think about how rDF can be used to implement the algorithm
without an explicit representation of the leaf-lest *LL*(*v*).
