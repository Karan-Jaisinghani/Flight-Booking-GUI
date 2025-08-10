from tkinter import *
from tkcalendar import *
from datetime import date
from PIL import Image, ImageTk
import pymysql

root=Tk()
root.geometry("2000x2000")
root.title('BOOK HERE')
root.configure(bg='white')

#Variables

adlt= None
child= None
inf= None
class1= StringVar(root, "")
entrymail= StringVar(root, " ")
entryname= StringVar(root, "")
clicked1 = StringVar()
clicked2 = StringVar()
cal1=None
cal2=None
price= int
dt1=date(2024,12,25) 
dt2=date(2026,12,30)


txt="Welcome to 'Fly High Airlines!'"
count = 0
text=""


def slider():
    global count,text
    if count >= len(txt):
        count=-1
        text=''
        label33.config(text=text)
    else:
        text = text + txt[count]
        label33.config(text=text)
    count += 1
    label33.after(100,slider)

# Functions


def create_widgets():
    global  adlt
    global child
    global inf  #Type of passengers

    global class1 #Seat/Ticket Type

    global entrymail
    global entryname #name and email

    global clicked1
    global clicked2

    global date1
    global date2

    global cal1
    global cal2

    global classfac
    global childfac
    global destinyfac
    global price
   
    inf= Spinbox(root, from_=0, to=10,width=25)
    inf.place(x=1296,y=540)
    child=Spinbox(root,from_=0,to=10,width=25)
    child.place(x=1296, y=625)
    adlt = Spinbox(root, from_=0, to=10, width=25)
    adlt.place(x=1296, y=700)

    rb1=Radiobutton(root,text='Economy',variable=class1,value="Economy",height=4,width=20,relief='solid').place(x=165,y=510)
    rb2=Radiobutton(root,text='Premium Economy',variable=class1,value="Premium Economy",height=4,width=20,relief='solid').place(x=165,y=590)
    rb3=Radiobutton(root,text='Business Class',variable=class1,value="Business Class",height=4,width=20,relief='solid').place(x=165,y=670)

    entry1 = Entry(root,width=22,relief='solid',font=('Arial', 15),bd=1,textvariable=entrymail).place(x = 514, y = 250)  
    entry2 = Entry(root,width=22,relief='solid', font=('Arial', 15), bd=1,textvariable=entryname).place(x = 782, y = 250)
    
    clicked1.set( "Choose" ) 
    flightsfrom=["Jaipur","Delhi","Mumbai","Kolkata","Bangalore"]
    labelflights1= Label(root, text=" Available Flights From",width=40) .place(x=1150,y=225)
    flights1=OptionMenu(root,clicked1,*flightsfrom)
    flights1.place(x=1150,y=265)
    flights1.config(width=40)
    flights1.config(height=2)
    flights1.config(bg='light blue')

    clicked2.set( "Choose" ) 
    flightsto=["Jaipur","Delhi","Mumbai","Kolkata","Bangalore","Dubai","Singapore","Phillipines"]
    labelflights2= Label(root, text=" Available Flights To",width=40) .place(x=1150,y=335)
    flights2=OptionMenu(root,clicked2,*flightsto)
    flights2.place(x=1150,y=375)
    flights2.config(width=40)
    flights2.config(height=2)
    flights2.config(bg='light blue')

    cal1= Calendar(root, selectmode="day",mindate=dt1,maxdate=dt2)
    cal1.place(x = 650,y =350)

  
    def get_date1():
        buttonlabel1.config(text=cal1.get_date())
  

    button1= Button(root, text= "Select the Date", command= get_date1,relief='solid',bd=1,width=35)
    button1.place(x = 649,y =542)
    buttonlabel1= Label(root, text="",relief='solid',font=('Arial', 15),width = 13)
    buttonlabel1.place(x = 707,y =573)
 


