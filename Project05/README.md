# Project 5 — Read mapper

The final project of this class, as we have hinted at from day one, is the implementation of a read-mapper. We will not implement a fully-fledged read-mapper—this would require us to take read quality and map quality into account—but we will build all the string-algorithm steps in a mapper.

Since it is the final project, you have more freedom in how you approach the project, but the minimum requirement of your read mapper is: *Your read-mapper should be able to find either all or the best approximative match (at a given edit-distance) for all reads in a FASTAQ file.*



## Step 1: Control flow of a read-mapper

There are three basic steps your read-mapper should implement:

1. Read in the genomic sequence (from a FASTA file or an index structure you have created in a pre-processing step).
2. Scan through all reads (from a FASTQ file), searching for approximative matches.
3. Output matches (in the SAM format) for all reads that have an approximative match.

You can see the `main`-function of an exact pattern matching read-mapper I have written in C [here](https://github.com/mailund/gsa-exercises/blob/5c9342ce6129670ac0ec5fa4ffc47e25b21238b3/Project05/src/match_readmap.c#L129-L215).

I have implemented the steps like this:

1. [Read in the genome sequence from a FASTA file.](https://github.com/mailund/gsa-exercises/blob/5c9342ce6129670ac0ec5fa4ffc47e25b21238b3/Project05/src/match_readmap.c#L205)
2. [Scan through reads in a FASTQ file](https://github.com/mailund/gsa-exercises/blob/5c9342ce6129670ac0ec5fa4ffc47e25b21238b3/Project05/src/fastq.c#L10-L28)

     1. [For each read (or alternatively, each string a certain distance from the read)](https://github.com/mailund/gsa-exercises/blob/5c9342ce6129670ac0ec5fa4ffc47e25b21238b3/Project05/src/match_readmap.c#L108-L127)
     2. [Search for a match using an exact pattern matching algorithm](https://github.com/mailund/gsa-exercises/blob/5c9342ce6129670ac0ec5fa4ffc47e25b21238b3/Project05/src/match_readmap.c#L90-L105)
     3. [Output matches in SAM format](https://github.com/mailund/gsa-exercises/blob/5c9342ce6129670ac0ec5fa4ffc47e25b21238b3/Project05/src/match_readmap.c#L77-L88).
 
My implementation is a little convoluted because it uses call-backs to tie the different pieces together in a way where I can replace one algorithm with another at any step in the process. Different languages have different ways of enabling such flexibility—and C is particularly primitive in this regard—so choose something appropriate if you want this flexibility. Alternatively, just ignore this problem and implement one solution for each of the steps.

For completing this part of the project, you should be able to simply combine code you have written in the exercises and previous projects. You should [already have parsers for FASTA and FASTQ](https://github.com/mailund/gsa-exercises/tree/master/Week01); you have implemented [several](https://github.com/mailund/gsa-exercises/tree/master/Project01) [exact pattern-matching](https://github.com/mailund/gsa-exercises/tree/master/Project02) algorithms; you have code for [generating all strings at a given edit-distance from a core string](https://github.com/mailund/gsa-exercises/tree/master/Week02), and while you have not output matches in SAM format before, this should be manageable if you have a read, the CIGAR string describing an alignment, and the position of the match.

## Step 2: Approximate pattern matching

**FIXME:** Algorithm for approximate matching

## Step 3: Go-faster stripes

**FIXME:** competition aspect…


