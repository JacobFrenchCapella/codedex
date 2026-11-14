wind = int(input("what is the wind"))

status = "unset"

if wind < 8:
    #when doing math use ==
    status = "Calm"
elif 7 < wind < 32:
    #this code could also have been written 8 <= wind <= 31
    status = "Breeze"
elif 31 < wind < 64:
    status = "Gale"
else:
    status = "Storm"

print(status)