# Project

TBA

## Control flow of a read-mapper

You can see the `main`-function of an exact pattern matching read-mapper I have written in C [here](https://github.com/mailund/gsa-exercises/blob/5c9342ce6129670ac0ec5fa4ffc47e25b21238b3/Project05/src/match_readmap.c#L129-L215).

1. [Read in the genome sequence from a FASTA file.](https://github.com/mailund/gsa-exercises/blob/5c9342ce6129670ac0ec5fa4ffc47e25b21238b3/Project05/src/match_readmap.c#L205)
2. [Scan through reads in a FASTQ file](https://github.com/mailund/gsa-exercises/blob/5c9342ce6129670ac0ec5fa4ffc47e25b21238b3/Project05/src/fastq.c#L10-L28)

     a. [For each read (or alternatively, each string a certain distance from the read)](https://github.com/mailund/gsa-exercises/blob/5c9342ce6129670ac0ec5fa4ffc47e25b21238b3/Project05/src/match_readmap.c#L108-L127)
     b. [Search for a match using an exact pattern matching algorithm](https://github.com/mailund/gsa-exercises/blob/5c9342ce6129670ac0ec5fa4ffc47e25b21238b3/Project05/src/match_readmap.c#L90-L105)
     c. [Output matches in SAM format](https://github.com/mailund/gsa-exercises/blob/5c9342ce6129670ac0ec5fa4ffc47e25b21238b3/Project05/src/match_readmap.c#L77-L88).
 
My implementation is a little convoluted because it uses call-backs to tie the different pieces together in a way where I can replace one algorithm with another at any step in the process. 