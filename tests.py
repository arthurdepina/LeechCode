
def mergeTwoLists(list1, list2):
    output = list()
    for i in list1:
        output.append(i)
    for j in list2:
        output.append(j)
    output.sort()
    return output


lista_a = [1, 2, 4]
lista_b = [1, 3, 4]
print(mergeTwoLists(lista_a, lista_b))