def Book():
    
    Booknow=Toplevel(root)
    Booknow.geometry("2000x2000")

    txtadlt = adlt.get()
    txtchild=child.get()
    txtinf=inf.get()
    txtclass1=class1.get()
    txtentry1=entrymail.get()
    txtentry2=entryname.get()
    txtopt1=clicked1.get()
    txtopt2=clicked2.get()

    if(txtopt2=="Jaipur"):
        destinyfac=1.5
    elif (txtopt2=="Delhi"):
        destinyfac=1.4
    elif (txtopt2=="Mumbai"):
        destinyfac=1.4
    elif (txtopt2=="Bangalore"):
        destinyfac=1.7
    elif (txtopt2=="Kolkata"):
        destinyfac=1.6
    elif (txtopt2=="Dubai"):
        destinyfac=5
    elif (txtopt2=="Singapore"):
        destinyfac=6
    elif (txtopt2=="Phillipines"):
        destinyfac=4
    else:
        destinyfac=0

    if(txtclass1=="Premium Economy"):
        classfac=3
    elif(txtclass1=="Economy"):
        classfac=1
    elif(txtclass1=="Business Class"):
        classfac=6
    else:
        classfac=0
        
    if(int(txtchild)!=0):
        childfac=0.5
    else:
        childfac=0

    price = (int(txtchild)*childfac*destinyfac*classfac*2000)+(int(txtadlt)*destinyfac*classfac*2000)
   
    image_path1 = "C:/Users/iamka/Downloads/Airlinenew2.jpg"
    image1 = Image.open(image_path1)
    photo = ImageTk.PhotoImage(image1)
    label1 = Label(Booknow, image=photo)
    label1.image1 = photo
    label1.place(x=360,y=180)
 
    Confirmed = Message(Booknow, text="TICKET CONFIRMED", font="500", fg="BLACK", width=500, bd=6, relief="solid")

    Adults = Label(Booknow, text="Adults", fg="BLACK", width=10,relief = "solid",height=2)
    Adult1 = Label(Booknow, text=txtadlt, fg="BLACK", width=5,relief = "solid",height=2)
    
    Children = Label(Booknow, text="Children", fg="BLACK", width=10,relief = "solid",height=2)
    Child1 = Label(Booknow, text=txtchild, fg="BLACK", width=5,relief = "solid",height=2)
    
    Infants=Label(Booknow,text="Infants",fg="BLACK",width=10,relief = "solid",height=2)
    Inf1=Label(Booknow,text=txtinf,fg="BLACK",width=5,relief = "solid",height=2)
    
    Class1=Label(Booknow,text=txtclass1,width=15,relief = "solid",height=2)
    FlyToLabel=Label(Booknow,text=txtopt1,width=20,relief = "solid",height=2)
    FlyFromLabel=Label(Booknow,text=txtopt2,width=20,relief = "solid",height=2)
    
    labelhead=Label(Booknow,text='FLY HIGH AIRLINES',bd=10,fg='Black' ,bg="#7092bf",font=("algerian",20),width=15)
    labelhead.place(x=490, y=190)
    labelcharges=Label(Booknow,text='CHARGES',bd=10,fg='Black' ,bg="#7092bf",font=("Times New Roman",15),width=15)
    labelcharges.place(x=960, y=190)
    labelname=Label(Booknow,text='Name :  '+txtentry1,bd=10,bg='white',fg='Black' ,font=("Times New Roman",13),width=20,anchor="w")
    labelname.place(x=375,y=250)
    labelemail=Label(Booknow,text='Email : '+txtentry2,bd=10,bg='white',fg='Black' ,font=("Times New Roman",13),width=20,anchor="w")
    labelemail.place(x=375, y=280)

    labelfrom=Label(Booknow,text='From :  '+txtopt1,bd=10,bg='white',fg='Black' ,font=("Times New Roman",13),width=20,anchor="w")
    labelfrom.place(x=375,y=350)
    labelto=Label(Booknow,text='To :  '+txtopt2,bd=10,bg='white',fg='Black' ,font=("Times New Roman",13),width=20,anchor="w")
    labelto.place(x=375, y=380)

    labelclass=Label(Booknow,text='Class : '+txtclass1,bd=10,bg='white',fg='Black' ,font=("Times New Roman",13),width=20,anchor="w")
    labelclass.place(x=375, y=450)

    labeladlt=Label(Booknow,text='Adults : '+ txtadlt,bd=10,bg='white',fg='Black' ,font=("Times New Roman",13),width=15,anchor="w")
    labeladlt.place(x=960, y=250)
    labelchild=Label(Booknow,text='Children : '+ txtchild,bd=10,bg='white',fg='Black' ,font=("Times New Roman",13),width=15,anchor="w")
    labelchild.place(x=960, y=280)
    labelinf=Label(Booknow,text='Infants : '+ txtinf,bd=10,bg='white',fg='Black' ,font=("Times New Roman",13),width=15,anchor="w")
    labelinf.place(x=960, y=310)
    labeprice=Label(Booknow,text='Total Fair : '+ str(price) +"Rs.",bd=10,bg='white',fg='Black' ,font=("Times New Roman",13),width=18,anchor="w")
    labeprice.place(x=960, y=340)
    
    Datefromlabel=Label(Booknow,text="",bd=10,fg='Black' ,bg='white',font=("Times New Roman",17 ),width=10,anchor="w")
    Datefromlabel.config(text="Date:  \n  "+ cal1.get_date())
    Datefromlabel.place(x=530,y=350)
    
    
    ans = cal1.get_date()
    num = int(txtadlt)+int(txtchild)+int(txtinf)
    
    def confirmtkt():
     
        conn = pymysql.connect( user='Karan', password='root', host='localhost', database='airlines' )      
        cursor = conn.cursor()
        sql = """ INSERT INTO ticket (name, email, dates, Departure, Arrival, class1, num,charges ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """
        cursor.execute(sql, (txtentry1, txtentry2, ans, txtopt1, txtopt2, txtclass1, num, price))
        conn.commit()
        cursor.close()
        conn.close()
        
    buttontkt= Button(Booknow, text= "Confirm Ticket", command= confirmtkt,relief='solid',bd=1,width=35,height = 3,bg="thistle3")
    buttontkt.place(x = 670,y =600)
   
