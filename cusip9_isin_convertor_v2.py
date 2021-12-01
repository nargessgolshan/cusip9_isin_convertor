def cusip9_isin_convertor(CUSIP9):
    

    CUSIP9_2=[alpha_number_dict[character] if character in alpha_number_dict else character  for character in CUSIP9]
    CUSIP9_edited="".join(CUSIP9_2)

        
    temp='3028'+CUSIP9_edited
    odds=""
    evens=""
    for i in range(len(temp)):
        if i%2==0:
            odds=odds+temp[i]
        else:
            evens=evens+temp[i]
            
    if len(odds)>len(evens):    
        odds2=[str(int(i)*2) for i in odds]
    else: 
        odds2=[str(int(i)*2) for i in evens]

    
    odds3=[]
    for  i in range(len(odds2)):
        for j in range(len(odds2[i])):
            odds3.append(int(odds2[i][j]))
        
        if len(odds)>len(evens):
            odds4=odds3+[int(i) for i in evens] 
        else: 
            odds4=odds3+[int(i) for i in odds] 
       


    isin_check_digit=(10-sum(odds4)%10)%10

    isin="US"+CUSIP9+str(isin_check_digit)
    return(isin)
