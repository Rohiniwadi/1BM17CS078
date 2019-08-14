def sqroot(n):
   if n<0:
      return "imaginary number"
   l,h,m=0,n,0
   ans=0
   while l<=h:
      m=(h+l)/2
      if m*m==n:
         ans=int(m+1)
         break
      elif m*m<n:
         l=m+1
         ans=int(m+1)
      else:
         h=m-1
   return ans
n=int(input())
print(sqroot(n))



