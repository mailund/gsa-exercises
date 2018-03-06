# Genome-scale Algorithms Week 6 — exercises

## Building a suffix trie

With the code we have for building a trie from week 4, it should be relatively easy to build a suffix trie. If you used boolean string labels, change them to integer labels again—we know that there will be no duplicated strings. We also know that only leaves will have a label, so if you want, you can also exploit that, but at least the leaves need to contain an index.

Instead of having characters associated with edges, use an index into the string. This doesn’t change the complexity, but it is closer in spirit to suffix trees.

Modify your trie code to do this.

## Building a suffix tree from a suffix array

Prove that successive indices when you move along a non-branching path in the suffix trie differ by exactly one. That is, if you take a sequence of non-branching nodes in trie, you get an interval of indices into your string.

To build a suffix tree from a suffix trie, you simply have to compress paths. If your nodes contain both a from and to index you can start out with your initial trie and simply identify non-branching paths and replace them with a single node consisting of the same interval as the path.

Try implementing this.

What is the complexity of this algorithm?

## Using a suffix tree for exact pattern matching

Say that we want to find the occurrences of a pattern (of length m) in text (of length n), and that we know that the pattern occurs at least once. Using a suffix tree we can solve this problem in worst case time O(m + z), where z is the number of occurrences, but can it be done faster in the best case since we know that the pattern occurs at least once in the text?

## Using a suffix tree for counting the number of non-overlapping occurrences of pattern

Using a suffix tree for a text (of length n), we can easily count the number of occurrences of a pattern (of length m) in the text in time O(m). How fast can you count the maximal number of non-overlapping occurrences of a pattern (of length m) in the text?

## Suffix links

Recall the definition of a suffix link from the lecture. Show that if u is a node in a suffix tree, then the suffix link, s(u), is also a node.
