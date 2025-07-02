marksrange=[0,20,40,60,80,100,120]

countprog=0
countmodtrail=0
countmodretri=0
countexclu=0

pro_a=0
pro_b=0
pro_c=0
pro_d=0
pro_list1=[]
pro_list2=[]
pro_list3=[]
pro_list4=[]

#to get the Progression Outcomes & for validation parts
def validateinputs(passes,defer,fail):    
    pass120=(passes==120 and (defer==0 and fail==0))
    pass100=(passes==100 and (defer==20 and fail==0)) or (passes==100 and (defer==0 and fail==20))
    pass80=(passes==80 and defer==40 and fail==0) or (passes==80 and defer==20 and fail==20) or (passes==80 and defer==0 and fail==40)
    pass60=(passes==60 and defer==60 and fail==0) or (passes==60 and defer==40 and fail==20) or (passes==60 and defer==20 and fail==40)or (passes==60 and defer==0 and fail==60)
    pass40=(passes==40 and defer==80 and fail==0) or (passes==40 and defer==60 and fail==20) or (passes==40 and defer==40 and fail==40)or (passes==40 and defer==20 and fail==60)
    pass20=(passes==20 and defer==100 and fail==0) or (passes==20 and defer==80 and fail==20) or (passes==20 and defer==60 and fail==40)or (passes==20 and defer==40 and fail==60)
    pass0=(passes==0 and defer==120 and fail==0) or (passes==0 and defer==100 and fail==20) or (passes==0 and defer==80 and fail==40)or (passes==0 and defer==60 and fail==60)

    passEx40=(passes==40 and defer==0 and fail==80)
    passEx20=(passes==20 and defer==20 and fail==80)or (passes==20 and defer==0 and fail==100)
    passEx0=(passes==0 and defer==40 and fail==80)or (passes==0 and defer==20 and fail==100)or (passes==0 and defer==0 and fail==120)

    #Histrogram & Lists
    if pass120==True:
        print("\nProgress\n")
        global countprog
        countprog=countprog+1
        
        global pro_list1
        pro_a=(passes,defer,fail)
        pro_list1.append(pro_a)
                             
    elif pass100==True:
        print("\nProgress (module trailer)\n")
        global countmodtrail
        countmodtrail=countmodtrail+1
        
        global pro_list2
        pro_b=(passes,defer,fail)
        pro_list2.append(pro_b)
       
    elif pass80 ==True or pass60 ==True or pass40 ==True or pass20==True or pass0 ==True:
        print("\nModule retriever\n")
        global countmodretri
        countmodretri=countmodretri+1
        
        global pro_list3
        pro_c=(passes,defer,fail)
        pro_list3.append(pro_c)

    elif passEx40==True or passEx20==True or passEx0==True:
        print("\nExclude\n")
        global countexclu
        countexclu=countexclu+1
        
        global pro_list4
        pro_d=(passes,defer,fail)
        pro_list4.append(pro_d)
        
#Histrogram       
def histrogram():
    outcometotal=0
    
    print("-------------------------------------------------------\nHistrogram")
    print("Progress ",countprog,'                  : ',end=" ")
    for i in range(countprog):
        print( "* ", end="")
    print("\nProgress (module trailer) ", countmodtrail,' : ',end=" " )
    for i in range(countmodtrail):
        print( "* ", end="")
    print("\nModule retriever ",countmodretri,'          : ',end=" ")
    for i in range(countmodretri):
        print( "* ", end="")
    print("\nExclude ", countexclu,'                   : ',end="" )
    for i in range(countexclu):
        print( " * ", end="")
    outcometotal=countprog+countmodretri+countmodtrail+countexclu
    print('\n\n',outcometotal,'outcomes in total\n-------------------------------------------------------\n\nPart 2 - List (extension) :\n___________________________\n\n')
  
    #Lists
    if countprog>0:
        new1=str(i)
        new1=pro_list1
        print ("Progress - ",new1)
            
    if countmodtrail>0:
        new2=str(i)
        new2=pro_list2
        print ("Progress (module trailer) - ",new2)
          
    if countmodretri>0:
        new3=str(i)
        new3=pro_list3
        print ("Module retriever - ",new3)
                  
    if countexclu>0:
        new4=str(i)
        new4=pro_list4
        print ("Exclude - ",new4)
    
    #Text File
    print('\nPart 3 - Text File (extention) : This will be open as a separate file\n______________________________')    
    f=open('Part 3 - Text File.txt', 'w')
    for x in pro_list1 :
        print("Progress - ",x,file=f)
    for x in pro_list2:
        print("Progress (module trailer) - ",x,file=f)
    for x in pro_list3:
        print("Module retriever - ",x,file=f)
    for x in pro_list4:
        print("Exclude - ",x,file=f)       
            
    f.close()
   
#Main Version
def mainfunct():   
    while True:
        try:
            # Input pass
            passes=int(input("Please enter your credit at pass: "))
            #to check the value in the range or out of the range (Pass)
            while(not passes in marksrange):
                print("Out of range!\n")
                passes=int(input("Please enter your credit at pass: "))
               
            # Input Defer  
            defer=int(input("Please enter your credit at defer: "))
            #to check the value in the range or out of the range (Defer)
            while(not defer in marksrange):
                print("Out of range!\n")
                defer=int(input("Please enter your credit at defer: "))
               
            # Input Fail 
            fail=int(input("Please enter your credit at fail: "))
            #toh ceck the value in the range or out of the range (Fail)
            while(not fail in marksrange):
                print("Out of range!\n")
                fail=int(input("Please enter your credit at fail: "))  
                                           
        except ValueError:     #to ckeck user inputs are integers or not
            print("Integer Required\n")
            
        else:        #to check the total is correct or not
            total= passes+defer+fail
            if total!=120:
                print("Total incorrect")
            else:
                validateinputs(passes,defer,fail)# calling the input validate function

            #to ask another set or quit
            y= True
            while y:
                print("Would you like to enter another set of data")
                x= str(input("Enter 'y' for yes or 'q' to quit and view result:  "))
            
                if (x=="q") or (x=="Q"):
                    histrogram()
                    exit()
                
                elif(x== "y") or (x=="Y"):
                    mainfunct()  #to continue again the program
                    
                else:      #to check the user input is y,Y,q,Q or not
                    (x!="y" and x!="Y" )
                    print("Invalid Input\nPlease enter again.\n")
                    while False:
                        y = False
                        continue
                    
print("Part 1 - Main Version :\n_____________________\n\n")
mainfunct()#calling the mainfunction   #gathering user inputs
           #Beginning of the program


#REFERENCES
#for loop-https://www.w3schools.com/python/python_for_loops.asp
#while loop-https://www.w3schools.com/python/python_while_loops.asp
