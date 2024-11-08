def wc(s):
    s=s.lower()
    l=[]
    for i in s:
        if i not in l:
            l.append(i)
    print("Alphabet        Frequency")
    for i in l:
        c=s.count(i)
        print(f"{i}               {c}")

k=input("Enter a string:")
wc(k)