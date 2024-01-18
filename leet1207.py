# 1207. Unique Number of Occurrences

def uniqueOccurrences(arr) -> bool:
    occurrences = dict()
    for i in arr:
        if i in occurrences: occurrences[i] += 1
        else: occurrences[i] = 1
    occ = list(occurrences.values())
    return len(set(occ)) == len(occ) 


print(uniqueOccurrences([1,2,2,1,1,3])) # true
print(uniqueOccurrences([1,2])) # false
print(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])) # true
