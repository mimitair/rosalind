a = 60
if a < 50:
    print 'a is kleiner dan 50'
else:
    print 'a is groter dan 50'

greetings = 1
while greetings <= 5:
  print 'Hello! ' * greetings
  greetings = greetings + 1      # copied from rosalind

print range(5, 12)

# exercise:
b = 4644
c = 9133
# repeat c-b times? determine if a is odd, use if else
if b % 2 == 1 and c % 2 == 1: # het getal is niet deelbaar door zichzelf als er 1 overblijft na deling. DUS: if b is oneven:
    print range(b, (c + 2), 2)
    print sum(range(b, (c + 2), 2))
elif b % 2 == 0 and c % 2 == 1:
    b = b+1
    print range(b, (c + 2), 2)
    print sum(range(b, (c + 2), 2))
elif b % 2 == 1 and c % 2 == 0:
    print range(b, c, 2)
    print sum(range(b, c, 2))
else:
    b = b + 1
    print range(b, c, 2)
    print sum(range(b, c, 2))
 # dit zou moeten werken, maar ik denk dat het vele efficienter kan. Ja, herhaal dit. Dit kan vele korter






