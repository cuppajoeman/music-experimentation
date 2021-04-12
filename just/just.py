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

def lcm(lst):
    ans=1
    for i in lst:
        ans = ans*i//gcd(ans,i)
    return ans

def process_lcm(tup):
    return lcm(tup[0])

rhs_list = [x[1] for x in ratios]


#pprint.pprint(sorted(ratios, key=lambda r: sum(r)))


#pprint.pprint(sorted(ratios, key=lambda r: r[0]/r[1] % 1))

complexity_ordered_intervals = sorted(ratios, key=process_lcm)
complexity_ordered_intervals = sorted(ratios, key=process_lcm)

from itertools import chain, combinations

all_chords = combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 4)

complexity_ordered_chords = sorted(all_chords, key=lcm)

pprint.pprint(complexity_ordered_chords)



#lcm = lcm(rhs_list)

#for r in ratios:
    #multiplier = lcm/r[1]
    #r[0] *= multiplier
    #r[1] *= multiplier


#pprint.pprint(ratios)






