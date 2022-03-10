def fun(lst):
  m=[]
  for n in range(1,13): 
    if n not in lst: 
      m.append(n)
      print(m)
fun([1,2,3,4,5,6,7,8,9,12])