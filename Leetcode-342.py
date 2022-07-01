n = int(input())
mantiq = False
while(n/4):
    if n == 4 or n ==1:
        mantiq = True
        break
    n /= 4
    if n<4:
        break
print(mantiq)