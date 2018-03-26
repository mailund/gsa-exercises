
def recurse(hits, k, d, table_idx, i, matches, acc):
    """Recursively collect strings of k-mers."""
    if d < 0:
        return

    if table_idx >= len(hits):
        matches.append(acc)
        return

    for edits in range(0,+d + 1):
        j = k + edits
        if i + j in hits[table_idx]:
            recurse(hits, k, d-edits, table_idx + 1, i + j,
                    matches, acc+[(table_idx,i+j)])

def merge_kmer_hits(hits, k, d):
    """Extracts the strings of k-mers that probably less than edit
    distance d from a match."""
    matches = []
    for skip in range(d + 1):
        for i in hits[skip]:
            recurse(hits, k, d, skip+1, i, matches, [(skip,i)])
    return matches

def find_kmer_hits(str, kmer):
    """Get all the indices where `kmer` can be found in `str`."""
    index = -1
    hits = []
    while True:
        index = str.find(kmer, index + 1)
        if index == -1:
            break  # All occurrences have been found
        hits.append(index)
    return hits

def k_map(str, pat, k, d):
    """Locates the k-mers in `pat` in `str` and tries to combine them."""
    n = len(pat)
    assert n % k == 0
    m = n // k

    kmers = [pat[i:(i+k)] for i in range(m)]
    hits = [find_kmer_hits(str, kmer) for kmer in kmers]
    hits_sets = [set(h) for h in hits]

    print(hits_sets)

    return merge_kmer_hits(hits, k, d)

if __name__ == "__main__":

    str = "accacagggataccattc"
    pat = "acac"
    k = 2
    d = 1

    print (k_map(str, pat, k, d))
