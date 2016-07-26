# Rewrite your function from Udacity to remove the while True: and replace it with a condition.
# Then return the final result *after* the loop exits on its own.
# Basically make it look more like my example function.

# My example
# def while_example():
# ....start = 0
# ....while start < 10:
#         print(start)
#         start += 1
# ....return start - 5

# Your code
# def find_last(target,search):
#     count = -1
#     while True:
#         local=target.find(search,count+1)
#         if local == -1:
#             return count

def find_last(target, search):
	count = -1
	while target.find(search,count+1)!=-1:
		count += 1
	return count

print find_last("asbdecde", "de")


def find_last():
	target = "asbdecde"
	search = "de"
	count = -1
	while target.find(search,count+1)> -1:
		count += 1
	return count
