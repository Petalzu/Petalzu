
import itertools
aa = ['a', 'b', 'c']
bb = list(itertools.permutations(aa, 2))
print(bb)
print("######################")
cc = list(itertools.combinations(aa, 2))
print(cc)