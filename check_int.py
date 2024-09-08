
def check_int():
    try:
        int(S)
       
    except:
        print("Bad String")
    else:
        print(S)


S = input().strip()
check_int()