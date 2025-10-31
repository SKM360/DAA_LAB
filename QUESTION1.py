#Write a program to trace the time complexity of the loop. For ( i=0; i<n; i++) 

import time
n = int(input("Enter n: "))
start_time = time.time()
for i in range(n): 
 end_time = time.time()
RUN_time = end_time - start_time
print("Time taken:", RUN_time  ,"seconds")
