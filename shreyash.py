print("========== admission crateria ==========")
age=int(input("Enter your age:"))
mark=float(input("Enter your mark:"))

if(age>=18 and age<=25):
    print("age is  eligible.")

    if(mark>=70):
        
        if(mark>=85):
            print("it is eligiblr for aiml.")
        elif(mark<=85 and mark>=75):
            print("it is eligible for ent&c.")
        else:
           print("it is eligible for civil,mechanical,electrical.") 
    else:
     print("it is not eligible for engneering admission.")  
else:
    print ("age is not eligible.")

print("========== thank you  ==========")  