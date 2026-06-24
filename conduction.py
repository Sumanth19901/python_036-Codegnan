a=input().lower()
m=int(input())
if m>=90:
    grade="a"
elif m>80:
    grade="b"
elif m>70:
    grade="c"
elif m>60:
    grade="d"
elif m<=40:
    grade="e"
else:
    print("fail")
print(f"name{a},marks{m},grade{grade}")
