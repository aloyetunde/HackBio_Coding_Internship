#start coding... 
dna_sequences = ["ATGCGTAC", "GCTTAGCT", "CGTACGTA"]

for seq in dna_sequences:
    g_count = seq.count('G')
    c_count = seq.count('C')
    gc_content = ((g_count + c_count) / len(seq)) * 100
    print(f"GC content of {seq}: {gc_content:.3f}%")

#8: Example 3: Iterating Over a Dictionary
    gene_expression = {
    "BRCA1": 12.5,
    "TP53": 7.8,
    "MYC": 19.2
}

for gene, expression in gene_expression.items():
    print(f"Gene: {gene}, Expression Level: {expression}")



gene_expression = {
    "JAK2": 16.5,
    "KRAS": 9.8,
    "TP53": 10.2
}

for gene, expression in gene_expression.items():
    print(f"Gene: {gene}, Expression Level: {expression}")

sequences = ["ATG", "TGC", "CGA"]

for seq1 in sequences:
    for seq2 in sequences:
        if seq1 != seq2:
            print(f"Comparing {seq1} with {seq2}")

sequences = ["ATG", "TGC", "CGA"]

# Function to calculate Hamming distance between two sequences
def hamming_distance(seq1, seq2):
    # Ensure sequences are of equal length
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must be of equal length")
    # Count the number of differing positions
    return sum(1 for a, b in zip(seq1, seq2) if a != b)
# Iterate over each pair of sequences
for i in range(len(sequences)):
    for j in range(i + 1, len(sequences)):
        seq1 = sequences[i]
        seq2 = sequences[j]
        distance = hamming_distance(seq1, seq2)
        print(f"Hamming distance between {seq1} and {seq2}: {distance}")
        
#Understanding i and j in Nested Loops:
#i: Typically represents the loop counter for the outer loop.
#j: Typically represents the loop counter for the inner loop.

#Example 5: Using range() in For Loops
initial_population = 100
growth_rate = 1.05  # 5% growth per generation

for generation in range(1, 11):
    population = initial_population * (growth_rate ** generation)
    print(f"Generation {generation}: {population:.2f}")       

#Simulate population growth for 15 generations with an initial population of 200 and a growth rate of 1.03.
initial_population = 200
growth_rate = 1.03  # 3% growth per generation

for generation in range(1, 16):
    population = initial_population * (growth_rate ** generation)
    print(f"Generation {generation}: {population:.2f}") 
    
def gc_content(sequence):
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    gc_content_percentage = ((g_count + c_count) / len(sequence)) * 100
    return gc_content_percentage
    
##You can call this function with a DNA sequence as an argument:
dna_sequence = "ATGCGTAC"
gc = gc_content(dna_sequence)
print(f"GC content of {dna_sequence}: {gc:.2f}%")

#Based on the last slide, write a function to calculate the AT content of a DNA sequence.
def AT_content(sequence):
    A_count = sequence.count('A')
    T_count = sequence.count('T')
    AT_content_percentage = ((A_count + T_count) / len(sequence)) * 100
    return AT_content_percentage

DNA_sequence = "ACGTAGTAGTACCATGGTATTAGCATTGAAC"
AT = AT_content(DNA_sequence)
print(f"AT content of {DNA_sequence}: {AT:.2f}%")


# Create a dictionary to map codons to amino acids
codon_table = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
    'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
}
def translate_dna(dna_sequence):
    """
    Translates a DNA sequence into a protein sequence.

    Parameters:
    dna_sequence (str): The DNA sequence to be translated.

    Returns:
    str: The resulting protein sequence.
    """
    protein_sequence = ""
    # Loop through the DNA sequence in steps of three letters
    for i in range(0, len(dna_sequence) - 2, 3):
        # Get the current codon
        codon = dna_sequence[i:i+3]
        # Find the corresponding amino acid
        amino_acid = codon_dict.get(codon, 'X')  # 'X' means unknown codon
        if amino_acid == '_':  # Stop translation if stop codon is found
            break
        # Add the amino acid to the protein sequence
        protein_sequence += amino_acid
    return protein_sequence

# Sample DNA sequence
dna_sequence = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"

# Translate the DNA sequence into a protein sequence
protein_sequence = translate_dna(dna_sequence)

# Print the results
print("DNA Sequence    : ", dna_sequence)
print("Protein Sequence: ", protein_sequence)

