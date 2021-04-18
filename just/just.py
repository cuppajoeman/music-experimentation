from math import gcd
import pprint
import itertools

# We will make classes out of this next

ratios = [
    ([1,1], 0),
    ([16,15], 1),
    ([9,8], 2),
    ([6,5], 3),
    ([5,4], 4),
    ([4,3], 5),
    ([45,32], 6),
    ([3,2], 7),
    ([8,5], 8),
    ([5,3], 9),
    ([9,5], 10),
    ([15,8], 11),
]

just_interval_ratios = {
    0: [1,1],
    1: [16,15],
    2: [9,8],
    3: [6,5],
    4: [5,4],
    5: [4,3],
    6: [45,32],
    7: [3,2],
    8: [8,5],
    9: [5,3],
    10: [9,5],
    11: [15,8]
}

def compute_common_base_ratio(jir):
    return lcm([x[0] for x in just_interval_ratios.values()])

def convert_ratios_to_common_base(jir):
    cbr = compute_common_base_ratio(jir)
    for k, v in jir.items():
        base_ratio = v[0]
        multiplier = cbr//base_ratio
        v[0] *= multiplier
        v[1] *= multiplier

def lcm(lst):
    ans=1
    for i in lst:
        ans = ans*i//gcd(ans,i)
    return ans

def process_lcm(tup):
    return lcm(tup[1])


convert_ratios_to_common_base(just_interval_ratios)

jir_list = [ (k, v) for k, v in just_interval_ratios.items()]


complexity_ordered_intervals = sorted(jir_list, key=process_lcm)

pprint.pprint(complexity_ordered_intervals)

#from itertools import chain, combinations
#
#all_chords = combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 4)
#
#def chord_complexity(chord):
#    all_ratios = []
#    for interval in chord:
#        all_ratios.extend(just_interval_ratios[interval])
#    print(all_ratios)
#    return lcm(list(all_ratios))
#
#complexity_ordered_chords = sorted(all_chords, key=chord_complexity)
#
#print('ordered')
#pprint.pprint(complexity_ordered_chords)







