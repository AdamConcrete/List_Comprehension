#Max lenght word:
from operator import itemgetter

words = ['Python', 'is', 'a', 'widely', 'used',
         'high-level', 'programming', 'language',
         'for', 'general-purpose', 'programming,',
         'created', 'by', 'Guido', 'van', 'Rossum',
         'and', 'first', 'released', 'in', '1991.']

result = ['', 0]
result = [(word,len(word)) for word in words]
longest_word = max(result,key=itemgetter(1))

print (longest_word)


