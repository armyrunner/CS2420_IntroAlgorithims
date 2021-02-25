def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]


def main():
    print "Generating permutations..."
    perms = []
    s = ['0', '1', '2', '3','4','5','6','7','8']
    for p in all_perms(s):
        perms.append(p)
    perms.sort()
    print 'There are', len(perms), 'permutations'
    print 'First permutation:',perms[0]
    print 'Last permutation:',perms[-1]
    print 'Middle permutation:',perms[len(perms)/2]
    #for i in range(len(perms)):
    #    print perms[i]
    
    
main()
