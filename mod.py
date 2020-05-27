x = x
y = y
mod =1000
while(mod != 0):
    mod = x % y
    print(x,'÷',y,'...',mod)
    x = y
    y = mod
    