
# coding: utf-8

# In[ ]:


def multiplication_table(m, n):
  for i in range(1,10):  
    for ii in range(m,n+1):
        print("%d x %d = %2d " % (ii,i,ii*i),end="   ")
    print()
  print()

def ChristmasTree(n,m):
 print("Merry Christmas !") 
 for i in range(0,n):
        print(" "*(n-i-1)+"ψ"*(i*2+1))
 for ii in range(0,m):
        print(" "*(n-2)+"| |")


