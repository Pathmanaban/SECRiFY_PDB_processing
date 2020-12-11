########################
######## README ########
########################

# S. cerevisiae data:
# "Sc_resultstable_all.txt", "Sc_resultstable_enriched.txt" and "Sc_resultstable_depleted.txt" contains the data of 3 two-round expression screens of human (HEK293) cDNA fragments in S. cerevisiae. Sequencing data was mapped on a human GRCh38 transcriptome assembled using known transcripts from protein-coding genes only.
# all = all in-frame fragments detected in either the unsorted baseline library (merged for 3 replicates), or in all 3 sorted replicate samples
# enriched = those with log_FC > 1 in all three replicates (11625)
# depleted = those with log_FC < -1 in all three replicates (136531)

# For each fragment, the following information is provided:

# Ensembl_geneID --> Ensembl gene ID
# Ensembl_txID --> Ensembl transcript ID
# tx_start --> Transcript start position on human genome GRCh38
# tx_end --> Transcript end position on human genome GRCh38
# chr --> chromosome #
# gene_symbol --> official gene symbol
# frag_start --> fragment start position on the transcript, 0-based 
# frag_stop --> fragment end position on the transcript, 0-based
# cDNA --> DNA sequence of the fragment
# protein --> translated AA sequence of the fragment in frame 1
# IND_count --> raw count value in the baseline (unsorted) library (merged for 3 replicates), NAs replaced by 0.001
# SORT(1)_count --> raw count value in the sorted sample replicate (1), NAs replaced by 0.001
# IND_FPTM --> normalized FPTM value in the baseline (unsorted) library 
# SORT(1)_FPTM --> normalized FPTM value in the sorted sample replicate (1)
# logFC_(1) --> log2(SORT(1)_FPTM/IND_FPTM)


# P. pastoris data:
# "Pp_resultstable_all.txt", "Pp_resultstable_enriched.txt" and "Pp_resultstable_depleted.txt" contains the data of 3 single-round expression screens of human cDNA fragments in P. pastoris. Sequencing data was mapped on a human GRCh38 transcriptome assembled using known transcripts from protein-coding genes only.
# all = all in-frame fragments detected in either the unsorted baseline library (merged for 3 replicates), or in all 3 sorted replicate samples
# enriched = those with log_FC > 1 in all three replicates (10404)
# depleted = those with log_FC < -1 in all three replicates (141357)
# the table has the same organization as for the S. cerevisiae data, but the replicates are labeled 3/4/5 instead of 1/2/3 here.

