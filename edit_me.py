def monotonic(lst):
    M=True
    for i in range(len(lst)-1):
        if lst[i]<lst[i+1]:
            continue
        else:
            M=False
            break
    print(M)

lst=(2,3,4,5,6)
monotonic(lst)