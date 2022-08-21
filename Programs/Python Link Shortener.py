import pyshorteners
url=input("Enter A Link>>")
i=pyshorteners. Shortener().tinyurl.short(url)
print("The Shortened Link is>>: ",i)