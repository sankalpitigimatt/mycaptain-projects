import csv
def csv_function(info_list):#function for splited elements to be written in csv(csv func)


    with open("student_info.csv","a",newline="") as csv_file:#the word "a"used here means append

       

        writer=csv.writer(csv_file)#objest
        if csv_file.tell()==0:
             writer.writerow(["NAME","AGE","CONTACT-NUMBER","E-MAIL"])
        writer.writerow(info_list)#function call

if __name__=="__main__":
    condition= True
    student_num=1
    while(condition):
        student_info=input("Enter  student information of student #{} in the format of (Name Age Contact_number E-mail_ID)::".format(student_num))
        # the input in the upper format


       

        student_info_list=student_info.split(" ")
        #stores the splitted in above address

       
        print("\n Entered information is:-\n Name: {} \n Age: {} \n Contact_number: {} \n E-mail ID: {} "
        .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))

        #.format will assign the arguments passed through it in the curly brackets
        choice_check=input("Is entered information is correct or not:(yes/no):-")
        if choice_check=="yes":

            csv_function(student_info_list)#csv function call
            #passes the spitted info as an  arguments in the above fuction call
            
            condition_check=input("enter(yes/no) if if u want to enter another student information:::")
            if condition_check=="yes":
                condition=True
                student_num=student_num+1
            elif condition_check=="no":
                condition=False
        elif choice_check=="no":
            print("\n Please re-enter the values!::")    

