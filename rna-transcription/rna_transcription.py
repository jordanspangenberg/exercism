def to_rna(dna_strand):
    complement = {'G': 'C',
                  'C': 'G',
                  'T': 'A',
                  'A': 'U'}
    return ''.join([complement[c] for c in dna_strand])
