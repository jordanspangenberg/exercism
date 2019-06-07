'''
Codon 	            Protein
AUG 	            Methionine
UUU, UUC 	        Phenylalanine
UUA, UUG 	        Leucine
UCU, UCC, UCA, UCG 	Serine
UAU, UAC 	        Tyrosine
UGU, UGC 	        Cysteine
UGG 	            Tryptophan
UAA, UAG, UGA 	    STOP
'''
def proteins(strand):
    d = {'AUG': 'Methionine', 'UUU': 'Phenylalanine',
        'UUC': 'Phenylalanine', 'UUA': 'Leucine', 'UUG': 'Leucine',
        'UCG': 'Serine', 'UCA': 'Serine', 'UCC': 'Serine', 'UCU': 'Serine',
        'UAU': 'Tyrosine', 'UAC': 'Tyrosine',  'UGU': 'Cysteine', 'UGC': 'Cysteine',
        'UGG': 'Tryptophan', 'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP',
    }
    protein = []
    for codon in [strand[i:i+3] for i in range(0, len(strand), 3)]:
        if (d[codon] is not 'STOP'):
            protein.append(d[codon])
        else:
            return protein
    return protein
