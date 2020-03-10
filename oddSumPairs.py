# Check if a list of even length has possible pairs such that the sum of each pair is an odd number

#method to check if a pair of numbers has an odd sum
def is_odd_pair(a,b):
    if (a+b)%2==0:
        return False
    else:
        return True
        
        
#method to find unique odd-sum pairs in a list
def find_odd_pairs(A):
    pairslist = []
    for i in range(len(A)):
        for j in range(len(A)):
            if i==j:
                continue
            if is_odd_pair(A[i],A[j]):
                pairslist.append((A[i],A[j]))
    pairslist = [tuple(x) for x in set(map(frozenset, pairslist))]
    return pairslist


#method to check if a given list (of length N an even number) has unique odd-sum pairs
def has_unique_odd_sum_pairs(A):
    pairs = find_odd_pairs(A)
    for i in pairs:
        paircheck = []
        paircheck.append(i[0])
        paircheck.append(i[1])
        for j in pairs:
            if i[0]==j[0] or i[0]==j[1] or i[1]==j[0] or i[1]==j[1]:
                continue
            paircheck.append(j[0])
            paircheck.append(j[1])
        if set(paircheck) == set(A):
            return True
    return False


#method to test the list unique odd sum pairs method on 100 samples
def test_driver():
    import random
    from random import seed
    from random import randint
    # seed random number generator
    seed(42)
    for _ in range(1,100):
        testlist = []
        random_even = random.randrange(2, 11, 2)
        for __ in range(random_even):
            testlist.append(randint(1,100))
        print("Input List : {} || Has odd sum pairs : {}".format(testlist,list_unique_odd_sum_pairs(testlist)))

def main():
    test_driver()

if __name__ == "__main__":
    main()
