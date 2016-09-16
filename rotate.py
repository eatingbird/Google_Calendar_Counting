# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def rotate(string, n):
    lis = ['a', 'b', 'c', 'd','e','f', 'g', 'h', 'i', 'j','k','l','m','n','o','p','q','r','s', 't','u','v','w','x','y','z']
    cllc = ""
    cnt = 0
    for e in string:
        if e ==" ":
            cllc = cllc + e
        else:
            cllc = cllc + lis[(int(lis.index(e))+n)%26]
    return cllc

print (rotate ('sarah', 13))
#>>> 'fnenu'
print (rotate('fnenu',13))
#>>> 'sarah'
print (rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17))
