import strings

while True:
    user_input: str = input("""1-Hamming Distance
2-Dna Complement
3-Exit
""")

    user_input = int(user_input)

    if user_input == 1:
        s = input("dna1: ")
        s2 = input("dna2: ")
        out = strings.get_hamming_distance(s, s2)
        print(out)
    
    elif user_input == 2:
        s = input("dna: ")
        out = strings.get_dna_complement(s)
        print(out)
    
    else:
        break

