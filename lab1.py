def sqroot(n):
   if n<0:
      return "imaginary number"
   l,h,m=0,n,0
   ans=0
   while l<=h:
      m=int((h+l)/2)
      if m*m==n:
         ans=(m)
         break
      elif m*m<n:
         l=m+1
         ans=(m)
      else:
         h=m-1
   return ans
n=int(input())
print(sqroot(n))




