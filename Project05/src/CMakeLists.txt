
cmake_minimum_required(VERSION 3.2.0)
set(CMAKE_C_STANDARD 11)

project(GSA-readmap)
include(CTest)

add_library(stralg SHARED 
	buffer.h buffer.c 
	match.h match.c
	trie.h trie.c
	queue.h queue.c
	aho_corasick.h aho_corasick.c
	edit_distance_generator.h edit_distance_generator.c
	cigar.h cigar.c
	strings.h strings.c
	string_vector.h string_vector.c
	size_vector.h size_vector.c
	fasta.h fasta.c
	fastq.h fastq.c
	sam.h sam.c
	pair_stack.h pair_stack.c
	suffix_array.h suffix_array.c
)

add_executable(match_readmap match_readmap.c)
target_link_libraries(match_readmap stralg)

add_executable(ac_readmap ac_readmap.c)
target_link_libraries(ac_readmap stralg)

add_test(Read-mapping read_map_comparison_test.sh)
