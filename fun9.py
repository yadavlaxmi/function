def fun(a):
  i=0
  max=0
  while i<len(a):
    if a[i]>max:
      max=a[i]
    i=i+1
  return(max)
print(fun([50, 40, 23, 70, 56, 12, 5, 10,]))
