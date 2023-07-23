first_tuple=("Master","Nani","Hanuman","Venkateshwara Swamy ")

# Extracting the index number for the particular item
print(first_tuple.index("Hanuman"))

# No of times of occurance for a specified value if the element does not exist it will gve nothing

print(first_tuple.count("Mahesh"))


# Unpacking the elements from a tuple
name1,name2,*name3=first_tuple

print(name1,name2,name3)

num_tuple=(1,2,3,4,5,6)
print(num_tuple*2)