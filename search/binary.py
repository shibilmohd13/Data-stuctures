

new_list = [1,2,3,4,5,6,7,8,9]



# def search(ls, emt):
    
#     lower = 0
#     upper = len(ls) - 1

#     while lower < upper:
#         mid = upper + lower // 2

#         if ls[mid] == emt:
#             return f"Found at position {mid+1}"
#         else:
#             if emt < ls[mid]:
#                 upper = mid - 1
#             else:
#                 lower = mid + 1
#     return "not found"

# print(search(new_list,))



def search(ls , emt):
    lower = 0 
    upper = len(ls) - 1

    while lower < upper:

        mid = upper + lower // 2
        if ls[mid] == emt:
            return f"found at position {mid}"
        else:
            if ls[mid] < emt:
                lower = mid + 1
            else:
                upper = mid - 1
    return "not found"

print(search(new_list, 9190))


