#USER INTERFACE

labelhead=Label(root,text='FLY HIGH ! BOOK YOUR HAPPINESS !',bd=10,relief=RIDGE,fg='white' ,bg='#2F2F4F',font=("algerian",30))
labelhead.place(x=425, y=20)

labelcentre=Label(root,bd=1,bg='thistle2',height=27,width=77)
labelcentre.place(x=500,y=200)

labelleft=Label(root,bd=1,bg="thistle4",height=38,width=60)
labelleft.place(x=37,y=200)

labelright=Label(root,bd=1,bg="thistle4",height=38,width=60)
labelright.place(x=1079,y=200)

labelbottom=Label(root,bd=1,bg="thistle4",height=9,width=77)
labelbottom.place(x=500,y=635)

arrivallable=Label(root,text='DEPARTURE',bd=1,bg="#BCBCEE",relief='solid',width=73,height=2)
arrivallable.place(x=515,y=296)

labelframe1 = LabelFrame(root,bg="#363664" ,height=70,width=200,font=('algerian',1),fg='gold',bd=2,relief=RIDGE)
labelframe1.place(x=0,y=110,relwidth=10)

label33= Label(root, text=txt, font=('algerian' ,30, "bold"), fg='white',bg="#363664")
label33.pack(pady=120)

slider()

labelname = Label(root, text = "Name",width=35,bg='#BCBCEE',relief='solid',bd=1,height=2).place(x = 512,y = 210)  
labelemail = Label(root, text = "Email Address",width=35,bg='#BCBCEE',relief='solid',bd=1,height=2).place(x = 780, y = 210)    

classlabel=Label(root,text='Choose Class',bd=1,bg='#BCBCEE',width=58,height=2,relief='solid').place(x=40,y=450)
classlabel1=Label(root,text='Select Number of People',bd=1,bg='#BCBCEE',width=58,height=2,relief='solid').place(x=1086,y=450)

inflable=Label(root,text='Infants',bd=1,relief='solid',width=27,height=3).place(x=1086,y=526)
childlable=Label(root,text='Children',bd=1,relief='solid',width=27,height=3).place(x=1086,y=606)
adultlable=Label(root,text='Adults',bd=1,relief='solid',width=27,height=3).place(x=1086,y=686)

bookbutton=Button(root, text= "Book The Flight",width=60,height=5, command=Book,relief='solid',bd=1)
bookbutton.place(x = 555,y =660)

image_path = "C:/Users/iamka/Downloads/Screenshot 2024-12-12 130225.png"  # Replace with your image path
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

label = Label(root, image=photo,height=220,width=365) 
label.place(x=65,y=212)

create_widgets()
root.mainloop()


