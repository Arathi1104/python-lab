while(True):
    print("Menu:")
    print("1.Occurence of word")
    print("2.character frequency")
    print("3.Display the factors of a given number")
    print("4.Exit")
    choice=input("Enter choice 1 -4:")
    if choice=="1":
        text=input("Enter a line of text:")
        words=text.split()
        count_words=[]
        counts=[]
        for s in words:
            if s not  in count_words:
                count=0
                for i in words:
                    if i==s:
                        count+=1
                count_words.append(s)
                counts.append(count)
        for i in range(len(count_words)):
            print(count_words[i],':',counts[i])
            
    if choice=="2":
        words=input("Enter a word:")
        freqcounts=[]
        counts=[]
        for s in words:
            if s not  in freqcounts:
                count=0
                for i in words:
                    if i==s:
                        count+=1
                freqcounts.append(s)
                counts.append(count)
        for i in range(len(freqcounts)):
            print(freqcounts[i],':',counts[i])
            
    if choice=="3":
        n=int(input("enter a number:"))
        if n>=0:
            factors=[]
            for i in range(1,n+1):
                if n%i==0:
                    factors.append(i)
        print("factors:",factors)

    if choice=="4":
        print("Exit")
            
        
        
    
