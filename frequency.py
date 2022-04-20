string = input("enter a string:")
  
# using naive method to get count 
# of each element in string 
all_freq = {}
  
for i in string:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
  
# printing result 
print (  "output:"+ str(all_freq))