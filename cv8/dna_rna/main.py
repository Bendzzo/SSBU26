from Bio import SeqIO
from Bio.Seq import Seq, UndefinedSequenceError
from random import randint, choice

# Task 1: Load sequence from a file in the inputs directory
def load_sequence(filepath):
    records = SeqIO.parse(filepath, "genbank")
    for record in records:
        print(record.id)

        try:
            seq_str = str(record.seq)
            if seq_str:
                print(seq_str)
            else:
                print("No sequence found.")
                record.seq = Seq("")

        except UndefinedSequenceError:
            print("No sequence found.")
            record.seq = Seq("")

    return record

# Task 2: Create complementary strand
def create_complementary_strand(dna_sequence):
    """
    Pseudocode:
    - Create a translation table for DNA base complements (A <-> T, G <-> C).
    - Translate the input DNA sequence using the complement table.
    - Print the complementary strand.
    - Return the complementary strand.
    """
    trans_table = str.maketrans('ATCG', 'TAGC')

    dna_complement = str(dna_sequence.translate(trans_table))
    print(dna_complement)

    return dna_complement
# Task 3: Create gene mutation
def mutate(dna):
    """
    Pseudocode:
    - Convert the DNA sequence into a list of characters.
    - Perform 1000 random mutations:
        - Select a random index in the DNA sequence.
        - Replace the base at the selected index with a random different base.
    - Join the mutated list back into a string.
    - Print the mutated DNA sequence.
    - Return the mutated DNA sequence.
    """
    dna_list = list(dna)


    for i in range(1000):
        nahodny_index = randint(0, len(dna) - 1)


        aktualna_baza = dna_list[nahodny_index]
        vsetky_bazy = "ACGT"

        mozne_bazy = vsetky_bazy.replace(aktualna_baza, "")
        nahodny_base = choice(mozne_bazy)

        dna_list[nahodny_index] = nahodny_base

    mutated_dna = "".join(dna_list)
    print(mutated_dna)

    return mutated_dna

# Task 4: Calculate GC content
def calculate_gc_content(dna_sequence):
    """
    Pseudocode:
    - Count the occurrences of 'G' and 'C' in the DNA sequence.
    - Calculate the GC content as a percentage of the total sequence length.
    - Print the GC content percentage.
    - Return the GC content percentage.
    """
    if not dna_sequence or len(dna_sequence) == 0:
        return 0.0

    dna_sequence = Seq(dna_sequence)
    dna_sequence = dna_sequence.upper()

    gc_count = dna_sequence.count("G") + dna_sequence.count("C")
    gc_percentage = (gc_count / len(dna_sequence)) * 100
    print(f"GC content: {gc_percentage:.2f}%")
    return gc_percentage

# Example usage
if __name__ == "__main__":
    # Task 1: Load sequence from the inputs directory
    sequence_record = load_sequence("inputs/NC_005816.gb")

    # Task 2: Create complementary strand
    print('Complementary strand:')
    create_complementary_strand("TACCGGAT")

    # Task 3: Mutate a sequence loaded from the inputs directory
    # with open('inputs/AE017046.1.fasta', 'r') as file:
    #     contents = file.read()
    #     print("Fasta AE017046.1:", contents)

    fasta_sequence = SeqIO.read("inputs/AE017046.1.fasta", "fasta").seq
    print('mutated_dna:')
    mutated_sequence = mutate(str(fasta_sequence))

    # Task 4: Calculate GC content
    calculate_gc_content(str(fasta_sequence))