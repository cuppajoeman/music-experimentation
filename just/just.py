from math import gcd
import pprint
ratios = [
        [1,1],
        [16,15],
        [9,8],
        [6,5],
        [5,4],
        [4,3],
        [45,32],
        [3,2],
        [8,5],
        [5,3],
        [9,5],
        [15,8],
        ]

def lcm(lst):
    ans=1
    for i in lst:
        ans = ans*i//gcd(ans,i)
    return ans

rhs_list = [x[1] for x in ratios]


pprint.pprint(sorted(ratios, key=lambda r: sum(r)))


pprint.pprint(sorted(ratios, key=lambda r: r[0]/r[1] % 1))

pprint.pprint(sorted(ratios, key=lcm))

for r in ratios:
    print(sum(r))


lcm = lcm(rhs_list)

for r in ratios:
    multiplier = lcm/r[1]
    r[0] *= multiplier
    r[1] *= multiplier


pprint.pprint(ratios)






