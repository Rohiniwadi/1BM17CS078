def valid(s):
    opening=tuple('([{')
    closing=tuple(')]}')
    m=dict(zip(opening,closing))
    q=[]
    for i in s:
        if i in opening:
            q.append(m[i])
        elif i in closing:
            if not q or i!=q.pop():
                return "invalid"
    if len(q) :
      return "invalid"
    return "valid"
s="[](){)(}"
s1="{{}[]{"
print(valid(s))
print(valid(s1))
            
