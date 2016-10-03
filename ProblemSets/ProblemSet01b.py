#Problem set 1b

s = 'azcbobobegghakl' #test number
s = s.lower() #convert to lower case, not really needed for test

start = 0
end = len(s) #length of variable s
ans = 0

while start < end:
    ansFind = s.find('bob', start, end)
    if ansFind == -1: #to stop an infinite loop, ansFind will equal -1 if no more 'bob' is found - s.find workings..
        break
    else:
        start = ansFind + 1 #add +1 to move onto the next character
    ans += 1 #answer

print("Number of times bob occurs is: " + str(ans))