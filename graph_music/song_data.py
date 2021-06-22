
from fractions import Fraction
# single beat (4 beats in a measure
b = 1
# half
h = 1/2
# thirds
t = Fraction(b, 3)
# two thirds
tt = 2 * t

jens_solo_arps = [
    ("0' 4' 7' 11' R", [tt, t, tt, t+b, b]), ("R 7' 4' 7' 7'", [tt, t, tt, t + b, b]),
    ("9' 6' R", [b + tt, t + b, b]), ("6' 2' 9' 6' 0'' 9' R",[tt, t, tt, t, tt, t, b]),

    ("5' 2' 9' 0'' 5'", [tt, t, tt, t + b, b]),
    ("2' 7 11 2' 5' 2' R", [tt, t, tt, t, tt, t, b]),
    ("4' 4' 4' 0'",  [b, tt, t + b, b]),
    ("11 7 11 2' 5' 2' R", [tt, t, tt, t, tt, t, b]),

    ("4' 0' R 4' R 4' R 4'",[tt, t, tt, t, tt, t, tt, t]), ("7' 4' 7' 7' R 11'", [tt, t, tt, t, 1 + tt, t]),
    ("0'' 0'' 9' R 9' 6'", [b, tt, t, tt, t, b]), ( "R 2' 2' 2' R",[ b, b, tt, t, b]),

    ("0'' 0'' 9' R 9' 5'", [b, tt, t, tt, t, b]),
    ("R 2' 11 5' 2' 11 7", [b, tt, t, tt, t, tt, t]),
    ("4' 0' R 4' 0' R", [tt, t, tt, t, b, b]),
    ("7' 4' 7' 10' R", [tt, t, tt, t + b, b]),
    
    ("R 9 0' 9 0' 9",[b, b, tt, t, tt, t]), ("5 9 0' 4' R",[tt, t, tt, t + b, b]), ( "R 0' 4' 0' R",[b, b, tt, t, b]), ("9 0' 5 R", [b, tt, t + b, b]),

    ("2' R 0'' 6' 9' 6'",[b, b, tt, t, tt, t]), ( "0'' 0'' 9' R",[b, tt, t + b, b]),
    ("9' R 9' 2' 5' 2'", [b, b, tt, t, tt, t]),
    ("11 11 2' R", [b, tt, t + b, b]),
    
    ("4' 0' 7' 0' R 4' 7' 11'", [tt, t, tt, t, tt, t, tt, t+b]),("7' 11' R", [tt, t + b, b]),
    ("6' 2' 9' 2' R 9'", [tt, t, tt, t, b, b]),("0'' 6' R 9' R",[tt, t, tt, t + b, b]),

    ("9' 2' R 5' 2'", [tt, t, tt, t + b, b]),
    ("5' 11 R 2' 5'", [tt, t, tt, t + b, b]),
    ("4' 0' 7' 4' 7' 11'", [tt, t, tt, t, tt, t + b]),
    ("R", [4 * b]),
]

arp_ex_9_0_4_7 = [
        ("9 11 0' 4' 7' 4' 11' 10' ", [tt, t, tt, t, tt, t, tt, t]),
        ("9' 7' 2' 4'", [tt, t, tt, t + 2*b])
]

arp_exm_9_0_4_7 = [
        ("0u 4u 7u 9u 11u 0uu 9u 7u", [tt, t, tt, t, tt, t, tt, t]),
        ("4u 2u 1u 0u", [tt, t, tt, t + 2*b])
]

arp_ex_0_4_7_11 = [
        ("4' 5' 7' 9' 11' 0'' 9' 7'", [tt, t, tt, t, tt, t, tt, t]),
        ("4' 2' 1' 0'", [tt, t, tt, t + 2 * b])
]

#template = [
#        (, []),
#        (, [])
#]

arp_ex_5_9_0_4 = [
        ("2'' 4'' 2'' 11' 0'' 9' 5' 2'", [tt, t, tt, t, tt, t, tt, t]),
        ("4' 2' 0' 9", [tt, t, tt, t + 2 * b]),
]

arp_ex2_9_0_4_7 = [
        ("4 7 11 2' 0' 4' 7' 11'", [tt, t, tt, t, tt, t, tt, t]),
        ("9' 7' 9' 2''", [tt, t, tt, t + 2 * b]),
]

arp_ex3_9_0_4_7 = [
        ("7' 4' 0' 9 2' 11 7 4", [tt, t, tt, t, tt, t, tt, t]),
        ("0' 9 10 11 7 4 2 0", [tt, t, tt, t, tt, t, tt, t]),
]

arp_ex_2_6_9_0 = [
        ("4'' 0'' 9' 6' 0'' 9' 6' 2'", [tt, t, tt, t, tt, t, tt, t]),
        ("9' 5' 2' 11 5' 6' 9' 0''", [tt, t, tt, t, tt, t, tt, t]),
]

arp_ex4_9_0_4_7 = [
        ("7u 4u 0u 9 9u 6u 2u 11 ", [tt, t, tt, t, tt, t, tt, t]),
        ("0u 4u 7u 11u 9u 4u 7u 2u", [tt, t, tt, t, tt, t, tt, t]),
]

arp_ex5_9_0_4_7 = [
        ("0u 4 7 11 9 7 4 5", [tt, t, tt, t, tt, t, tt, t]),
        ("6 9 0u 3u 2u 3u 2u 0u 10 11", [tt, t, tt, t, tt/3, tt/3, tt/3, t, tt, t]),
]

arp_ex6_9_0_4_7 = [
        ("0uu 2uu 11u 10u 9u 0u 4u 7u", [tt, t, tt, t, tt, t, tt, t]),
        ("6u 3u 2u 11 0u 2u 3u 5u", [tt, t, tt, t, tt, t, tt, t]),
        ("2u", [4 * b]),
]

arp_ex7_9_0_4_7 = [
        ("2uu 1uu 0uu 9u 11u 7u 4u 0u", [tt, t, tt, t, tt, t, tt, t]),
        ("10u 6u 3u 0u 10u 6u R 9u", [tt, t, tt, t, tt, t, tt, t]),
        ("9u 5u 2u 11 11 R ", [b, tt, t, tt, t, b]),
]


all_examples = [arp_ex_9_0_4_7, arp_exm_9_0_4_7,arp_ex_5_9_0_4 , arp_ex2_9_0_4_7,  arp_ex3_9_0_4_7, arp_ex_2_6_9_0, arp_ex4_9_0_4_7, arp_ex5_9_0_4_7, arp_ex6_9_0_4_7, arp_ex7_9_0_4_7]
all_examples_cont = []
for example in all_examples:
    all_examples_cont.extend(example)
