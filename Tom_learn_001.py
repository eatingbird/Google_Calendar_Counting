# Rewrite your function from Udacity to remove the while True:
# and replace it with a condition.
# Then return the final result *after* the loop exits on its own.
# Basically make it look more like my example function.
#
# # My example
# def while_example():
#      start = 0
#     while start < 10:
#         print(start)
#         start += 1
#     return start - 5
#
# #Your code
# def find_last(target,search):
#     count = -1
#     while True:
#         local=target.find(search,count+1)
#         if local == -1:
#             return count
#
# Hint for beginner programming: when you get confused, go verbose.
# This is particularly useful when refactoring code (which is what you're doing here)
# I do it all the time even now.
# So here you can just assign the output of everything you call (find, whatever)
# to local variables and then delete any variable you use exactly once.

## An alternative for comparison.
def find_last():
    count = 0
    final = 0
    tg = "abcdeabcdeaaedaa"
    sc = "dea"

    rev_tg = tg[::-1]
    rev_sc = sc[::-1]
    count_from_back = rev_tg.find(rev_sc)
    final = len(tg) - count_from_back - len(sc)
    print (final)

## The homework
def find_last_real():
    count = -1
    final = 0
    tg = "abcdeabcdeaaedaa"
    sc = "dea"
    
    while final >= 0: #run if final is larger than or equal to 0 (if there is another string)
        count = count+1
        final = tg.find(sc,count+1)# count+1= 0-3 find 1st loc, 4-8 & find 2nd loc, 9 and final is -1
##    return count # The procedure is supposed to return, not print, but just like "My example", but not working.
    print (count) # count is 8, and final is -1 and it pops out of the loop to do this.

find_last()
find_last_real()
