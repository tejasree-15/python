#A string is a collection of characters
#Accessing elements in the string
#A string element can be accessing the slice & indexing
#indexing
a="software industry"
print(a[0:12])
#slicing
b="software industry"
print(b[2:17:2])

#Representation of a string: A string can be represented in 3 ways :
#single quotations
x='ece'
print(type(x))
#double quotations
y="tejasri"
print(type(y))
#triple quotation
z="""ramcharan"""
print(type(z))

#string methods
#upper()
a="python"
print(a.upper())

#lower()
b="PYTHON"
print(b.lower())

#count()
c="i love kerala"
print(c.count("kerala"))

#index()
d="rajahmundry"
print(d.index("u"))

#strip()
e1=" this is my ring "
print(len(e1))
print(e1)
e2=e1.strip()
print(len(e2))
print(e2)

#rstrip()
s1=" i like dhoni "
print(len(s1))
print(s1)
s2=s1.rstrip()
print(len(s2))
print(s2)

#lstrip()
s1=" i like chocolates "
print(len(s1))
print(s1)
s2=s1.lstrip()
print(len(s2))
print(s2)

#format()
name=["ram","cherry","anu"]
for i in name:
    print("hi {} thinnava".format(i))

#find()
k="tamilnadu"
print(k.find("n"))
print(k.find("d"))

#startswith()
t="i like biryani"
print(t.startswith("i"))

#endswith()
L="i love cricket"
print(L.endswith("t"))

#eg
websites=["amazon.com","myntra.in","ajio.in","flipkart.com"]
in_websites=[]
for i in websites:
    if i.endswith("in"):
        in_websites.append(i)
print(in_websites)

#isalpha()
print("openai".isalpha()) #True
print("openai123".isalpha()) #False(contains numbers)
print("open ai".isalpha()) #False(contains space)

#isalnum():
print("openai123".isalnum())#true
print("openai!".isalnum())#false
print("openai 123".isalnum())#false

#Title():
s="the wing of fire"
print(s.title())

#split():
s="hello"
print(s.split())

#join():
s="dolly".join(s)
print(s)
