for a in range(60):
    for b in range(60):
        for c in range(60):
            for d in range(60):
                for e in range(60):
                    for f in range(60):
                        if not a==b and not b==c and not c==d and  not d==e and  not e==f:
                            possiveis = [a,b,c,d,e,f]
                            print(possiveis)