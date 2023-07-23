# a=["JAI BALAYYA",["Mahesh","Anil","PSPK","NTR"]]
# b=list()
#
# # for j in range(len(a)):
# #     # print(a[j])
# #     for i in range(0,len(a[j])):
# #         print(a[j][i]+" ",end="")
# a.insert(1,"NTR")
# for i in range(len(a)):
#     if a[i]=="JAI BALAYYA"or a[i]=="NTR":
#         # a.pop(1)
#         continue
#     else:
#         for j in range(len(a[i])):
#             # a[i][j].capitalize()
#             if a[i][j]=="Mahesh" :
#
#                 continue
#             else:
#
#                 # print(a,end="")
#                 print(a[i][j])
# # a.remove(a[1][0])
# # print(a)
#
#
# #

# new_list=["Mahesh","Anil","Likitha","Renu"]
# new_list.sort()
# print(new_list)
# # Doubt here
# number=["12","1221","121","212","222","1","3","2","4","6","5","7"]
# print(number.sort())
# new_list.clear()
# print(new_list)

#2d lists

fruits=["Orange","Apple","Kiwi"]
Biryani=["Dum","chicken","Mutton"]
desserts=["Cake","Lassi","Gulab Jamun"]

food=[fruits,Biryani,desserts]
for i in range(len(food)):
    for j in range(len(food[i])):
        print(food[j][0])








