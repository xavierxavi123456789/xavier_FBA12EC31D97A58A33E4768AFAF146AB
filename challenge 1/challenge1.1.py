def fact_rec(n):
  if(n==0 or n==0):
    return 1  
  else:
    return n*fact_rec (n-1)
number=5
res=fact_rec(number)
print("the factorial of {}is{}".format(number,res))
