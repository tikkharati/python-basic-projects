#to verity that the gmail is valid or not
#if email is worng then output is worng g@g.com

email=input("enter your email  :")
k,j,d=0,0,0
if (len(email)>=6):
    if(email[0].isalpha()):
       if ("@" in email) and (email.count("@")==1):
          if(email[-3]==".") ^ (email[-4]=="."):
             for i in email:
                if(i== i.isspace()):
                    k=1

                elif(i.isalpha()):
                     if i==i.upper():
                        j=1

                elif (i.isdigit()):
                    continue

                elif(i=="_" or i=="." or i=="@"):
                    continue

                else:
                  d=1

             if(k==1 or j==1 or d==1 ):
                print("worng email5")

          else:
            print("wrong email 4") 

       else:
        print("wrong email 3")
          

    else:
        print("wrong email 2")

else:
    print("wrong email 1")