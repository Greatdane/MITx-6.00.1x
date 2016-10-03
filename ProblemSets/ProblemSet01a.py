#Problem set 1a

s = 'Azcbobobegghakl' #alreay given in problem set
s = s.lower() #convert to lower
ans = int(s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')) #counting
print("Number of vowels: " + str(ans))
