n=input()
a=n.split(".")
print("%02d" % int(a[2])+"-"+"%02d" % int(a[1])+"-"+"%04d" % int(a[0]))