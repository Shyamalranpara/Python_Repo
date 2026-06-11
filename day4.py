a=4
b=5
print("Sum of %d and %d is %d"%(a,b,a+b))

a=4.5
b=5.5
print("Sum of %f and %f is %f"%(a,b,a+b))

x=50
y=70
print("Sum of",x,"and",y,"is",x+y)

a=10
b=20
c=30
print(a,b,c,sep='-',end='\t')

print(a,end=' ')
print(b,end='\n\n\n\n')
print(c)
print("Hello\rAB")
print("\\")
print("\"")

"""
Escape Sequences

\n  New line
\t  Tab pace
\r  Carriage Return
\b  Backspace
\\  print \
\"  print "
\'  print '

"""

a=10
b=20
c=30

print(a,b,c,sep="-",end="\t")
print(a,end="\t")
print(b,end="\t")
print(c)

print("Hello\rAbc")
print("hello\\world")
print("\\")
print("hello\",world")
print("helloname\'")