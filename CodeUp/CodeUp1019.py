
n=input()
a=n.split('.')

print(str('%04d' % int(a[0]))+'.'+str('%02d' % int(a[1]))+'.'+str('%02d' % int(a[2])))