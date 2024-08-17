# third exercise for Rosalind, some experimenting with lists and strings
fungi_list = ["psilocybe", "agaricus", "pichia", "candida"]
print fungi_list[:2]

a = "kaka"
b = "pipi"
c = a[:2] + b[2:]
print c
# deze code geeft "kapi" :)

# now the true exercise:
s = "AfD4Nktbk81IWChrttusia29NpusillaXSuNKJ7AVlfr5s9djhR2wwJTsJDlqlREfwCtM6siU7Jg30nTgFdC3SScO5zIm68GgkgW6zXzulS201xhO7TZkd89wCHJvnFvawUW3HVSs3AVnic4wwxCjFNw1VuBpQUCHgDgvG6N951WzmwyegeG8zrIRttY6kcu570neD."
a = 13
b = 21
c = 25
d = 31
x = " "
ss = s[a:b] + s[b] + ' ' + s[c:d] + s[d] # ' ' voor een spatie, je hoeft geen extra variabele "x" aan te maken
print (ss)
# Hoezee!!

