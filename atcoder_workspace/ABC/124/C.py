import sys
input = sys.stdin.readline
s = input()

ans1=0
ans2=0
# 01にする
for i in range(len(s)):
    if i % 2 == 0:
        if s[i] == '1':
            ans1+=1
    else:
        if s[i] == '0':
            ans1+=1
# 10にする
for i in range(len(s)):
    if i % 2 == 0:
        if s[i] == '0':
            ans2+=1
    else:
        if s[i] == '1':
            ans2+=1
print(min(ans1,ans2))