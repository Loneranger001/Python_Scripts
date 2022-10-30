# sets are unordered, mutable, no duplicates

myset = {1,2,3,4,5,1,2,3}
# print(myset)

# empty set 
myset = set()
# print(type(myset))
myset.add(1)
myset.add(2)
myset.add(3)
myset.add(1)
# print(myset)
# print(myset.pop())
# print(myset)

# for x in myset:
#    print(x)

odds = {1,3,5,7,9}
evens = {2,4,6,8,10}
primes = {2,3,5,7}

odds_evens=odds.union(evens)
# print(odds_evens)
odds_primes= odds.intersection(primes)
# print(odds_primes)

setA={1,2,3,4,5,6,7,8,9}
setB={1,2,3,10,11,12}

diff=setA.difference(setB)
# print(diff)

setA={1,2,3,4,5}
setB={1,2,3}
print(setA.issuperset(setB))
