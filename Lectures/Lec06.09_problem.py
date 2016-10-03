#L6 Problem 9

#initial set
animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

animals['d'] = 'donkey'

#questions are what is output of the following;

animals #{'a': 'aardvark', 'b': 'baboon', 'c': 'coati', 'd': 'donkey'}

animals['c'] #coati

animals['donkey'] #error

len(animals) #4

animals['a'] = 'anteater'
animals['a'] #anteater

len(animals['a']) #8

animals.has_key('baboon') #False

'donkey' in animals.values() #True

animals.has_key('b') #True

animals.keys() #['a', 'c', 'b', 'd']

del animals['b']
len(animals) #3

animals.values() #['anteater', 'coati', 'donkey']