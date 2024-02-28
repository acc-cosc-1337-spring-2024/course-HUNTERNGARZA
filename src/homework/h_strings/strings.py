def get_hamming_distance(dna1: str, dna2: str):
    hamming_distance = 0

    for i in range(len(dna1)):
        dna1_symbol: str = dna1[i]
        dna2_symbol: str = dna2[i]

        if dna1_symbol != dna2_symbol:
            hamming_distance += 1
    
    return hamming_distance


def get_dna_complement(dna: str) -> str:
    reversed_dna = "".join(reversed(dna))

    def f(x):
        if x == "A":
            return "T"
        elif x == "T":
            return "A"
        elif x == "C":
            return "G"
        return "C"

    reversed_complement: map[str] = map(f, reversed_dna)

    return "".join(reversed_complement)
