# Return whether any two nr from the list add up to k
def add_up_to_k(list_nr, k):
    for element1 in list_nr:
        for element2 in list_nr:
            if element1+element2 == k:
                return True
        return False

given_list = [10, 15, 3, 7]
k = 17
print(add_up_to_k(given_list,k))
