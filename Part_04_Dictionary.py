marksrange=[0,20,40,60,80,100,120]

dictionary={}

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

result=0

def diction(passes,defer,fail,uownumber):
    result=passes,defer,fail
    
    if passes==120 and defer==0 and fail==0:
       dictionary[uownumber]=("Progress"+str(result))
        
    elif passes==100 and defer<=20 and fail<=20:
        dictionary[uownumber]=("Module Trailer"+str(result))
        
    elif passes<=80 and defer<=120 and fail<=60:
        dictionary[uownumber]=("Progress-Module Retriever"+str(result))
    else:
        dictionary[uownumber]=("Exclude"+str(result))


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
    
    if pass120==True:
        print("Progess")
        global countprog
        countprog=countprog+1
        
        global pro_list1
        pro_a=(passes,defer,fail)
        pro_list1.append(pro_a)
                             
    elif pass100==True:
        print("Progress (module trailer)")
        global countmodtrail
        countmodtrail=countmodtrail+1
        
        global pro_list2
        pro_b=(passes,defer,fail)
        pro_list2.append(pro_b)
       
    elif pass80 ==True or pass60 ==True or pass40 ==True or pass20==True or pass0 ==True:
        print("Module retriever")
        global countmodretri
        countmodretri=countmodretri+1
        
        global pro_list3
        pro_c=(passes,defer,fail)
        pro_list3.append(pro_c)

    elif passEx40==True or passEx20==True or passEx0==True:
        print("Exclude")
        global countexclu
        countexclu=countexclu+1
        
        global pro_list4
        pro_d=(passes,defer,fail)
        pro_list4.append(pro_d)
        
def mainfunct():
    while True:
        try:
            # Input pass
            uownumber=input("Enter the UOW number: ")
            passes=int(input("Please enter your credit at pass: "))
            # Checking the range of Pass
            while (not passes in marksrange): # mrang=[0,20,40,60,80,100,120]
                print("Out of range!")
                passes=int(input("Please enter your credit at pass: "))
               
            # Input Defer  
            defer=int(input("Please enter your credit at defer: "))
            # Checking the range of Defer
            while (not defer in marksrange):
                print("Out of range!")
                defer=int(input("Please enter your credit at defer: "))
               
            # Input Fail 
            fail=int(input("Please enter your credit at fail: "))
            # Checking the range of Fail
            while (not fail in marksrange):
                print("Out of range!")
                fail=int(input("Please enter your credit at fail: "))
            
                                           
        except ValueError:     #to ckeck user inputs are integers or not
            print("Integer Required\n")
            
        else:        #to check the total is correct or not
            total= passes+defer+fail
            if total!=120:
                print("Total incorrect")
            else:
                validateinputs(passes,defer,fail)# calling the input validate function

                answers=passes,defer,fail
                diction(passes,defer,fail,uownumber)
                
                y=True
                while y:
                    contin=str(input("Do you want to continue?\nEnter 'y' for YES to add another set or 'n' for NO to stop program : "))
                    if contin=="Y" or contin=="y":
                        mainfunct() #to continue again the program
                            
                    elif contin=="N" or contin=="n":
                        print("\nPart 4 - Dictionary :\n_____________________\n\n",dictionary)
                        exit()
                    
                    else:      #to check the user input is y,Y,n,N or not
                        (contin!="y" and contin!="Y" )
                        print("Invalid Input\nPlease enter again.\n")
                        while False:
                            y = False
                            continue
                    
mainfunct()


#REFERENCES
#Dictionary - https://www.w3schools.com/python/python_dictionaries.asp
    
