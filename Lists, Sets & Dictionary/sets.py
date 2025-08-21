s = {1, 2, 3, 38}
print(s, type(s))
#print(s[3]) # can't print indices cuz its unordered

s.add(39)
s.remove(1)
# s.remove(83) - will throw error 
s.discard(83)
# s.pop() -  removes random element
print(s)