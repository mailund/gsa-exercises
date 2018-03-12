# Genome-scale Algorithms Week 7 — exercises

## Discuss Project 2

At the exercises we will discuss the results as described in the project description.

## Branching occurrences of tandem repeats

Recall the definition of a branching occurrence of a tandem repeat.

How many occurrences of branching tandem repeats can there be in a
string of length *n*? Can you give an example of a string that
contains the worst case number of occurrences of branching tandem
repeats?

## Finding all occurrences of branching tandem repeats

Recall the algorithm for finding all occurrences of branching tandem
repeats in a string of length *n* in time O(*n* log *n*).

What is the best case running time of this algorithm? Explain
and give an example of best case input?

What is the worst case running time? Explain and give an example of
worst case input?

## Finding all occurrenes of non-branching tandem repeats

Recall how any occurrence of a non-branching tandem repeat (*i*, *l*,
2) is a left-rotation of another occurrence of a tandem repeat (*i*+1,
*l*, 2).

Show that an occurrence of a branching tandem repeat (*i*, *l*,
2) is not a left-rotation of another occurrence of a tandem repeat (*i*+1,
*l*, 2).

An occurrence of a branching tandem (*i*, *l*, 2) thus starts a chain
of 0 or more occurrences of non-branching tandem repeats (*i*-1, *l*,
2), ..., (*i-k*, *l*, 2). Write the pseudo-code for a function that
given an occurrence of a branching tandem repeat (*i*, *l*, 2) finds
all *k* ≥ 0 occurrences of non-branching tandem repeats in this chain
in time O(*k*).

What is the worst case running time of running this function for all
branching occurrences of tandem repeats in a string of *n*? Why?

## Depth-first numbering

Recall how depth-first numbering of the leaves in the suffix tree T(*S*) is
used in the algorithm for finding all occurrences of branching tandem
repeats in a string *S* of length *n*.

Explain how we can make a table DF in time O(*n*) suchthat we can look
up the depth-fist number DF(*l*) of leaf *l* in time O(1).

Let rDF be the reverse, i.e. *l* = rDF(DF(*l*). Explain how to compute
rDF in time O(*n*).

Think about how DF and DF can be used to implement the algorithm without an
explicit representation of the leaf-lest *LL*(*v*).
