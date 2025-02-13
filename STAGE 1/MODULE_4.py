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

#Functions with Default Parameters
def gc_content(sequence, uppercase=True):
    if not uppercase:
        sequence = sequence.upper()
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    gc_content_percentage = ((g_count + c_count) / len(sequence)) * 100
    return gc_content_percentage
##Call the function with and without converting to uppercase:

print(gc_content("atgcgtac", uppercase=False))
print(gc_content("ATGCGTAC"))
