#Creation of dictionary
#1.empty dictionary
a={}
print(type(a))

#2.key values
mydict={1:"chennai",2:"rajahmundry"}
print(type(mydict))

#accessing the elements in a dictionary
b={100:"pallavi",200:"adhya","phone":9367937836,"place":"rajahmundry"}
print(b[100])
print(b["place"])

#updating the dictionary:
d={100:"karthik",200:"max","phone":9367937836,"place":"goa"}
d[100]="ram"
print(d)

#METHODS OF DICTIONARY
#get():
s={"name":"vidhya","s.no":1,"phone":9673459267}
print(s)
print(s.get("name"))
print(s.get("s.no"))

#keys():
s1={"name":"divya","s.no":19,"phone":9673459267}
print(s1)
print(s1.keys())

#values():
s2={"name":"preethi","s.no":7,"phone":9673459267}
print(s2)
print(s2.values())

#items():
s3={"name":"sri","s.no":73,"phone":9673459267}
print(s3)
print(s3.items())

#update():
s5={"name":"teja","place":"kerala","phone":967025867}
s5.update({"food":"biryani"})
print(s5)

#updating the dictionary into list
s4={"name":"pooja","s.no":29,"phone":9673459267}
print(s4)
print(list(s4))

#pop():
s6={"name":"swetha","place":"kashmir","s.no":56}
s6.pop("s.no")
print(s6)