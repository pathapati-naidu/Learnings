l1=[11,2,3,4,5,9]
target=20

def extract_index():
    for i in range(len(l1)):
        for j in range(1,len(l1)):
            if l1[i]+l1[j]==target:
                return [i,j]

print(extract_index())