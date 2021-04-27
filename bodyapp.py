from tkinter import *
from tkinter import filedialog
import os
import csv
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
import serial
import datetime
import time
from datetime import date
from datetime import datetime
from datetime import timedelta
import smtplib
from email.message import EmailMessage


#khi ket hop voi maindisplay nho tat root=TK, ser =serial...,class main
root = Tk()

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0)

class bodyapp():

    db_name = 'qlsvlab.db'
    def __init__(self,win,ser):
        self.ser=ser
        
        self.win=win
        self.win.title("Lab Manage 21")
        self.win.geometry('1280x720-300+200')
        self.win.configure(bg='SlateGray')
        #self.win.resizable(width=False,height=False)
    #Thứ tự các frame ở đây quan trọng
        self.allframe()
        self.frameone()
        self.framethree()
        self.fr2home()
        self.fr2chat()
        self.fr2hd()
        self.fr2dangki()
        self.fr2manage()
        self.fr2save()
        self.frameao1()
        self.frameao2()
        self.apidata()
        self.apidata_basic()
        self.fln = ''
        self.saveaddress =[]
        print('Start nao nao....')
        self.s = StringVar()
        self.s1 = StringVar()
        self.s2 = StringVar()
        self.s3 = StringVar()
        self.s4 = StringVar()
        self.s5 = StringVar()
        self.s6 = StringVar()
        global is_on
        is_on = True
        
        #s = ttk.Style()
        
        style = ttk.Style()
        style.theme_use("alt")
        style.configure("Treeview",
            background = "Orange1",
            foreground = "#000000",
            rowheight=25,
            fieldbackground = "LightCyan1"
            )      
        style.map("Treeview",
            background=[("selected","Purple")],
            foreground = [("selected","DarkGoldenrod1")]
            )
        style.configure('Treeview', font=('Arial 12 '),rowheight=40)
        
       
        #self.win.frame2dangki=LabelFrame(self.win,text="Đăng kí thẻ",fg="white",font='Helve 18 bold',bg="SlateGray",width=300,relief="raised")
        self.win.after(60,self.min)

 
    def allframe(self):
        self.framebig=LabelFrame(self.win,bg="#123036")
        self.framebig.pack()
    def min(self):
        
        thing = self.ser.readline().decode('ascii')
        #thing = self.ser.readline()      
        v=str(thing)
        #print('v=',v)
       
        self.s.set(v)
        self.win.after(300, self.min)
        conn = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
        call = conn.cursor()
        if len(str(v))>0 :

            '''
            unix = time.time()
            dateerror = datetime.now()
            date = dateerror.fromtimestamp(unix).strftime("%Y-%m-%d %H:%M:%S")
            '''
            # l = "69 4D FE B3" 
            dateerror = datetime.now()
            date = dateerror.strftime("%Y-%m-%d %H:%M:%S")
        

            l=str(v)
            print('id=',l)
            self.id1.delete(0,END)
            self.browseimage.place_forget()
            self.ht.delete(0,END)
            self.mssv1.delete(0,END)
            self.nhom1.delete(0,END)
            self.gt.delete(0,END)
            self.bh.delete(0,END)   
            self.email1.delete(0,END)  
            self.sdt1.delete(0,END)
            self.id1.insert(0,l)   
            self.email1.insert(0,'@gmail.com')  
            self.gt.insert(0,'Nam')
            self.bh.insert(0,'2000')
            #print(self.id1)
            #self.browseimage2=Label(self.frame2dangki)
            #self.browseimage2.place(x=240,y=40)
            call.execute(f"SELECT * FROM mnlab WHERE id= '{l}'")
    
            for row in call.fetchall():     
                #print(row)
                z=row[0]
                a=row[1]    
                b=row[2]    
                c=row[3]
                print('c la: ',c)
                d=row[4]    
                e=row[5]    
                f=row[6]
                g=row[7]    
                h=row[8]
                k=row[10]
                #print('Db la: ',k)
                
                self.gt.delete(0,END)
                self.email1.delete(0,END) 
                self.bh.delete(0,END)
                self.ht.insert(0,b)
                self.mssv1.insert(0,c)
                self.nhom1.insert(0,d)
                self.gt.insert(0,e)
                self.bh.insert(0,f)    
                self.email1.insert(0,g)    
                self.sdt1.insert(0,h)
                if self.ht=='':
                    self.saveinfo['state'] = NORMAL
                else:
                    self.editthe['state'] = NORMAL

                #self.browseimage.place_forget()
                call.execute(f"SELECT * FROM qltime ")
                for time in call.fetchall():
                    hour = time[0]
                    minute = time[1]
                    second = time[2]
                g = datetime.now() + timedelta(hours=int(hour)) + timedelta(minutes=int(minute)) + timedelta(seconds=int(second))
                g = g.strftime("%Y-%m-%d %H:%M:%S")

 
                if k == '':
                    k='/media/vudat/New Volume/Laptrinh/Python/GUI/working/Boapp/unnamed.png'
                 
                    
                    self._img= ImageTk.PhotoImage((Image.open(k)).resize((38, 38), Image.ANTIALIAS))
                    #print('k ko co:')
        
                    #####Cua frame dang ki
                    # img.thumbnail((250,350))
                    '''
                    if self.mssv1 =='':
                        #print('mssv = rong')
                        self.browseimage.place_forget()
                    else:
                        self.img = Image.open(k)
                        self.resized = self.img.resize((195,210),Image.ANTIALIAS)
                        self.img = ImageTk.PhotoImage(self.resized)
                        self.browseimage.configure(image=self.img)
                        self.browseimage.image = self.img
                    '''
                    self.img = Image.open(k)
                    self.resized = self.img.resize((195,210),Image.ANTIALIAS)
                    self.img = ImageTk.PhotoImage(self.resized)
                    self.browseimage.configure(image=self.img)
                    self.browseimage.image = self.img
                    #self.browseimage.place_forget()
                    self.browseimage.place(x=240,y=40)
                    
                else:
                    ####Cua frame hd
                    
                    #self.img = ImageTk.PhotoImage(Image.open(k))
                    image = Image.open(k)
                    # The (450, 350) is (height, width)
                    image = image.resize((38, 38), Image.ANTIALIAS)
                    self._img = ImageTk.PhotoImage(image)
                    
                
                    #self._img= ImageTk.PhotoImage((Image.open(k)).resize((38, 38), Image.ANTIALIAS))


                    self.img = Image.open(k)
                    #####Cua frame dang ki
                    # img.thumbnail((250,350))
                    self.resized = self.img.resize((195,210),Image.ANTIALIAS)
                    self.img = ImageTk.PhotoImage(self.resized)
                    self.browseimage.configure(image=self.img)
                    self.browseimage.image = self.img
                    self.browseimage.place(x=240,y=40)
                    
                  
                call.execute("SELECT * FROM hoatdong WHERE timeoff > CURRENT_TIMESTAMP() AND time REGEXP(CURRENT_DATE())")
                demsv = 0
                for row2 in call.fetchall():
                    #print('row2: ',row2)
                    demsv +=1
                    ms_sv = row2[2]
                    ti_me = row2[4]
                    ho_ten = row2[1]
                    time_off =  row2[6]

                    #print('ti_me: ',ti_me)
                    #print('mssv: la',ms_sv)
                    if ms_sv == c:
                        # - timedelta(seconds=1)
                        timeoff = datetime.now()
                        timeoff = timeoff.strftime("%Y-%m-%d %H:%M:%S")
                        call.execute(f"UPDATE hoatdong SET timeoff = '{timeoff}' WHERE mssv = '{c}' and timeoff > CURRENT_TIMESTAMP()")
                        call.execute("commit")

                        for child in self.tree2.get_children():
                            quet1 = self.tree2.item(child)["values"]
                            tg = quet1[5]
                        
                            if ti_me == tg:
                    
                                self.tree2.delete(child)

                                for child3 in self.tree4.get_children():
                                    xoatree4 = self.tree4.item(child3)["values"]
                                    print('xoa tree4: ',xoatree4[1])

                                    #if ho_ten == xoatree4[1]:
                                        #self.tree4.delete(child3)
                                    if ms_sv == xoatree4[1]:
                                        self.tree4.delete(child3)
                                        
                                    else:
                                        pass
                                    print('hd_timehd_time la: ',ti_me)
                                call.execute(f"DELETE FROM hoatdongtemp WHERE time = '{ti_me}'")
                                call.execute("commit")

                                call.execute(f"SELECT * FROM hoatdong WHERE mssv ='{c}'AND time REGEXP(CURRENT_DATE()) ORDER BY time DESC LIMIT 1")
                                #SELECT * FROM hoatdong WHERE timeoff > CURRENT_TIMESTAMP() AND time REGEXP(CURRENT_DATE()) AND mssv ='{c}'
                                ############ SAI cho nay
                                for row5 in call.fetchall():
                                        
                                    hd_id5=row5[0]        
                                    hd_ht5=row5[1]
                                    hd_ms5=row5[2]
                                    hd_nhom5=row5[3]
                                    hd_time5=row5[4]
                                    hd_sl5=row5[5] 
                                    hd_timeoff5=row5[6]
                        
                                self.tree2.insert(parent='',index='end',text="",values=(hd_sl5, hd_id5,hd_ht5,hd_ms5,hd_nhom5,hd_time5,hd_timeoff5))
                                #############Them
                                '''
                                for clearoneline in self.tree2.get_children():
                                    xoaonetree2 = self.tree2.item(clearoneline)["values"]
                                    #print('xoaonetree2: ',xoaonetree2)
                                    for rowdelete in xoaonetree2:
                                        #print('xoaonetree2[3]: ',xoaonetree2[3])
                                        if xoaonetree2[3] == c and rowdelete[6] =='':
                                            self.tree2.delete(rowdelete)
                                            print('Delete them sucessfully')
                                '''

                #print('dem sv la: ', demsv)
                self.slsv = Label(self.frame2hd, text = int(demsv)+1, bg='LightCyan1',fg = "Brown",font=('Arial 14 bold'))  
                self.slsv.place_forget()              
                self.slsv.place(x=520,y=110)


                call.execute("insert into hoatdong values('"+ a +"','"+ b +"','"+ c +"','"+ d +"','"+ date +"','""','"+g+"')")
                
                call.execute("SELECT * FROM hoatdong WHERE (timeoff > CURRENT_TIMESTAMP() AND time REGEXP(CURRENT_DATE())) ORDER BY timeoff DESC LIMIT 1")
                
                for row2 in call.fetchall():
                    #print('row2: ',row2)
                    ms_sv = row2[2]
                    ti_me = row2[4]
                    ho_ten = row2[1]
                    time_off =  row2[6]
                call.execute("insert into hoatdongtemp values('"+ a +"','"+ b +"','"+ date +"','"+ ms_sv +"','%s')"%(self._img))

                #call.execute("""insert into hoatdongtemp (id,hoten,time,timeoff,addressimg) values(%s,%s,%s,%s,%s)""",(a,b,date,time_off,self._img))


                call.execute("commit")

                hoatdong = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
                callhd = hoatdong.cursor()
        
                dateerror = datetime.now()
                date = dateerror.strftime("%Y-%m-%d %H:%M:%S")
            
                #date = dateerror
                hoatdong.commit()
                callhd.execute(f"SELECT * FROM hoatdong WHERE id= '{l}' AND time REGEXP(CURRENT_DATE()) ORDER by time ASC")
                dem = 0
                tgend = []
                tgstart =[]
                records = callhd.fetchall()
                for row1 in records:
                    dem +=1
                    ssw = dem
                    
                    h=row1[0]    
                    ll=row1[1]  
                    self.publicten=row1[0]
                    vu=row1[2]
                    dat=row1[3]  

                    timestart = row1[4]
                    timeend = row1[6]
                    tgend.append(timeend)
                    tgstart.append(timestart)
                #print('tgend : ',tgend)
                #print('tgstart : ',tgstart)
                callhd.execute(f"UPDATE hoatdong SET solan = '{ssw}' ORDER BY time DESC LIMIT 1")
                callhd.execute("commit")
            
                #self.tree4.insert(parent='',index='end',text="",image=img2,values=(l))
               
                # Insert image to #0 
        
                #file='tuiohoinghi.jpg'
                self.thongbaoten = Label(self.frame2hd,text='...'+ll+' vừa vào phòng',bg='SteelBlue2',fg='#FFCC00',font=('Helve 20 bold'),width=50)
               
                self.thongbaoten.place(x=100,y=10)
        
                self.tree4.insert(parent='',index='end',text="",image= self._img,values=(ll,vu))
                self.tree2.insert(parent='',index='end',text="",values=(ssw, h,ll,vu,dat,date))
          
                self.saveaddress.append(self._img)

                


                callhd.execute("insert into luuanhhd values('"+ str(self.saveaddress) +"','"+h+"','"+vu+"')")
                callhd.execute("commit")
                '''
                callhd.execute(f"SELECT * FROM mailcontent WHERE nhom ='{self.tendetaisend.get()}' and date REGEXP(CURRENT_DATE())")
                
                for content in callhd.fetchall():
                    maildetai = content[0]
                    #print('id sai: ',his_id)
                    mailchude = content[1]
                    #print('hoten sai: ',his_hoten)
                    mailnoidung = content[2]
                    #print('mssv sai: ',his_mssv)
                    maildate = content[3]
                '''

                #self.saveaddress.split('<')
                print('saveaddreass : ',self.saveaddress)
                '''
                callhd.execute(f"SELECT * FROM hoatdongtemp where id ='{l}'")
                for imghdtemp in callhd.fetchall():
                    uiui = imghdtemp[4].append(self._img)
                    print('imghdtemp[4] :',uiui)
                    callhd.execute(f"UPDATE hoatdongtemp SET addressimg = '{uiui}' where id ='{l}'")
                    callhd.execute("commit")
                '''
                for tgs in tgstart:
                    for tge in tgend:
                        if abs(int(tgs[-2:]) - int(tge[-2:])) < 2 and tgs[:-2] == tge[:-2]:
                            print('time start: ',tgs)
                            print('time end: ',tge)

                            callhd.execute(f"SELECT * FROM hoatdong WHERE time ='{tgs}'AND time REGEXP(CURRENT_DATE())")
                            for tree4_cl1 in callhd.fetchall(): 
                                   
                                hd_ht_tree4=tree4_cl1[1]
                                hd_time_tree4=tree4_cl1[4]
                                hd_mssv_tree4=tree4_cl1[2]
                                for tglegend2 in self.tree4.get_children():
                                    cl_tglegend2 = self.tree4.item(tglegend2)["values"]

                                    if hd_ht_tree4 == cl_tglegend2[0]:
                                        print('ho ten la: ',hd_ht_tree4)
                                        print('time lucsau la: ',hd_time_tree4)
                                        self.tree4.delete(tglegend2)
                                        
                                        self.thongbaoten = Label(self.frame2hd,text='...'+ho_ten+' đã rời phòng',bg='SteelBlue2',fg='#FFCC00',font=('Helve 20 bold'),width=50)
               
                                        self.thongbaoten.place(x=100,y=10)
                                        demsvhd=0
                                        callhd.execute("SELECT * FROM hoatdong WHERE timeoff > CURRENT_TIMESTAMP() AND time REGEXP(CURRENT_DATE())")
                                        for demsvhdne in callhd.fetchall():
                                            demsvhd +=1
                                        
                                        self.slsv = Label(self.frame2hd, text = int(demsvhd)-1, bg='LightCyan1',fg = "Brown",font=('Arial 14 bold'))                
                                        self.slsv.place_forget()
                                        self.slsv.place(x=520,y=110)

                                        callhd.execute(f"DELETE FROM luuanhhd WHERE mssv = '{hd_mssv_tree4}'")
                                        callhd.execute("commit")
                                        
                                        
                                    else:
                                        pass
                                #print('hd_timehd_time la: ',hd_time)
                                callhd.execute(f"DELETE FROM hoatdongtemp WHERE time = '{tgs}'")
                                callhd.execute("commit")
                                

                            callhd.execute(f"DELETE FROM hoatdong WHERE time = '{tgs}'")
                            callhd.execute("commit")
                            hoatdong.close()
                            for tglegend in self.tree2.get_children():
                                cl_tglegend = self.tree2.item(tglegend)["values"]
                                tg = cl_tglegend[5]
                                if tgs == tg:
                                    self.tree2.delete(tglegend)
                                else:
                                    pass
                            #Vuong cho nay 

                        else:
                            pass

  

                g = datetime.now() + timedelta(hours=1)
                g = g.strftime("%Y-%m-%d %H:%M:%S")
                    #self.win.after(1000,self.id1)
                #sendmail
                #print('aa: ',self.ghicontent.get(1.0,'end-1c'))
                #print('bb: ',self.ghisub.get())
                if is_on == True:
                    msg = EmailMessage()
                    
                    #msg['Subject'] = 'Toi yeu ban'
                    msg['From'] = "lab204bk@gmail.com"
                    callhd.execute(f"SELECT * FROM mnlab where id ='{l}'")
                    for mail in callhd.fetchall():
                        gmail = mail[7]
                        tendetai = mail[11]
                        print('gmail la: ',gmail)
                    msg['To'] = str(gmail)
                    callhd.execute(f"SELECT * FROM mailcontent where detai ='{tendetai}'and tinhtrang='Already'")
                    for guimail in callhd.fetchall():

                    
                        msg.set_content(guimail[2])

                        msg['Subject'] = guimail[1]

                # Send the message via our own SMTP server.
                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    server.login("lab204bk@gmail.com", "lab204bk123456")
                    server.send_message(msg)
                    print('Gui thanh cong')
                    server.quit()
                else:
                    
                    pass
                
                self.quetthanhcong()
                
                self.top4.after(1500,self.turnoffquet)
    def quetthanhcong(self):
        
        self.top4 = Toplevel()
        self.top4.geometry("300x200-800+450")
        self.top4.title("Tình trạng quét")
        print('dangquet ne')
        self.top4.configure(bg='WhiteSmoke')
        quetthanhcong = Label(self.top4, text = 'QUÉT THÀNH CÔNG',bg='WhiteSmoke',fg='#00AA00',font=('Helve 18 bold'))
        quetthanhcong.place(x=14,y=60)
    def turnoffquet(self):
        self.top4.withdraw()
  
    def frameone(self):
        
        self.frame1=LabelFrame(self.framebig,text="Danh mục",fg="white",font='Helve 12 bold',bg="DeepSkyBlue4",width=112,height=1220,relief="raised")
        self.frame1.pack(side=LEFT)
        self.but_login=Button(self.frame1,text="Trang chủ",width=8,height=3,bg='Firebrick4',fg='white',font='Arial 12 bold',command=self.fr2_1).place(x=5,y=40)
        self.but_login1=Button(self.frame1,text="Tài liệu",width=8,height=3,bg='Firebrick4',fg='white',font='Arial 12 bold',command=self.fr2_2).place(x=5,y=150)
        self.but_login2=Button(self.frame1,text="Hoạt động\nhằng ngày",width=8,height=3,bg='Firebrick4',fg='white',font='Arial 12 bold',command=self.fr2_3).place(x=5,y=260)
        self.but_login3=Button(self.frame1,text="Đăng kí\nthẻ",width=8,height=3,bg='Firebrick4',fg='white',font='Arial 12 bold',command=self.fr2_ao1).place(x=5,y=370)
        self.but_login4=Button(self.frame1,text="Quản lí\nsinh viên",width=8,height=3,bg='Firebrick4',fg='white',font='Arial 12 bold',command=self.fr2_ao2).place(x=5,y=480)
        self.but_login5=Button(self.frame1,text="Lưu trữ",width=8,height=3,bg='Firebrick4',fg='white',font='Arial 12 bold',command=self.fr2_6).place(x=5,y=590)

    def nhapcong(self):
        
        toplevel = Toplevel(self.win)
        wd2 = inputport(toplevel)
    def settg(self):
        self.thietlapnote['state'] = NORMAL
        ngay = self.ngay.get()
        thang = self.thang.get()
        nam = self.nam.get()
        gio = self.gio2.get()
        phut = self.phut2.get()
        giay = self.giay2.get()
        global text6
        text6 = self.textnote.get(1.0, "end-1c")
        if(gio =="" or phut=="" or giay =="" or ngay =="" or thang =="" or nam =="" or text6==""):
            MessageBox.showinfo("Nhắc nhở","Điền đầy đủ thông tin - Trống viết '00'")
        else:
            con = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
            cursor = con.cursor()
         

            cursor.execute(f"insert into timenotehome (noidung,ngay,thang,nam,gio,phut,giay) values('{text6}','{ngay}','{thang}','{nam}','{gio}','{phut}','{giay}')")
            #cursor.execute(f"Update timenotehome set noidung = '{text}',ngay='{ngay}', thang='{thang}',nam='{nam}',gio='{gio}',phut='{phut}',giay='{giay}'")
            cursor.execute("commit")
            
     
            MessageBox.showinfo("Insert Status","Inserted Successfully")
            #self.top2.withdraw()
            self.top8.destroy()
            print('haha')
    def settimenote(self):
        
        self.top8 = Toplevel()
        self.top8.geometry("500x500-600+300")
        self.top8.title("Đăng kí")
        self.top8.configure(bg='#FFFF99')


        kgtgoff=Label(self.top8,text="Khoảng thời gian off",fg="black",font=("Arial","18","bold"),bg="#FFFF99")
        kgtgoff.place(x=160,y=90)
       
        time=Label(self.top8,text='TIME',fg="red",font=("Arial","25","bold"),bg="#FFFF99").place(x=16,y=180)
        labelngay=Label(self.top8,text='Ngày',fg="red",font=("Arial","18","bold"),bg="#FFFF99").place(x=140,y=150)
        labelthang=Label(self.top8,text='Tháng',fg="red",font=("Arial","18","bold"),bg="#FFFF99").place(x=250,y=150)
        labelnam=Label(self.top8,text='Năm',fg="red",font=("Arial","18","bold"),bg="#FFFF99").place(x=360,y=150)

        labelhour=Label(self.top8,text='Giờ',fg="red",font=("Arial","18","bold"),bg="#FFFF99").place(x=140,y=250)
        labelminute=Label(self.top8,text='Phút',fg="red",font=("Arial","18","bold"),bg="#FFFF99").place(x=250,y=250)
        labelsecond=Label(self.top8,text='Giây',fg="red",font=("Arial","18","bold"),bg="#FFFF99").place(x=360,y=250)

        thietlap= Button(self.top8,text='Thiết lập',width=16,bg='SteelBlue2',fg="black",command=self.settg, font=("Arial","12","bold") )
        thietlap.place(x=180,y=450)
        self.ngay=Entry(self.top8,width=6,font=('Arial 25 bold'))
        self.ngay.place(x=100,y=180)
        #hour.insert('00')
        self.thang=Entry(self.top8,width=6,font=('Arial 25 bold'))
        self.thang.place(x=220,y=180)
        self.nam=Entry(self.top8,width=6,font=('Arial 25 bold'))
        self.nam.place(x=340,y=180)

        self.gio2=Entry(self.top8,width=4,font=('Arial 25 bold'))
        self.gio2.place(x=120,y=290)
        #hour.insert('00')
        self.phut2=Entry(self.top8,width=4,font=('Arial 25 bold'))
        self.phut2.place(x=240,y=290)
        self.giay2=Entry(self.top8,width=4,font=('Arial 25 bold'))
        self.giay2.place(x=360,y=290)

        today = date.today() 

       
        self.gio2.insert(0,23)
        self.phut2.insert(0,59)
        self.giay2.insert(0,59)
        self.ngay.insert(0,today.day)
        self.thang.insert(0,today.month)
        self.nam.insert(0,today.year)
        #self.deadline = datetime(self.nam.get(),self.thang.get(),self.ngay.get(),self.gio2.get(),self.phut2.get(),self.giay2.get()) 

    def setnote(self):
        #deadline = datetime(int(self.nam.get()),int(self.thang.get()),int(self.ngay.get()),int(self.gio2.get()),int(self.phut2.get()),int(self.giay2.get()))
       
        con = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
        calltime = con.cursor()
        calltime.execute(f"SELECT * FROM timenotehome where noidung ='{text6}'")
        for thongtin in calltime.fetchall():
            noidung = thongtin[0]
            ngay = thongtin[1]
            thang = thongtin[2]
            nam = thongtin[3]
            gio = thongtin[4]
            phut = thongtin[5]
            giay = thongtin[6]
        print('gio la: ',gio)


        deadline = datetime(int(nam),int(thang),int(ngay),int(gio),int(phut),int(giay)) 

        con = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
        cursor = con.cursor()
        

        cursor.execute(f"insert into ghichu (noidung,deadline) values('{text6}','{deadline}')")
        #cursor.execute(f"Update timenotehome set noidung = '{text}',ngay='{ngay}', thang='{thang}',nam='{nam}',gio='{gio}',phut='{phut}',giay='{giay}'")
        cursor.execute("commit")
        
    
        
        #deadline = datetime(int(str(nam)),int(str(thang)),int(str(ngay)),int(str(gio)),int(str(phut)),int(str(giay))) 
        print('deadline la: ',deadline)
    
        self.tree6.insert(parent='',index='end',text="",values=(noidung,deadline))
        MessageBox.showinfo("Insert Status","Inserted Successfully")
    def delenote(self):
        dele = self.tree6.selection()
        if MessageBox.askyesno("Bạn Chắc chắn xóa","Delete tất cả những mục bạn đã chọn ?"):
        
            for rm in dele:
                datarm = self.tree6.item(rm)["values"]
                print(self.tree6.item(rm)["values"])
                #self.tree2.delete(rm)

                for detree6 in self.tree6.get_children():
                    data4rm = self.tree6.item(detree6)["values"]
                    print('datarm[1]: ',datarm[1])
                    print('data4rm[1]): ',data4rm[1])
                    if datarm[1] == data4rm[1]:
                        
                        self.tree6.delete(detree6)
                    else:
                        pass   

                print('Thoi gian xoa la: ',data4rm[1])
                rmhd = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")

                cursorrm = rmhd.cursor()
                #cursorrm.execute(f"SELECT MAX(time) FROM (SELECT *  FROM hoatdongtemp WHERE time REGEXP(CURRENT_DATE()) ORDER BY time LIMIT {rm2}) as T1")
                #cursorrm.execute(f"SELECT MAX(time) FROM (SELECT *  FROM hoatdong WHERE time REGEXP(CURRENT_DATE()) ORDER BY time LIMIT {rm2}) as T1")

                cursorrm.execute(f"DELETE FROM ghichu WHERE deadline = '{datarm[1]}'")
                cursorrm.execute("commit")
              

            MessageBox.showinfo("Delete Status","Deleted Successfully")
    def quaylaythe(self):
        pass
    def fr2home(self):
       
        self.frame2home=LabelFrame(self.framebig,text="Home",fg="black",font='Helve 12 bold',bg="SteelBlue2",width=1700,height=1220,relief="raised")
        self.frame2home.pack(side=RIGHT)

        vanmay = Label(self.frame2home,text='Vận may mỗi ngày',bg='SteelBlue2',fg='red',font=('Arial 16  bold'))
        vanmay.place(x=600,y=15)
        labelnote = Label(self.frame2home,text='Ghi chú',bg='SteelBlue2',fg='red',font=('Arial 12 bold'))
        labelnote.place(x=100,y=400)
        deadlinenote = Button(self.frame2home,text='Đặt Time',bg='green',fg='white',font=('Arial 12 bold'),command=self.settimenote)
        deadlinenote.place(x=350,y=400)

        delenote = Button(self.frame2home,text='Delete',bg='red',fg='white',font=('Arial 12 bold'),command=self.delenote)
        delenote.place(x=1200,y=400)

        thuvanmay = Button(self.frame2home,text='Quay lấy thẻ',bg='red',fg='white',font=('Arial 12 bold'),command=self.quaylaythe)
        thuvanmay.place(x=600,y=300)



        labelnotemoi = Label(self.frame2home,text='(Mời bạn nhập text)',bg='SteelBlue2',fg='black',font=('Arial 8 italic bold'))
        labelnotemoi.place(x=100,y=420)

        self.textnote=Text(self.frame2home,width=30,height=15,font=('Arial 18 bold'))
        self.textnote.place(x=100,y=440)


        self.thietlapnote = Button(self.frame2home,text='Thiết lập',bg='green',fg='black',font=('Arial 12  bold'),command=self.setnote,state = DISABLED)
        self.thietlapnote.place(x=530,y=560)

    
        


        self.framenote=Frame(self.frame2home,width=15,height=10)
        
        self.framenote.place(x=650,y=440)
        self.tree6 = ttk.Treeview(self.framenote,column=(1,2),show="headings",height="10")
        #Treeview phải nằm left, srcollbar nằm right thì nó mới khít frame
        self.tree6.pack(side=LEFT)
        self.tree6.heading(1,text='Nội dung',anchor=CENTER)
        self.tree6.column(1,width=400,anchor=CENTER)

        self.tree6.heading(2, text="Deadline",anchor=CENTER)
        self.tree6.column(2,width=250,anchor=CENTER)

 

        #configure the scrollbar
        self.scrolltable6 = Scrollbar(self.framenote,orient="vertical",command=self.tree6.yview)
        #self.scrolltable.place(x=215,y=400,relx=100)
        #self.scrolltable.grid(row=4,column=3,padx=250,pady=380,sticky="ns")
        self.scrolltable6.pack(side=RIGHT,fill=Y)
        self.tree6.config(yscroll=self.scrolltable6.set)
        #self.tree2.bind('<ButtonRelease-1>', self.select_item)
  



    def update_clock(self):
        date_time = time.strftime("%A, %d/%m/%Y, %H:%M:%S")
    
        self.my_clock.configure(text=date_time)
        self.my_clock.place(x=300,y=50)
        
        self.my_clock.after(1000, self.update_clock)
    def setmail(self):
        setmail = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
        contentmail = setmail.cursor()
        dateerror = datetime.now()
        date = dateerror.strftime("%Y-%m-%d %H:%M:%S")
        #date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        contentmail.execute("insert into mailcontent values('"+ self.tendetaisend.get() +"','"+ self.ghisub.get() +"','"+ self.ghicontent.get("1.0",END) +"','"+ date +"','Already')")
        contentmail.execute("commit")
        #contentmail.execute(f"SELECT * FROM mailcontent WHERE detai ='{self.tendetaisend.get()}' and date REGEXP(CURRENT_DATE()) and tinhtrang ='Already'")

        contentmail.execute(f"SELECT * FROM mailcontent WHERE detai ='{self.tendetaisend.get()}' and date REGEXP(CURRENT_DATE()) and tinhtrang ='Already' ORDER BY date DESC LIMIT 1")
       
        for content in contentmail.fetchall():
            maildetai = content[0]
            #print('id sai: ',his_id)
            mailchude = content[1]
            #print('hoten sai: ',his_hoten)
            mailnoidung = content[2]
            #print('mssv sai: ',his_mssv)
            maildate = content[3]
            mailtinhtrang = content[4]

         

            self.tree5.insert(parent='',index='end',text="",values=(maildetai, mailchude, mailnoidung,maildate,mailtinhtrang))
        contentmail.execute(f"SELECT * FROM mailcontent WHERE detai ='{self.tendetaisend.get()}' and date REGEXP(CURRENT_DATE()) and tinhtrang ='Already' ORDER BY date ASC LIMIT 1")
       
        for content2 in contentmail.fetchall():
    
            maildate2 = content2[3]
            for child in self.tree5.get_children():
                xoathietlap = self.tree5.item(child)["values"]
                if xoathietlap[3] == maildate2:
                    self.tree5.delete(child)
        contentmail.execute(f"Update mailcontent set tinhtrang='Busy' where detai ='{self.tendetaisend.get()}' and tinhtrang = 'Already' ORDER BY date ASC LIMIT 1")
        contentmail.execute("commit")
        MessageBox.showinfo("Insert Status","Insert Successfully")

    def clicktree5(self,event):
        self.editmail['state'] = NORMAL
        
    def okeditchude(self):
        self.top6.withdraw()
        selectchude = self.tree5.selection()
        geteditchude = self.entryedit4.get()
        
        print('noi dung la: ',geteditchude)
        for changechude in selectchude:
                #arraytree = self.tree2.get_children()
                
            datachange = self.tree5.item(changechude)["values"]
            

            print('mail la2: ',self.tree5.item(changechude)["values"])
            print('chude la: ',datachange[1])
            con = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
            cursor = con.cursor()
            
            cursor.execute(f"Update mailcontent set chude='{geteditchude}' where date='{datachange[3]}'")
            cursor.execute("commit")
            cursor.execute(f"SELECT * FROM mailcontent where date ='{datachange[3]}' ")

            for date in cursor.fetchall():
                if date[3] == datachange[3]:
                    print('date la: ',date)
                    
                    self.tree5.delete(changechude)
        MessageBox.showinfo("Update Status","Update Successfully")
        conn = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
        call = conn.cursor()
        call.execute(f"SELECT * FROM mailcontent where date ='{datachange[3]}' order by tinhtrang='Already' DESC")
        
        for insert in call.fetchall():
            dt = insert[0]
            cd = insert[1]
            nd = insert[2]
            date = insert[3]
            tt = insert[4]

   
               
            
            
            self.tree5.insert(parent='',index='end',text="",values=(dt,cd,nd,date,tt))
        conn.close()
    def okeditnoidung(self):
        self.top7.withdraw()
        selectnoidung = self.tree5.selection()
        geteditnoidung = self.entryedit5.get(1.0, "end-1c")
        
        print('noi dung la: ',geteditnoidung)
        for changenoidung in selectnoidung:
                #arraytree = self.tree2.get_children()
                
            datachange2 = self.tree5.item(changenoidung)["values"]
            

            print('mail la2: ',self.tree5.item(changenoidung)["values"])
            print('noidung la: ',datachange2[2])
            con2 = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
            cursor2 = con2.cursor()
            print('cho nay on')
            cursor2.execute(f"Update mailcontent set noidung='{geteditnoidung}' where date='{datachange2[3]}'")
            cursor2.execute("commit")
            cursor2.execute(f"SELECT * FROM mailcontent where date ='{datachange2[3]}'")

            for date in cursor2.fetchall():
                if date[3] == datachange2[3]:
                    print('date la: ',date)
                    
                    self.tree5.delete(changenoidung)
        MessageBox.showinfo("Update Status","Update Successfully")
        conn = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
        call = conn.cursor()
        call.execute(f"SELECT * FROM mailcontent where date ='{datachange2[3]}' order by tinhtrang='Already' DESC")
        
        for insert in call.fetchall():
            dt = insert[0]
            cd = insert[1]
            nd = insert[2]
            date = insert[3]
            tt = insert[4]
   
               
            
            
            self.tree5.insert(parent='',index='end',text="",values=(dt,cd,nd,date,tt))
        conn.close()
    def editchude(self):
        self.top5.withdraw()
        self.top6 = Toplevel()
        self.top6.geometry("300x200-700+450")
        self.top6.title("Nội dung chỉnh sửa")
        self.top6.configure(bg='SteelBlue2')
        labeledit4=Label(self.top6,text='Nhập nội dung\n chỉnh sửa',bg = 'SteelBlue2',fg='DodgerBlue4',font=('Arial 18 bold'))
        labeledit4.place(x=55,y=15)
        self.entryedit4=Entry(self.top6,width=25,font=('Arial 12 bold'))
        self.entryedit4.place(x=30,y=120)
        okeedit4 = Button(self.top6,text='Đồng ý',bg = 'DodgerBlue4',width=10,fg='white',font=('Arial 12 bold'),command=self.okeditchude)
        okeedit4.place(x=85,y=160)
        
    def editnoidung(self):
        self.top5.withdraw()
        self.top7 = Toplevel()
        self.top7.geometry("700x500-500+350")
        self.top7.title("Nội dung chỉnh sửa")
        self.top7.configure(bg='SteelBlue2')
        labeledit5=Label(self.top7,text='Nhập nội dung\n chỉnh sửa',bg = 'SteelBlue2',fg='DodgerBlue4',font=('Arial 18 bold'))
        labeledit5.place(x=280,y=15)
        self.entryedit5=Text(self.top7,width=40,height=15,font=('Arial 12 bold'))
        self.entryedit5.place(x=170,y=120)
        okeedit5 = Button(self.top7,text='Đồng ý',bg = 'DodgerBlue4',width=10,fg='white',font=('Arial 12 bold'),command=self.okeditnoidung)
        okeedit5.place(x=290,y=440)
    def editmail(self):
        
        self.top5 = Toplevel()
        self.top5.geometry("300x300-700+400")
        self.top5.title("Chọn mục chỉnh sửa")
        self.top5.configure(bg='SkyBlue4')
        labeledit=Label(self.top5,text='CHỌN MỤC CẦN\n CHỈNH SỬA',bg = 'SkyBlue4',fg='white',font=('Arial 18 bold'))
        labeledit.place(x=50,y=20)
        editchude = Button(self.top5,text='Chỉnh sửa mục "Chủ đề"',bg = 'snow1',width=20,fg='red',font=('Arial 12 bold'),command=self.editchude)
        editchude.place(x=50,y=120)
        editnoidung = Button(self.top5,text='Chỉnh sửa mục\n "Nội dung"',width=20,bg = 'snow1',fg='red',font=('Arial 12 bold'),command=self.editnoidung)
        editnoidung.place(x=50,y=200)
    def searchtree5(self,events):
        banphim = 'Okela'
        if banphim == 'Okela':
            seatree5 = self.ensearchmail.get()
            #print('chu nhan duoc: ',seatree2)
            searchmail = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
            callsearchmail = searchmail.cursor()       
            callsearchmail.execute(f"SELECT * FROM mailcontent WHERE (detai LIKE '%{seatree5}%' or chude LIKE '%{seatree5}%' or noidung LIKE '%{seatree5}%' or date LIKE '%{seatree5}%') ORDER BY date DESC ")
            
            self.tree5.delete(*self.tree5.get_children())

            for seamail in callsearchmail.fetchall():
            
                detai = seamail[0]
                chude = seamail[1]
                noidung = seamail[2]
                date = seamail[3]
                tinhtrang = seamail[4]

                
                self.tree5.insert(parent='',index='end',text="",values=(detai,chude,noidung,date,tinhtrang))
        else:
            #self.tree2.after(500, self.searchtree2)
            pass
        '''
            cursordata.execute(f"SELECT * FROM mailcontent WHERE detai ='{detai}' and tinhtrang ='Already' ORDER BY date ASC LIMIT 1")

            for content in cursordata.fetchall():
                print('date ss la: ',date)
                print('content ss la: ',content)

                if date == content[3]:
        '''
    def addmail(self):
        selectaddmail = self.tree5.selection()
        if MessageBox.askyesno("Thay đổi tình trạng","Bạn chọn thay thế nội dung cũ để gửi ?"):
        
            for slmail in selectaddmail:

                dataadd = self.tree5.item(slmail)["values"]
                print(self.tree5.item(slmail)["values"])
                #self.tree5.delete(slmail)
                print('slmail la:', slmail)
                detai = dataadd[0]
                print('detai la ',detai)
                date = dataadd[3]
                print('date la ' ,date)

            

                con = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
                cursor = con.cursor()
   
                cursor.execute(f"Update mailcontent set tinhtrang='Busy' where detai='{detai}'")
                cursor.execute("commit")
                cursor.execute(f"Update mailcontent set tinhtrang='Already' where date='{date}'")
                cursor.execute("commit")
                #MessageBox.showinfo("Insert Status","Insert Successfully")
                

            
        self.tree5.delete(*self.tree5.get_children())
        dataaddmail = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
        cursoradddata = dataaddmail.cursor()
        cursoradddata.execute("SELECT * FROM mailcontent order by tinhtrang='Already' DESC")
       
        for content in cursoradddata.fetchall():
            maildetai = content[0]
            #print('id sai: ',his_id)
            mailchude = content[1]
            #print('hoten sai: ',his_hoten)
            mailnoidung = content[2]
            #print('mssv sai: ',his_mssv)
            maildate = content[3]
            mailtt = content[4]

         

            self.tree5.insert(parent='',index='end',text="",values=(maildetai, mailchude, mailnoidung,maildate,mailtt))
        MessageBox.showinfo("Insert Status","Insert Successfully")
    def switch(self):
        global is_on
        # Co tac dong vao switch thi false
        if is_on:
            self.onbutton.config(image=self.off)
            is_on = False
            self.frame2chat.configure(bg='#303036',fg='white')
            self.nguoinhanlabel.configure(bg='#303036',fg='white')
            self.ghisublabel.configure(bg='#303036',fg='white')
            self.ghicontentlabel.configure(bg='#303036',fg='white')
            self.searchmail.configure(bg='#303036',fg='white')
            self.tatmail = Label(self.frame2chat,text='Đã tắt gửi mail',font=('Arial 12 bold'),bg='#303036',fg='white',width=15)
            self.tatmail.place(x=812,y=120)
        # Khong tac dong vao switch thi True
        else:
            self.onbutton.config(image=self.on)
            self.frame2chat.configure(bg='SteelBlue2',fg="black")
            self.nguoinhanlabel.configure(bg='SteelBlue2',fg='#000055')
            self.ghisublabel.configure(bg='SteelBlue2',fg='#000055')
            self.ghicontentlabel.configure(bg='SteelBlue2',fg='#000055')
            self.searchmail.configure(bg='SteelBlue2',fg='#000055')
            self.batmail = Label(self.frame2chat,text='Đã bật gửi mail',font=('Arial 12 bold'),bg='SteelBlue2',fg='black',width=15)
            self.batmail.place(x=812,y=120)
            is_on = True   
    def fr2chat(self):
        self.frame2chat=LabelFrame(self.framebig,text="Tài liệu",fg="black",font='Helve 12 bold',bg="SteelBlue2",width=1600,height=1220,relief="raised")
        #tennhom2 = [1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005]
        tendetai =[]
        conn = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
        call = conn.cursor()
        call.execute("SELECT * FROM mnlab")
        for detai in call.fetchall():
            #print('tennhom ',nhom[4])
            tendetai.append(detai[11])
        
        tendetai2 = sorted(set(tendetai))
        print('Ten de tai la: ',tendetai2)
        
        self.tendetaisend = ttk.Combobox(self.frame2chat, value = tendetai2,width=10)
        self.tendetaisend.current(0)
        #self.gt.bind("<<ComboboxSelected>>", self.combogtclick)
        self.tendetaisend.place(x=200,y=50)
        
        
        self.ghisub = Entry(self.frame2chat,width=50,font=('Arial 12'))
        self.ghisub.place(x=200,y=80)
        self.nguoinhanlabel = Label(self.frame2chat,text='Đề tài',font=('Arial 12 bold'),bg="SteelBlue2",fg='#000055')
        self.nguoinhanlabel.place(x=120,y=50)
        self.ghisublabel = Label(self.frame2chat,text='Chủ đề',font=('Arial 12 bold'),bg="SteelBlue2",fg='#000055')
        self.ghisublabel.place(x=120,y=80)
        self.ghicontent = Text(self.frame2chat,height=12,width=50,font=('Arial 12'))
        self.ghicontent.place(x=200,y=110)
        self.ghicontentlabel = Label(self.frame2chat,text='Nội dung',font=('Arial 12 bold'),bg="SteelBlue2",fg='#000055')
        self.ghicontentlabel.place(x=120,y=110)

        self.setmail = Button(self.frame2chat,text='Thiết lập',font=('Arial 12 bold'),bg="#000099",fg='white',command=self.setmail)
        self.setmail.place(x=400,y=350)

        self.searchmail = Label(self.frame2chat,text='Search',font=('Arial 12 bold'),bg="SteelBlue2",fg='#000055')
        self.searchmail.place(x=160,y=470)
        self.ensearchmail = Entry(self.frame2chat,width=14,font=('Arial 12'))
        self.ensearchmail.place(x=220,y=470)

        self.editmail = Button(self.frame2chat,text='Edit',font=('Arial 10 bold'),bg="#000099",fg='white',command=self.editmail,state = DISABLED)
        self.editmail.place(x=550,y=468)
        self.addmail = Button(self.frame2chat,text='Add',font=('Arial 10 bold'),bg="#000099",fg='white',command=self.addmail)
        self.addmail.place(x=365,y=468)

        self.frametl5=Frame(self.frame2chat,width=30,height=6)
    
        self.frametl5.place(x=150,y=500)
       
        self.tree5 = ttk.Treeview(self.frametl5,column=(1,2,3,4,5),show="headings",height="10")
        #Treeview phải nằm left, srcollbar nằm right thì nó mới khít frame
        self.tree5.pack(side=LEFT)
       
        self.tree5.heading(1, text="Đề tài",anchor=CENTER)
        self.tree5.column(1,width=100,anchor=CENTER)

        self.tree5.heading(2, text="Chủ đề",anchor=CENTER)
        self.tree5.column(2,width=145,anchor=CENTER)

        self.tree5.heading(3, text="Nội dung",anchor=CENTER)
        self.tree5.column(3,width=175,anchor=CENTER)

        self.tree5.heading(4, text="Date",anchor=CENTER)
        self.tree5.column(4,width=155,anchor=CENTER)

        self.tree5.heading(5, text="Tình trạng",anchor=CENTER)
        self.tree5.column(5,width=155,anchor=CENTER)

        

        
        #configure the scrollbar
        self.scrolltable5 = Scrollbar(self.frametl5,orient="vertical",command=self.tree5.yview)

        self.scrolltable5.pack(side=RIGHT,fill=Y)
        self.tree5.config(yscroll=self.scrolltable5.set)
         
        self.tree5.bind("<Button-1>",self.clicktree5)
        self.ensearchmail.bind("<KeyRelease>",self.searchtree5)
    #    frame2chat.pack(side=LEFT,ipadx=320,ipady=500)

        

        
        self.imgon = Image.open("/media/vudat/New Volume/Laptrinh/Python/GUI/working/Boapp/onyes.png")
        self.resizedon = self.imgon.resize((150,60),Image.ANTIALIAS)
        self.on = ImageTk.PhotoImage(self.resizedon)

        self.imgoff = Image.open("/media/vudat/New Volume/Laptrinh/Python/GUI/working/Boapp/offno.png")
        self.resizedoff = self.imgoff.resize((150,60),Image.ANTIALIAS)
        self.off = ImageTk.PhotoImage(self.resizedoff)

        self.onbutton = Button(self.frame2chat,image=self.on,bd =0,command=self.switch)
        self.onbutton.place(x=800,y=50)
        self.batmail2 = Label(self.frame2chat,text='Đã bật gửi mail',font=('Arial 12 bold'),bg='SteelBlue2',fg='black',width=15)
        self.batmail2.place(x=812,y=120)
    def searchtree2(self,event):
        banphim = 'Okela'
        if banphim == 'Okela':
            seatree2 = self.ensearchhd.get()
            #print('chu nhan duoc: ',seatree2)
            searchhd = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
            callsearchhd = searchhd.cursor()       
            callsearchhd.execute(f"SELECT * FROM hoatdong WHERE (time REGEXP(CURRENT_DATE())) and (id LIKE '%{seatree2}%' or hoten LIKE '%{seatree2}%' or mssv LIKE '%{seatree2}%' or nhom LIKE '%{seatree2}%' or solan LIKE '%{seatree2}%'or time LIKE '%{seatree2}%') ORDER BY time ASC ")
            
            self.tree2.delete(*self.tree2.get_children())

            for seahd in callsearchhd.fetchall():
            
                hd_sl=seahd[5]     
                hd_id=seahd[0]        
                hd_ht=seahd[1]
                hd_ms=seahd[2]
                hd_nhom=seahd[3]
                hd_time=seahd[4]
                hd_timeoff=seahd[6]

                
                self.tree2.insert(parent='',index='end',text="",values=(hd_sl, hd_id,hd_ht,hd_ms,hd_nhom,hd_time,hd_timeoff))
        else:
            #self.tree2.after(500, self.searchtree2)
            pass
    def clicktree2(self,event):
        self.removehd['state'] = NORMAL
    
    def removehd(self):
        self.frame2ao3=LabelFrame(self.frame2hd,text="Đăng nhập để tiếp tục",fg="white",font='Helve 12 bold',bg="SteelBlue2",width=1600,height=1220,relief="raised")
        self.frame2ao3.pack(side=RIGHT)
        self.matkhau_s=Label(self.frame2ao3,text='Mật khẩu',fg="black",font=("Arial","14","bold"),bg="SteelBlue2").place(x=200,y=240)
        
        self.matkhau_s2=Entry(self.frame2ao3,show="*")
        self.matkhau_s2.place(x=300,y=240)
        #tai khoan
        self.taikhoan_s=Label(self.frame2ao3,text='Tài khoản',fg="black",font=("Arial","14","bold"),bg="SteelBlue2").place(x=200,y=180)
        
        self.taikhoan_s2=Entry(self.frame2ao3)
        self.taikhoan_s2.place(x=300,y=180)
        
        self.portNo = StringVar()

        #self.Labelh_s=Label(self.frame2ao1,text='Ex: /dev/ttyACM0',fg="black",font=("Helve","10","bold"),bg="#CB356B").place(x=310,y=330)
        #self.entry1_s1=Entry(self.frame2ao1,textvariable=self.portNo).place(x=300,y=300)
        
        #self.nhapcong_s=Label(self.frame2ao1,text='Tên cổng Arduino',fg="black",font=("Helve","14","bold"),bg="#CB356B").place(x=125,y=300)
        self.Button1_s2= Button(self.frame2ao3,text='Đăng nhập',width=16,bg='green',fg="white",command=self.signinfrhd, font=("Helve","12","bold") )
        self.Button1_s2.place(x=300,y=360)

        '''
        for child in self.tree2.get_children():
            print(self.tree2.item(child)["values"])
        '''
 
    def signinfrhd(self):
        try:
            
            com = self.portNo.get()
            #ser = serial.Serial(com, 9600, timeout=0)
            print('Serial port is open')
            #self.frame2hd.pack_forget()
            log = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
            
            user=self.taikhoan_s2.get()
            passw=self.matkhau_s2.get()
            
            print('user:',self.taikhoan_s2)
            print('password:',self.matkhau_s2)
            cur = log.cursor()
            query = "SELECT username,password FROM login"
            cur.execute(query)
            
            for (userr,passs) in cur:
                if user==userr and passw==passs:
                    login = True
                    if login ==True:
                        print('Login thành công')
        
                        self.frame2dangki.pack_forget()
                        self.frame2ao1.pack_forget()
                        self.frame2ao3.pack_forget()
                        self.frame2chat.pack_forget()
                        self.frame2home.pack_forget()
                       
                        self.frame2ao2.pack_forget()
                        self.frame2manage.pack_forget()
                        self.frame2save.pack_forget()
                
                        self.matkhau_s2.delete(0,'end')
                       ###################### Clear Database Code ############
                        dele = self.tree2.selection()
                        if MessageBox.askyesno("Bạn Chắc chắn xóa","Delete tất cả những mục bạn đã chọn ?"):
                        
                            for rm in dele:
                                arraytree = self.tree2.get_children()
                                for reindex in range(len(self.tree2.get_children())):
                                    if arraytree[reindex] == rm:
                                        posit = reindex + 1
                                        print('stt la: ',posit)
                                    else:
                                        pass
                                datarm = self.tree2.item(rm)["values"]
                                

                                print(self.tree2.item(rm)["values"])
                                self.tree2.delete(rm)

                                for tree4 in self.tree4.get_children():
                                    data4rm = self.tree4.item(tree4)["values"]
                                    print('datarm[1]: ',datarm[2])
                                    print('data4rm[1]): ',data4rm[1])
                                    if datarm[2] == data4rm[1]:
                                        
                                        self.tree4.delete(tree4)
                                    else:
                                        pass   
                                rm2 = datarm[5]
                                print('Thoi gian xoa la: ',rm2)
                                rmhd = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")

                                cursorrm = rmhd.cursor()
                                #cursorrm.execute(f"SELECT MAX(time) FROM (SELECT *  FROM hoatdongtemp WHERE time REGEXP(CURRENT_DATE()) ORDER BY time LIMIT {rm2}) as T1")
                                #cursorrm.execute(f"SELECT MAX(time) FROM (SELECT *  FROM hoatdong WHERE time REGEXP(CURRENT_DATE()) ORDER BY time LIMIT {rm2}) as T1")

                                cursorrm.execute(f"DELETE FROM hoatdong WHERE time = '{rm2}'")
                                cursorrm.execute("commit")

                            MessageBox.showinfo("Delete Status","Deleted Successfully")
                            rmhd.close()
                            ##########################################3
                        
                    break
                else:
                    login = False
                    if login == False:
                        MessageBox.showerror('Cảnh báo','Thông tin đã nhập không chính xác')
                        print("Thông tin đã nhập không chính xác")
                    if user=="" or passw=="":
                        MessageBox.showinfo('Tập trung','Vui lòng nhập thông tin')
                        print("Vui lòng nhập thông tin")                          
        except:
            if user=="" or passw=="":
                MessageBox.showinfo('Tập trung','Vui lòng nhập thông tin')
            else:
                MessageBox.showerror('Cảnh báo','Kiểm tra lại cổng kết nối Arduino')
    def settinghd(self):
        self.sethd= Toplevel(self.win)              
        self.onsethd = caidathd(self.sethd)
    def fr2hd(self):
        self.frame2hd=LabelFrame(self.framebig,text="Hoạt động hằng ngày",fg="black",font='Helve 12 bold',bg="SteelBlue2",width=1600,height=1220,relief="raised")
    #    frame2hd.pack(side=LEFT,ipadx=320,ipady=500)
        self.sethd = Button(self.frame2hd,text="Cài đặt",font=("Arial 10 bold"),width=6,bg="Wheat",command=self.settinghd)
        self.sethd.place(x=30,y=15)

        self.my_clock = Label(self.frame2hd,text="",font=("Arial 14 bold"),width=50,bg="Green1")
        self.update_clock()
        self.ensearchhd = Entry(self.frame2hd)
        self.ensearchhd.place(x=140,y=110)

        self.ensearchhd.bind("<KeyRelease>",self.searchtree2)
        self.svdangonl = Label(self.frame2hd,text = 'Đang trong phòng: ',bg='LightCyan1',fg='#00CC00',font=('Arial 12 bold'))
        self.svdangonl.place(x=350,y=110)
        

        self.lasearchhd = Label(self.frame2hd,text='Search',bg="SteelBlue2",fg="black",font='Arial 12 bold')
        self.lasearchhd.place(x=70,y=110)
        
        self.frameintrohd=Label(self.frame2hd,text="Hoạt động ra vào, thời gian: ",fg="black",font='Arial 16 bold',bg="SteelBlue2")
        self.frameintrohd.place(x=100,y=50)
        self.realframehd=Frame(self.frame2hd,width=30,height=25)
        
        self.realframehd.place(x=20,y=150)
        self.tree2 = ttk.Treeview(self.realframehd,column=(1,2,3,4,5,6,7),show="headings",height="20")
        #Treeview phải nằm left, srcollbar nằm right thì nó mới khít frame
        self.tree2.pack(side=LEFT)
        self.tree2.heading(1,text='lần/ngày',anchor=CENTER)
        self.tree2.column(1,width=80,anchor=CENTER)

        self.tree2.heading(2, text="ID",anchor=CENTER)
        self.tree2.column(2,width=115,anchor=CENTER)

        self.tree2.heading(3, text="Họ tên",anchor=CENTER)
        self.tree2.column(3,width=175,anchor=CENTER)

        self.tree2.heading(4, text="MSSV",anchor=CENTER)
        self.tree2.column(4,width=100,anchor=CENTER)

        self.tree2.heading(5, text="Nhóm",anchor=CENTER)
        self.tree2.column(5,width=70,anchor=CENTER)

        self.tree2.heading(6, text="Thời gian vào")
        self.tree2.column(6,width=165,anchor=CENTER)
        self.tree2.heading(7,text='Thời gian off')
        self.tree2.column(7,width=165,anchor=CENTER)
        #configure the scrollbar
        self.scrolltable = Scrollbar(self.realframehd,orient="vertical",command=self.tree2.yview)
        #self.scrolltable.place(x=215,y=400,relx=100)
        #self.scrolltable.grid(row=4,column=3,padx=250,pady=380,sticky="ns")
        self.scrolltable.pack(side=RIGHT,fill=Y)
        self.tree2.config(yscroll=self.scrolltable.set)
        #self.tree2.bind('<ButtonRelease-1>', self.select_item)
        self.treeview = self.tree2
        self.tree2.bind("<Button-1>",self.clicktree2)
        
       
            
        #self.removehd = Button(self.frame2hd,text="Xóa",bg = "Brown3",fg="white",command=self.removehd,font=('Arial 12 bold'),width=10)
        self.removehd = Button(self.frame2hd,text="Delete",bg = "Brown3",fg="white",command=self.removehd,font=('Arial 12 bold'),width=10,state = DISABLED)
   
        self.removehd.place(x=800,y=100)

        #self.searchtree2()
        
    def goanh(self):
        
        if MessageBox.askyesno("Bạn Chắc chắn xóa","Gỡ bỏ Avatar ?"): 
            MessageBox.showinfo("Update Status","Update Successfully\n Bấm nút 'Cập nhật' để hoàn tất")
            self.browseimage.place_forget()
    def combogtclick(self):
        pass
    def fr2dangki(self):
        #dinh nghia frame2
        
        self.frame2dangki=LabelFrame(self.framebig,text="Đăng kí thẻ",fg="black",font='Helve 12 bold',bg="SteelBlue2",width=1600,height=1220,relief="raised")
        self.realframe=Frame(self.frame2dangki,width=300,height=150)
        #self.realframe.pack(side=BOTTOM,pady=20)
        self.realframe.place(x=200,y=380)
        #broswimg
        self.browseimg=Label(self.frame2dangki,width=24,height=12)
        self.browseimg.place(x=240,y=40)
        self.browseimage=Label(self.frame2dangki)
        self.browseimage.place(x=240,y=40)
        #putbi    

        self.picsave=Button(self.frame2dangki,text="Browse",command=self.browse,bg='green',fg="white",font='Helve 10 bold')
        self.picsave.place(x=300,y=275)
        self.picremove=Button(self.frame2dangki,text="Gỡ ảnh",command=self.goanh,bg='red',fg="white",font='Helve 8 bold')
        self.picremove.place(x=306,y=248)
        #saveinfo
        
        
        self.saveinfo=Button(self.frame2dangki,text="Tạo mới",bg='green',fg="white",width=10,font='Helve 10 bold',command=self.savemysql,state = DISABLED)
        self.saveinfo.place(x=750,y=275)
        #editthe
        self.editthe=Button(self.frame2dangki,text="Cập nhật",bg='green',fg="white",width=10,font='Helve 10 bold',command=self.editdata,state = DISABLED)
        self.editthe.place(x=480,y=275)
        #remove
        self.remove=Button(self.frame2dangki,text="Gỡ bỏ thẻ",bg='red',fg="white",width=8,font='Helve 10 bold',command=self.remove)
        self.remove.place(x=600,y=275)
        self.hoten=Label(self.frame2dangki,text="Họ tên",fg="black",bg="SteelBlue2",font='Helve 10 bold')
        self.hoten.place(x=480,y=20)
        self.ht=Entry(self.frame2dangki,width=25,bg="#EEEEEE")
        self.ht.place(x=480,y=40)
        #birth
        self.birth=Label(self.frame2dangki,text="Năm sinh",fg="black",font='Helve 10 bold',bg="SteelBlue2")
        self.birth.place(x=750,y=20)

        optionnamsinh = [1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005]

        #myComboday
        self.bh = ttk.Combobox(self.frame2dangki, value = optionnamsinh,width=14)
        self.bh.current(0)
        #self.gt.bind("<<ComboboxSelected>>", self.combogtclick)
        self.bh.place(x=748,y=40)

        '''
        self.bh=Entry(self.frame2dangki,width=15,bg="#EEEEEE")
        self.bh.place(x=750,y=40)
        '''
        #gioitinh
        self.gioitinh=Label(self.frame2dangki,text="Giới tính",fg="black",font='Helve 10 bold',bg="SteelBlue2")
        self.gioitinh.place(x=480,y=80)
        optionsgt = ['Nam','Nữ']

        #myComboday
        self.gt = ttk.Combobox(self.frame2dangki, value = optionsgt,width=24)
        self.gt.current(0)
        #self.gt.bind("<<ComboboxSelected>>", self.combogtclick)
        self.gt.place(x=478,y=100)
        '''
        self.gt=Entry(self.frame2dangki,width=25,bg="#EEEEEE")
        self.gt.place(x=480,y=100)
        '''
        self.mssv=Label(self.frame2dangki,text="MSSV (Bắt buộc)",fg="black",font='Helve 10 bold',bg="SteelBlue2")
        self.mssv.place(x=750,y=80)
        self.mssv1=Entry(self.frame2dangki,width=15,bg="#EEEEEE")
        self.mssv1.place(x=750,y=100)
        

        self.nhom=Label(self.frame2dangki,text="Nhóm",fg="black",font='Helve 10 bold',bg="SteelBlue2")
        self.nhom.place(x=480,y=140)
        self.nhom1=Entry(self.frame2dangki,width=25,bg="#EEEEEE")
        self.nhom1.place(x=480,y=160)

        self.id=Label(self.frame2dangki,text="My ID",fg="black",font='Helve 10 bold',bg="SteelBlue2")
        self.id.place(x=750,y=140)
        self.id1=Entry(self.frame2dangki,width=15,bg="#EEEEEE")
        self.id1.place(x=750,y=160)

        self.sdt=Label(self.frame2dangki,text="Số điện thoại",fg="black",font='Helve 10 bold',bg="SteelBlue2")
        self.sdt.place(x=480,y=195)
        self.sdt1=Entry(self.frame2dangki,width=25,bg="#EEEEEE")
        self.sdt1.place(x=480,y=220)

        self.email=Label(self.frame2dangki,text="Email",fg="black",font='Helve 10 bold',bg="SteelBlue2")
        self.email.place(x=750,y=195)
        self.email1=Entry(self.frame2dangki,width=15,bg="#EEEEEE")
        
        self.email1.place(x=750,y=220)
        #treeview scrollbar
        
       
        #tree
        self.tree = ttk.Treeview(self.realframe,column=(1,2,3,4,5),show="headings",height="12")
        #Treeview phải nằm left, srcollbar nằm right thì nó mới khít frame
        self.tree.pack(side=LEFT)
       
        

        self.tree.heading(1, text="STT")
        self.tree.column(1,width=70)

        self.tree.heading(2, text="ID")
        self.tree.column(2,width=145)

        self.tree.heading(3, text="Họ tên")
        self.tree.column(3,width=175)

        self.tree.heading(4, text="MSSV")
        self.tree.column(4,width=155)

        self.tree.heading(5, text="Thời gian")
        self.tree.column(5,width=155)
        #configure the scrollbar
        self.scrolltable = Scrollbar(self.realframe,orient="vertical",command=self.tree.yview)
        #self.scrolltable.place(x=215,y=400,relx=100)
        #self.scrolltable.grid(row=4,column=3,padx=250,pady=380,sticky="ns")
        self.scrolltable.pack(side=RIGHT,fill=Y)
        self.tree.config(yscroll=self.scrolltable.set)
        
        self.win.after(60,self.min)    

        #kich thuoc table neu ko hieu se che di noi dung
    def searchtree3(self,event):
        banphim = 'Okela'
        if banphim == 'Okela':
            seatree3 = self.ensearchmn.get()
            #print('chu nhan duoc: ',seatree3)
            searchmn = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
            callsearchmn = searchmn.cursor()       
            callsearchmn.execute(f"SELECT * FROM mnlab WHERE stt LIKE '%{seatree3}%' or id LIKE '%{seatree3}%' or hoten LIKE '%{seatree3}%' or mssv LIKE '%{seatree3}%' or nhom LIKE '%{seatree3}%' or gioitinh LIKE '%{seatree3}%' or namsinh LIKE '%{seatree3}%' or email LIKE '%{seatree3}%' or sdt LIKE '%{seatree3}%' ORDER BY stt ASC")
            self.tree3.delete(*self.tree3.get_children())
            for seamn in callsearchmn.fetchall():
                stt=seamn[0]
                id = seamn[1]
                hten=seamn[2]
                ms=seamn[3]
                nhom=seamn[4]
                gt=seamn[5]
                ns=seamn[6]
                em=seamn[7]
                tel=seamn[8]
                dat=seamn[9]

                self.tree3.insert(parent='',index='end',text="",values=(stt,id, hten, gt, ms, em, tel, nhom, 'chua co'))
        else:
            pass
    '''
    def exportmn(self):
        #dele = self.tree2.selection()
        row = 0
        datafull = []
        for child in self.tree3.get_children():
 
            data = self.tree3.item(child)["values"]
            row += 1
            print('so row la: ',row)
            datafull.append(data)
        print('datafull la: ',datafull)
        if row < 1:
            MessageBox.showerror("No Data","No data available to export")

        else:
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title = "Save CSV", filetypes = (("CSV File", "*.csv"),("All Files","*.*")))
            
            with open(fln, 'a') as myfile:

                exp_writer = csv.writer(myfile, dialect='excel')
                for i in range(len(datafull)):
                   # print('data[i]: ',datafull[i])
                    exp_writer.writerow(datafull[i])
                   # for record in ar:
                     #   exp_writer.writerow(tuple(ar))


            MessageBox.showinfo("Data Exported", "Your data has been exported to "+os.path.basename(fln)+" successfully")
    '''
    def clicktree3(self,event):
        self.editmana['state'] = NORMAL
    def okeditnhomcm(self):
        self.top2.withdraw()
        selectnhom = self.tree3.selection()
        geteditnhom = self.entryedit2.get()
        
        print('noi dung la: ',geteditnhom)
        for changenhom in selectnhom:
                #arraytree = self.tree2.get_children()
                
            datachange = self.tree3.item(changenhom)["values"]
            

            print('ten chon la: ',self.tree3.item(changenhom)["values"])
            print('MSSV la: ',datachange[4])
            con = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
            cursor = con.cursor()
            
            cursor.execute(f"Update mnlab set nhom='{geteditnhom}' where mssv='{datachange[4]}'")
            cursor.execute("commit")
        MessageBox.showinfo("Update Status","Update Successfully")
        conn = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
        call = conn.cursor()
        call.execute("SELECT * FROM mnlab ORDER BY stt ASC")
        for child in self.tree3.get_children():
            self.tree3.delete(child)
        for insertall in call.fetchall():
            stt=insertall[0]
            id = insertall[1]
            hten=insertall[2]
            ms=insertall[3]
            nhom=insertall[4]
            gt=insertall[5]
            ns=insertall[6]
            em=insertall[7]
            tel=insertall[8]
            dat=insertall[9]
            tendetai=insertall[11]
   
               
            
            
            self.tree3.insert(parent='',index='end',text="",values=(stt,id, hten, gt, ms, em, tel, nhom,tendetai))
        con.close()
                
    def okedittdtcm(self):
        self.top3.withdraw()
        selectnhom = self.tree3.selection()
        geteditdetai = self.entryedit3.get()
        
        #print('noi dung la: ',geteditnhom)
        for changenhom in selectnhom:
  
                
            datachange = self.tree3.item(changenhom)["values"]
            

            print('ten chon la: ',self.tree3.item(changenhom)["values"])
            print('MSSV la: ',datachange[4])
            con = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
            cursor = con.cursor()
            
            cursor.execute(f"Update mnlab set tendetai='{geteditdetai}' where mssv='{datachange[4]}'")
            cursor.execute("commit")
        MessageBox.showinfo("Update Status","Update Successfully")

        conn = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
        call = conn.cursor()
        call.execute("SELECT * FROM mnlab ORDER BY stt ASC")
        for child in self.tree3.get_children():
            self.tree3.delete(child)
        for insertall in call.fetchall():
            stt=insertall[0]
            id = insertall[1]
            hten=insertall[2]
            ms=insertall[3]
            nhom=insertall[4]
            gt=insertall[5]
            ns=insertall[6]
            em=insertall[7]
            tel=insertall[8]
            dat=insertall[9]
            tendetai=insertall[11]

            
              
            
            self.tree3.insert(parent='',index='end',text="",values=(stt,id, hten, gt, ms, em, tel, nhom,tendetai))
        self.tendetaisend.after(300, self.fr2chat)
      
        con.close()
    def editnhomcm(self):
        self.top.withdraw()
        self.top2 = Toplevel()
        self.top2.geometry("300x200-700+450")
        self.top2.title("Nội dung chỉnh sửa")
        self.top2.configure(bg='SteelBlue2')
        labeledit2=Label(self.top2,text='Nhập nội dung\n chỉnh sửa',bg = 'SteelBlue2',fg='DodgerBlue4',font=('Arial 18 bold'))
        labeledit2.place(x=55,y=15)
        self.entryedit2=Entry(self.top2,width=25,font=('Arial 12 bold'))
        self.entryedit2.place(x=30,y=120)
        okeedit2 = Button(self.top2,text='Đồng ý',bg = 'DodgerBlue4',width=10,fg='white',font=('Arial 12 bold'),command=self.okeditnhomcm)
        okeedit2.place(x=85,y=160)
    def edittendetaicm(self):
        self.top.withdraw()
        self.top3 = Toplevel()
        self.top3.geometry("300x200-700+450")
        self.top3.title("Nội dung chỉnh sửa")
        self.top3.configure(bg='SteelBlue2')
        labeledit3=Label(self.top3,text='Nhập nội dung\n chỉnh sửa',bg = 'SteelBlue2',fg='DodgerBlue4',font=('Arial 18 bold'))
        labeledit3.place(x=55,y=15)
        self.entryedit3=Entry(self.top3,width=25,font=('Arial 12 bold'))
        self.entryedit3.place(x=30,y=120)
        okeedit3 = Button(self.top3,text='Đồng ý',bg = 'DodgerBlue4',width=10,fg='white',font=('Arial 12 bold'),command=self.okedittdtcm)
        okeedit3.place(x=85,y=160)
    def editmanage(self):
        self.top = Toplevel()
        self.top.geometry("300x300-700+400")
        self.top.title("Chọn mục chỉnh sửa")
        self.top.configure(bg='SkyBlue4')
        labeledit=Label(self.top,text='CHỌN MỤC CẦN\n CHỈNH SỬA',bg = 'SkyBlue4',fg='white',font=('Arial 18 bold'))
        labeledit.place(x=50,y=20)
        editnhom = Button(self.top,text='Chỉnh sửa mục "Nhóm"',bg = 'snow1',width=20,fg='red',font=('Arial 12 bold'),command=self.editnhomcm)
        editnhom.place(x=50,y=120)
        edittendetai = Button(self.top,text='Chỉnh sửa mục\n "Tên đề tài"',width=20,bg = 'snow1',fg='red',font=('Arial 12 bold'),command=self.edittendetaicm)
        edittendetai.place(x=50,y=200)
        
    def fr2manage(self):
        self.frame2manage=LabelFrame(self.framebig,text="Quản lí sinh viên",fg="black",font='Helve 12 bold',bg="SteelBlue2",width=1600,height=1220,relief="raised")
       # self.frame2manage.pack(side=LEFT,ipadx=320,ipady=500)
        self.labelmanage=Label(self.frame2manage,text='Quản lí sinh viên',bg = 'SteelBlue2',fg='SteelBlue2',font=('Arial 18 bold'))
        self.labelmanage.place(x=55,y=30)
        self.realframemn=Frame(self.frame2manage,width=30,height=30)

        self.editmana = Button(self.frame2manage,text="Edit",bg = "Brown3",fg="white",command=self.editmanage,font=('Arial 10 bold'),width=14,state = DISABLED)
   
        self.editmana.place(x=700,y=110)
        self.tongsv = Label(self.frame2manage,text = 'Tổng sinh viên: ',bg='LightCyan1',fg='#00CC00',font=('Arial 12 bold'))
        self.tongsv.place(x=420,y=110)
    
        self.ensearchmn = Entry(self.frame2manage)
        self.ensearchmn.place(x=140,y=110)
        self.ensearchmn.bind("<KeyRelease>",self.searchtree3)
        self.lasearchmn = Label(self.frame2manage,text='Search',bg="SteelBlue2",fg="black",font='Arial 12 bold')
        self.lasearchmn.place(x=70,y=110)

        #self.exportmn = Button(self.frame2manage,text='Export',bg='#DCD800',fg = 'black',font=('Arial 12 bold'),command = self.exportmn)
        #self.exportmn.place(x=600,y=100)
        self.realframemn.place(x=50,y=150)
        self.tree3 = ttk.Treeview(self.realframemn,column=(1,2,3,4,5,6,7,8,9),show="headings",height="20")
        #Treeview phải nằm left, srcollbar nằm right thì nó mới khít frame
        self.tree3.pack(side=LEFT)
       
        self.tree3.heading(1, text="STT")
        self.tree3.column(1,width=70)

        self.tree3.heading(2, text="ID")
        self.tree3.column(2,width=125)

        self.tree3.heading(3, text="Họ tên")
        self.tree3.column(3,width=200)

        self.tree3.heading(4, text="Giới tính")
        self.tree3.column(4,width=100)

        self.tree3.heading(5, text="MSSV")
        self.tree3.column(5,width=155)

        self.tree3.heading(6, text="Email")
        self.tree3.column(6,width=155)

        self.tree3.heading(7, text="SĐT")
        self.tree3.column(7,width=155)

        self.tree3.heading(8, text="Nhóm")
        self.tree3.column(8,width=70)

        self.tree3.heading(9, text="Tên đề tài")
        self.tree3.column(9,width=250)
        #configure the scrollbar
        self.scrolltable = Scrollbar(self.realframemn,orient="vertical",command=self.tree3.yview)
        #self.scrolltable.place(x=215,y=400,relx=100)
        #self.scrolltable.grid(row=4,column=3,padx=250,pady=380,sticky="ns")
        self.scrolltable.pack(side=RIGHT,fill=Y)
        self.tree3.config(yscroll=self.scrolltable.set)
        self.tree3.bind("<Button-1>",self.clicktree3)

    def combodayclick(self,event):
        labelday = Label(self.frame2save,text='Ngày '+self.myCombo.get(),bg='SteelBlue2',fg='white',font=('Helve 12 bold'),width=15).place(x=110,y=150) 
        #print('Ngay combo la',self.myCombo.get())
    def combomonthclick(self,event):
        labelmonth = Label(self.frame2save,text='Tháng '+self.myCombo2.get(),bg='SteelBlue2',fg='white',font=('Helve 12 bold'),width=15).place(x=310,y=150) 
    def comboyearclick(self,event):
        #labelyear = Label(root,text="",width=20,bg='red').place(x=800,y=200)
        labelyear = Label(self.frame2save,text='Năm '+ self.myCombo3.get(),bg='SteelBlue2',fg='white',font=('Helve 12 bold'),width=15).place(x=510,y=150)
    def hisdataapi(self):
        self.treehis.delete(*self.treehis.get_children())
        hisdate = date(int(self.myCombo3.get()),int(self.myCombo2.get()),int(self.myCombo.get()))
        print('ngay la:',hisdate)
        hisdata = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
        calldata = hisdata.cursor()
        unix = time.time()
        #date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        
        hisdata.commit()
        calldata.execute(f"SELECT * FROM hoatdong WHERE time REGEXP('{hisdate}') ORDER BY time ASC")
       
        for hisrow in calldata.fetchall():
            his_id = hisrow[0]
            #print('id sai: ',his_id)
            his_hoten = hisrow[1]
            #print('hoten sai: ',his_hoten)
            his_mssv = hisrow[2]
            #print('mssv sai: ',his_mssv)
            his_nhom = hisrow[3]
            his_time = hisrow[4]
            his_stt = hisrow[5]
           # print('his_stt: ',his_stt)
            
         

         

            self.treehis.insert(parent='',index='end',text="",values=(his_stt, his_id, his_hoten,his_mssv,his_nhom, his_time))
        
    def searchtreehis(self,event):
        banphim = 'Okela'
        if banphim == 'Okela':
            seatreehis = self.ensearchhis.get()
            #print('chu nhan duoc: ',seatree2)
            hisdate = date(int(self.myCombo3.get()),int(self.myCombo2.get()),int(self.myCombo.get()))
            searchhis = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
            callsearchhis = searchhis.cursor()       
            callsearchhis.execute(f"SELECT * FROM hoatdong WHERE (time REGEXP('{hisdate}')) and (id LIKE '%{seatreehis}%' or hoten LIKE '%{seatreehis}%' or mssv LIKE '%{seatreehis}%' or nhom LIKE '%{seatreehis}%' or solan LIKE '%{seatreehis}%'or time LIKE '%{seatreehis}%') ORDER BY time ASC ")
            self.treehis.delete(*self.treehis.get_children())
            for seahis in callsearchhis.fetchall():
            
                hd_sl=seahis[5]     
                hd_id=seahis[0]        
                hd_ht=seahis[1]
                hd_ms=seahis[2]
                hd_nhom=seahis[3]
                hd_time=seahis[4]

                
                self.treehis.insert(parent='',index='end',text="",values=(hd_sl, hd_id,hd_ht,hd_ms,hd_nhom,hd_time))
        else:
            #self.tree2.after(500, self.searchtree2)
            pass
    
    def fr2save(self):
        self.frame2save=LabelFrame(self.framebig,text="Lưu trữ",fg="black",font='Helve 12 bold',bg="SteelBlue2",width=1600,height=1220,relief="raised")
        self.tkluutru=Label(self.frame2save,text="Tìm kiếm lưu trữ",fg='black',bg='SteelBlue2',font=('Arial 16 bold'))
        self.tkluutru.place(x=100,y=50)

        self.ensearchhis = Entry(self.frame2save)
        self.ensearchhis.place(x=750,y=260)
 
        self.ensearchhis.bind("<KeyRelease>",self.searchtreehis)
      

        self.lasearchhis = Label(self.frame2save,text='Search',bg="SteelBlue2",fg="black",font='Arial 12 bold')
        self.lasearchhis.place(x=680,y=260)
        #Tao fullscreen scrollbar
        '''
        #Create A main Frame
        self.main_his = Frame(self.frame2save)
        #self.main_his.pack(fill=BOTH, expand=1)
        self.main_his.place(x=0,y=0)
        #Create canvas
        self.his_canvas = Canvas(self.main_his,width=1515,height=1220,bg='blue')
        self.his_canvas.pack(side=LEFT)
        #self.his_canvas.pack(side=LEFT,fill=BOTH,expand=1)
        #Create self.his_canvas
        self.his_scrollbar = ttk.Scrollbar(self.main_his, orient=VERTICAL, command=self.his_canvas.yview)
        self.his_scrollbar.pack(side=RIGHT,fill=Y)
        # Configure canvas
       
        self.his_canvas.configure(yscrollcommand=self.his_scrollbar.set)
        self.his_canvas.bind('<Configure>',lambda e: self.his_canvas.configure(scrollregion = self.his_canvas.bbox('all')))

        self.second_frame = Frame(self.his_canvas)
        
        self.his_canvas.create_window((100,100), window=self.second_frame, anchor="nw")
        for i in range(100):
            Button(self.second_frame, text="My Button - "+str(i)).pack()
        '''    

        self.day=Label(self.frame2save,text="Ngày",fg='black',bg='SteelBlue2',font=('Helve 10 bold'))
        self.day.place(x=100,y=100)
        self.month=Label(self.frame2save,text="Tháng",fg='black',bg='SteelBlue2',font=('Helve 10 bold'))
        self.month.place(x=300,y=100)
        self.year=Label(self.frame2save,text="Năm",fg='black',bg='SteelBlue2',font=('Helve 10 bold'))
        self.year.place(x=500,y=100)
        self.seehis = Button(self.frame2save,text="Xem lưu trữ",bg='blue',fg='black',font=('Helve 10 bold'),borderwidth=0,command=self.hisdataapi)
        self.seehis.place(x=350,y=200)

        self.hishoatdong=Label(self.frame2save,text="HOẠT ĐỘNG TRONG NGÀY",fg='black',bg='SteelBlue2',font=('Helve 12 bold'))
        self.hishoatdong.place(x=75,y=260)
        
        
        #day
        optionsday = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24
                    ,25,26,27,28,29,30,31]

        #myComboday
        self.myCombo = ttk.Combobox(self.frame2save, value = optionsday,width=10)
        self.myCombo.current(0)
        self.myCombo.bind("<<ComboboxSelected>>", self.combodayclick)
        self.myCombo.place(x=150,y=100)
       
        #month
        optionsmonth = [1,2,3,4,5,6,7,8,9,10,11,12]

        #myCombomonth
        self.myCombo2 = ttk.Combobox(self.frame2save, value = optionsmonth,width=10)
        self.myCombo2.current(0)
        self.myCombo2.bind("<<ComboboxSelected>>", self.combomonthclick)
        self.myCombo2.place(x=360,y=100)
        #year
        optionsyear = [2020,2021,2022,2023,2024,2025,2026,'to be continuted']

        #myComboyear
        self.myCombo3 = ttk.Combobox(self.frame2save, value = optionsyear,width=14)
        self.myCombo3.current(0)
        self.myCombo3.bind("<<ComboboxSelected>>", self.comboyearclick)
        self.myCombo3.place(x=550,y=100)
        
        
        #Table

        self.hisframehd=Frame(self.frame2save,width=30,height=30)
    
        self.hisframehd.place(x=50,y=300)
       
        self.treehis = ttk.Treeview(self.hisframehd,column=(1,2,3,4,5,6),show="headings",height="30")
        #Treeview phải nằm left, srcollbar nằm right thì nó mới khít frame
        self.treehis.pack(side=LEFT)
       
        self.treehis.heading(1, text="Số lần/ngày")
        self.treehis.column(1,width=100)

        self.treehis.heading(2, text="ID")
        self.treehis.column(2,width=145)

        self.treehis.heading(3, text="Họ tên")
        self.treehis.column(3,width=175)

        self.treehis.heading(4, text="MSSV")
        self.treehis.column(4,width=155)

        self.treehis.heading(5, text="Nhóm")
        self.treehis.column(5,width=155)

        self.treehis.heading(6, text="Thời gian vào")
        self.treehis.column(6,width=155)
        #configure the scrollbar
        self.scrolltablehis = Scrollbar(self.hisframehd,orient="vertical",command=self.treehis.yview)

        self.scrolltablehis.pack(side=RIGHT,fill=Y)
        self.treehis.config(yscroll=self.scrolltablehis.set)
        
    def frameao1(self):
        self.frame2ao1=LabelFrame(self.framebig,text="Đăng kí thẻ",fg="white",font='Helve 12 bold',bg="SteelBlue2",width=1600,height=1220,relief="raised")
        self.matkhau_s=Label(self.frame2ao1,text='Mật khẩu',fg="black",font=("Arial","14","bold"),bg="SteelBlue2").place(x=200,y=240)
        
        self.matkhau_s1=Entry(self.frame2ao1,show="*")
        self.matkhau_s1.place(x=300,y=240)
        #tai khoan
        self.taikhoan_s=Label(self.frame2ao1,text='Tài khoản',fg="black",font=("Arial","14","bold"),bg="SteelBlue2").place(x=200,y=180)
        
        self.taikhoan_s1=Entry(self.frame2ao1)
        self.taikhoan_s1.place(x=300,y=180)
        
        self.portNo = StringVar()

        #self.Labelh_s=Label(self.frame2ao1,text='Ex: /dev/ttyACM0',fg="black",font=("Helve","10","bold"),bg="#CB356B").place(x=310,y=330)
        #self.entry1_s1=Entry(self.frame2ao1,textvariable=self.portNo).place(x=300,y=300)
        
        #self.nhapcong_s=Label(self.frame2ao1,text='Tên cổng Arduino',fg="black",font=("Helve","14","bold"),bg="#CB356B").place(x=125,y=300)
        self.Button1_s1= Button(self.frame2ao1,text='Đăng nhập',width=16,bg='green',fg="white",command=self.openport, font=("Helve","12","bold") )
        self.Button1_s1.place(x=300,y=360)
    def openport(self):
        try:
            
            com = self.portNo.get()
            #ser = serial.Serial(com, 9600, timeout=0)
            print('Serial port is open')
            log = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
            
            user=self.taikhoan_s1.get()
            passw=self.matkhau_s1.get()
            
            print('user:',self.taikhoan_s1)
            print('password:',self.matkhau_s1)
            cur = log.cursor()
            query = "SELECT username,password FROM login"
            cur.execute(query)
            
            for (userr,passs) in cur:
                if user==userr and passw==passs:
                    login = True
                    if login ==True:
                        print('Login thành công')
                        self.frame2dangki.pack(side=RIGHT)
                        self.frame2ao1.pack_forget()
                        self.frame2chat.pack_forget()
                        self.frame2home.pack_forget()
                        self.frame2hd.pack_forget()
                        self.frame2ao2.pack_forget()
                        self.frame2manage.pack_forget()
                        self.frame2save.pack_forget()
                       # self.taikhoan_s1.delete(0,'end')
                        self.matkhau_s1.delete(0,'end')
                       
                        
                    break
                else:
                    login = False
                    if login == False:
                        MessageBox.showerror('Cảnh báo','Thông tin đã nhập không chính xác')
                        print("Thông tin đã nhập không chính xác")
                    if user=="" or passw=="":
                        MessageBox.showinfo('Tập trung','Vui lòng nhập thông tin')
                        print("Vui lòng nhập thông tin")                          
        except:
            if user=="" or passw=="":
                MessageBox.showinfo('Tập trung','Vui lòng nhập thông tin')
            else:
                MessageBox.showerror('Cảnh báo','Kiểm tra lại cổng kết nối Arduino')
    def frameao2(self):
        self.frame2ao2=LabelFrame(self.framebig,text="Quản lí sinh viên",fg="white",font='Helve 12 bold',bg="SteelBlue2",width=1600,height=1220,relief="raised")
        
        self.matkhau=Label(self.frame2ao2,text='Mật khẩu',fg="black",font=("Arial","14","bold"),bg="SteelBlue2").place(x=200,y=240)
        
        self.matkhau1=Entry(self.frame2ao2,show="*")
        self.matkhau1.place(x=300,y=240)
        #tai khoan
        self.taikhoan=Label(self.frame2ao2,text='Tài khoản',fg="black",font=("Arial","14","bold"),bg="SteelBlue2").place(x=200,y=180)
        
        self.taikhoan1=Entry(self.frame2ao2)
        self.taikhoan1.place(x=300,y=180)
        
        self.portNo = StringVar()

        #self.Labelh=Label(self.frame2ao2,text='Ex: /dev/ttyACM0',fg="black",font=("Helve","10","bold"),bg="#CB356B").place(x=310,y=330)
        #self.entry1=Entry(self.frame2ao2,textvariable=self.portNo).place(x=300,y=300)
        
        #self.nhapcong=Label(self.frame2ao2,text='Tên cổng Arduino',fg="black",font=("Helve","14","bold"),bg="#CB356B").place(x=125,y=300)
        self.Button1= Button(self.frame2ao2,text='Đăng nhập',width=16,bg='green',fg="white",command=self.openport2, font=("Helve","12","bold") )
        self.Button1.place(x=300,y=360)
    def openport2(self):
        try:
            com = self.portNo.get()
            #ser = serial.Serial(com, 9600, timeout=0)
            print('Serial port is open')
            log = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
           
            user=self.taikhoan1.get()
            passw=self.matkhau1.get()
            
            print('user:',self.taikhoan1)
            print('password:',self.matkhau1)
            cur = log.cursor()
            query = "SELECT username,password FROM login"
            cur.execute(query)
            
            for (userr,passs) in cur:
                if user==userr and passw==passs:
                    login = True
                    if login ==True:
                        print('Login thành công')
                    
                        
                        self.frame2manage.pack(side=RIGHT)
                        self.frame2ao1.pack_forget()
                        self.frame2chat.pack_forget()
                        #self.frame2home.pack_forget()
                        self.frame2hd.pack_forget()
                        self.frame2ao2.pack_forget()
                        self.frame2save.pack_forget()
                        self.matkhau1.delete(0,'end')
                        #self.taikhoan1.delete(0,'end')
                       
                        
                    break
                else:
                  
                    login = False
                    if login == False:
                        MessageBox.showerror('Cảnh báo','Thông tin đã nhập không chính xác')
                        print("Thông tin đã nhập không chính xác")
                  
                    if user=="" or passw=="":
                        MessageBox.showinfo('Tập trung','Vui lòng nhập thông tin')
                        print("Vui lòng nhập thông tin")  
                                   
        except:
            if user=="" or passw=="" or c=="":
                MessageBox.showinfo('Tập trung','Vui lòng nhập thông tin')
            else:
                MessageBox.showerror('Cảnh báo','Kiểm tra lại cổng kết nối Arduino')
    
    def fr2_ao1(self):
        self.frame2ao1.pack(side=RIGHT)
        self.frame2ao2.pack_forget()
        self.frame2home.pack_forget()
        self.frame2chat.pack_forget()
        self.frame2hd.pack_forget()
        self.frame2dangki.pack_forget()
        self.frame2manage.pack_forget()
        self.frame2save.pack_forget()
    def fr2_ao2(self):
        self.frame2ao2.pack(side=RIGHT)
        self.frame2ao1.pack_forget()
        self.frame2home.pack_forget()
        self.frame2chat.pack_forget()
        self.frame2hd.pack_forget()
        self.frame2dangki.pack_forget()
        self.frame2manage.pack_forget()
        self.frame2save.pack_forget()    
    def fr2_1(self):
        self.frame2home.pack(side=RIGHT)
        self.frame2ao2.pack_forget()
        self.frame2ao1.pack_forget()
        self.frame2chat.pack_forget()
        self.frame2hd.pack_forget()
        self.frame2dangki.pack_forget()
        self.frame2manage.pack_forget()
        self.frame2save.pack_forget()
    def fr2_2(self):
        self.frame2chat.pack(side=RIGHT)
        self.frame2home.pack_forget()
        self.frame2ao2.pack_forget()
        self.frame2ao1.pack_forget()
        self.frame2hd.pack_forget()
        self.frame2dangki.pack_forget()
        self.frame2manage.pack_forget()
        self.frame2save.pack_forget()
    def fr2_3(self):
        self.frame2hd.pack(side=RIGHT)
        self.frame2chat.pack_forget()
        self.frame2ao2.pack_forget()
        self.frame2ao1.pack_forget()
        self.frame2home.pack_forget()
        self.frame2dangki.pack_forget()
        self.frame2manage.pack_forget()
        self.frame2save.pack_forget()  
    def fr2_6(self):
        self.frame2save.pack(side=RIGHT)
        self.frame2chat.pack_forget()
        self.frame2ao2.pack_forget()
        self.frame2ao1.pack_forget()
        self.frame2home.pack_forget()
        self.frame2hd.pack_forget()
        self.frame2dangki.pack_forget()
        self.frame2manage.pack_forget()

    def browse(self):
        self.fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",filetypes=(("JPG File","*.jpg"),("PNG file","*.png"),("All Files","*,*")))
        self.img = Image.open(self.fln)
        print('duong dan la: ',self.fln)
        
        # img.thumbnail((250,350))
        self.resized = self.img.resize((195,210),Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.resized)
        self.browseimage.configure(image=self.img)
        self.browseimage.image = self.img
        self.browseimage.place(x=240,y=40)
        '''
        with open (fln, "rb") as f:
            data = f.read()
        imgdata = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
        imginfo = imgdata.cursor()
        imginfo.execute(f"insert into mnlab (id,hoten,mssv,nhom,gioitinh,namsinh,email,sdt,date,image) values('','','','','','','','','','{data}')")
        

        #imginfo.execute("insert into mnlab (id,hoten,mssv,nhom,gioitinh,namsinh,email,sdt,date,image) values('"+ self.id +"','"+ self.hoten +"','"+ self.mssv +"','"+ self.nhom +"','"+ self.gioitinh +"','"+ self.namsinh +"','"+ self.email +"','"+ self.sdt +"','"+ date +"','""')")
        imginfo.execute("commit")
        MessageBox.showinfo("Success!","Update sucessfull")
        '''
    def savemysql(self):
        self.id = self.id1.get()
        self.hoten = self.ht.get()
        self.mssv = self.mssv1.get()
        self.nhom = self.nhom1.get()
        self.gioitinh = self.gt.get()
        self.namsinh = self.bh.get()
        self.email = self.email1.get()
        self.sdt = self.sdt1.get()
        

        if(self.hoten =="" or self.email=="" or self.mssv =="" or self.sdt=="" or self.id==""):
            MessageBox.showinfo("Insert Status","All Fields are required")
        else:
            con = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
            cursor = con.cursor()
            #cursor.execute("insert into mnlab values('"+ self.id +"','"+ self.hoten +"','"+ self.mssv +"','"+ self.nhom +"','"+ self.gioitinh +"','"+ self.namsinh +"','"+ self.email +"','"+ self.sdt +"')")
            '''
            unix = time.time()
            date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
            '''
            dateerror = datetime.now()
            date = dateerror.strftime("%d/%m/%Y %H:%M:%S")
            #cursor.execute("insert into student values('"+ hoten1 +"','"+ email +"','"+ sdt +"','"+ mssv +"','"+ lop +"')")
            cursor.execute("SELECT MAX(stt) FROM mnlab")
           
            for thutu in cursor.fetchall():
                tt = int(thutu[0]) + 1

            cursor.execute(f"insert into mnlab (stt,id,hoten,mssv,nhom,gioitinh,namsinh,email,sdt,date,image,tendetai) values('{tt}','"+ self.id +"','"+ self.hoten +"','"+ self.mssv +"','"+ self.nhom +"','"+ self.gioitinh +"','"+ self.namsinh +"','"+ self.email +"','"+ self.sdt +"','"+ date +"','"+ self.fln +"','""')")
            cursor.execute("commit")
            
            self.ht.delete(0, 'end')
            self.email1.delete(0,'end')
            self.mssv1.delete(0,'end')
            self.sdt1.delete(0,'end')
            self.bh.delete(0,'end')
            self.gt.delete(0,'end')
            self.nhom1.delete(0,'end')
            MessageBox.showinfo("Insert Status","Inserted Successfully")
            print('haha')
            
            indangki = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
            calldk = indangki.cursor()
            '''
            unix = time.time()
            date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
            '''
            dateerror = datetime.now()
            date = dateerror.strftime("%d/%m/%Y %H:%M:%S")
            indangki.commit()
            calldk.execute("SELECT * FROM mnlab ORDER BY stt DESC LIMIT 1 ")
            
            
            print('hihi')
             
        
            for dong in calldk.fetchall():
                
                stt=dong[0]
                id = dong[1]
                hten=dong[2]
                ms=dong[3]
                nhom=dong[4]
                gt=dong[5]
                ns=dong[6]
                em=dong[7]
                tel=dong[8]
                dat=dong[9]
                print('id: ',dong[0])
                print('hten: ',dong[1])
                print('ms: ',dong[2])
              
            #self.tree.insert(parent='',index='end',text="",values=(1,self.a,self.b,self.c,date))
            #self.tree.insert(parent='',index='end',text="",values=(1,a,b,c,date)) 
            dem = 0 
            calldk.execute("SELECT * FROM mnlab")
            for stt in calldk.fetchall():
                dem +=1
            self.tree.insert(parent='',index='end',text="",values=(dem,id, hten, ms,date))
            self.tree3.insert(parent='',index='end',text="",values=(dem,id, hten, gt, ms, em, tel, nhom, 'chua co'))
            demslsv = 0
            calldk.execute("SELECT * FROM mnlab ")
            for slsv in calldk.fetchall():
                demslsv +=1

            self.tongsosv = Label(self.frame2manage, text = int(demslsv), bg='LightCyan1',fg = "Brown",font=('Arial 12 bold'),width=5)                
            self.tongsosv.place(x=560,y=110)
            con.close()
    def remove(self):
        if (self.mssv1.get() == ""):
            MessageBox.showinfo("Delete Status","ID is compolsary for delete")
        else:
            con = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
            cursor = con.cursor()
            cursor.execute("delete from mnlab where mssv='"+ self.mssv1.get() +"'")
            #cursor.execute("delete from mnlab where hoten='"+ ht.get() +"'")
            #or cursor.execute("delete from mnlab where id= '"+id1.get()+"'")
            cursor.execute("commit")
            self.tree.delete(*self.tree.get_children())
            self.tree3.delete(*self.tree3.get_children())

            cursor.execute("SELECT * FROM mnlab ORDER BY date ASC  ")
            demslsv = 0
            for row in cursor.fetchall():
                demslsv +=1
                #print(row)
                i=row[0] #stt
                o=row[1]    #id
                p=row[2]    #ht
                k=row[3]    #ms
                ii=row[4]   #nhom
                oo=row[5]   #gt
                pp=row[6]   #ns
                kk=row[7]   #mail
                sdt=row[8]   #sdt
                date = row[9]
                
                '''
                print('i: ',i)
                print('o: ',o)
                print('p: ',p)
                print('k: ',k)
                '''
                self.tree.insert(parent='',index='end',text="",values=(demslsv, o, p,k,date))
                #self.tree2.delete(parent='',index='end',text="sasad",values=(%s,%s,%s,%s,%s,%s))
                self.tree3.insert(parent='',index='end',text="sasad",values=(demslsv,o,p,oo,k,kk,sdt,ii,'chua co'))
            
            self.tongsosv = Label(self.frame2manage, text = int(demslsv), bg='LightCyan1',fg = "Brown",font=('Arial 12 bold'),width=5)                
            self.tongsosv.place(x=560,y=110)
            self.browseimage.place_forget()
            self.ht.delete(0, 'end')
            self.email1.delete(0,'end')
            self.mssv1.delete(0,'end')
            self.sdt1.delete(0,'end')
            self.bh.delete(0,'end')
            self.gt.delete(0,'end')
            self.nhom1.delete(0,'end')
            MessageBox.showinfo("Delete Status","Deleted Successfully")
            con.close()
            
    def editdata(self):
        self.id = self.id1.get()
        self.hoten = self.ht.get()
        self.mssv = self.mssv1.get()
        self.nhom = self.nhom1.get()
        self.gioitinh = self.gt.get()
        self.namsinh = self.bh.get()
        self.email = self.email1.get()
        self.sdt = self.sdt1.get()
        if(self.mssv =="" ):
            MessageBox.showinfo("Update Status","All Fields are required")
        else:
            con = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
            cursor = con.cursor()
            cursor.execute("Update mnlab set email='"+ self.email +"', hoten='" +self.hoten+"',sdt='"+self.sdt+"', gioitinh='" +self.gioitinh+"' ,mssv='"+self.mssv+"',namsinh='"+self.namsinh +"',nhom='"+self.nhom+"',image='"+self.fln+"' where id='"+self.id+"'")
            cursor.execute("commit")
         
            self.tree.delete(*self.tree.get_children())
            self.tree3.delete(*self.tree3.get_children())

            cursor.execute("SELECT * FROM mnlab ORDER BY date ASC  ")
            dem =0
            for row in cursor.fetchall():
                dem +=1
                #print(ro
                i=row[0] #stt
                o=row[1]    #id
                p=row[2]    #ht
                k=row[3]    #ms
                ii=row[4]   #nhom
                oo=row[5]   #gt
                pp=row[6]   #ns
                kk=row[7]   #mail
                sdt=row[8]   #sdt
                date = row[9]
                tendetai = row[11]
          
                self.tree.insert(parent='',index='end',text="",values=(dem, o, p,k,date))
                self.tree3.insert(parent='',index='end',text="sasad",values=(dem,o,p,oo,k,kk,sdt,ii,tendetai))
            '''
            self.ht.delete(0, 'end')
            self.email1.delete(0,'end')
            self.mssv1.delete(0,'end')
            self.sdt1.delete(0,'end')
            self.bh.delete(0,'end')
            self.gt.delete(0,'end')
            self.nhom1.delete(0,'end')
            '''
            MessageBox.showinfo("Update Status","Update Successfully")
            con.close()

    def framethree(self):
        #frame3=LabelFrame(self.win,text="Chức năng",fg="white",font='Helve 14 bold',bg="SlateGray",relief="raised",borderwidth=1)
        #frame3.pack(side=RIGHT,ipadx=120,ipady=500)

        self.frame3=LabelFrame(self.framebig,text="Online",fg="white",font='Helve 12 bold',bg="DeepSkyBlue4",relief="raised",width=200,height=1220)
        self.frame3.pack(side=RIGHT)
       
        framex = LabelFrame(self.frame3,width=200,height=1220)
        framex.pack(side=RIGHT)
   
        self.tree4 = ttk.Treeview(framex, column=(1,2), selectmode='none', height=40)
        self.tree4.grid(row=0, column=0, sticky='nsew')

        # Setup column heading
        self.tree4.heading('#0', text=' Avatar', anchor='center')
        self.tree4.heading(1, text=' Họ tên', anchor='center')
        self.tree4.heading(2, text=' MSSV', anchor='center')
        # #0, #01, #02 denotes the 0, 1st, 2nd columns

        # Setup column
        self.tree4.column('#0',anchor='center',width=60)
        self.tree4.column(1, anchor='center', width=140)
        self.tree4.column(2, anchor='center', width=80)

        scrolltable = Scrollbar(framex,orient="vertical",command=self.tree4.yview)
        #scrolltable.place(x=215,y=400,relx=100)
        #scrolltable.grid(row=4,column=3,padx=250,pady=380,sticky="ns")
        scrolltable.grid(row=0, column=4, sticky='nsew')

        self.tree4.config(yscroll=scrolltable.set)
        #tree2.bind('<ButtonRelease-1>', select_item)
        self.treeview = self.tree4
        
    def apidata_basic(self):
 
        savehd_basic= mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
        callsavehd_basic = savehd_basic.cursor()
        unix = time.time()
        #date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        #callsavehd_basic.execute("DELETE FROM hoatdongtemp")
        #callsavehd_basic.execute("commit")

        callsavehd_basic.execute("SELECT * FROM hoatdong WHERE time REGEXP(CURRENT_DATE()) ORDER BY time ASC")
        #self.tree2.delete(*self.tree2.get_children()) 
        #self.tree4.delete(*self.tree4.get_children())
        for rowhd in callsavehd_basic.fetchall():
           
            hd_sl=rowhd[5]     
            hd_id=rowhd[0]        
            hd_ht=rowhd[1]
            hd_ms=rowhd[2]
            hd_nhom=rowhd[3]
            hd_time=rowhd[4]
            hd_timeoff=rowhd[6]
           # print('hd_timeoff: ',hd_timeoff)
            dateerror = datetime.now()
            date = dateerror.strftime("%Y-%m-%d %H:%M:%S")
            # Hoạt động temp chứa data hiện tại
            #callsavehd_basic.execute("insert into hoatdongtemp values('"+ hd_id +"','"+ hd_ht +"','"+ hd_time +"')")
            #callsavehd_basic.execute("commit")
            
            if hd_timeoff == date :
                #self.tree2.delete(*self.tree2.get_children())
                #self.tree4.delete(*self.tree4.get_children())
                #print('hd_timeoff la: ',hd_timeoff)
                #print('date la: ',date)
                callsavehd_basic.execute(f"SELECT * FROM hoatdong WHERE timeoff = '{hd_timeoff}'")
                for rowhd in callsavehd_basic.fetchall():
                    #print('hang la: ',rowhd)
                    hd_sl=rowhd[5]     
                    hd_id=rowhd[0]        
                    hd_ht=rowhd[1]
                    hd_ms=rowhd[2]
                    hd_nhom=rowhd[3]
                    hd_time=rowhd[4]
                    hd_timeoff=rowhd[6]
                   
                    for child in self.tree2.get_children():
                        a = self.tree2.item(child)["values"]
                        tg = a[5]
                        if hd_time == tg:
                            self.tree2.delete(child)
                            
                            ######
                            for child2 in self.tree4.get_children():
                                c = self.tree4.item(child2)["values"]
                                #print('hd_ht la: ',hd_ht)
                                #print('c that la: ',c)
                                #print('c la: ',c[1])
                                
                                if hd_ht == c[0]:
                                    
                                    self.tree4.delete(child2)
                                    #self.thongbaoten.place_forget()
                                    
                                    self.thongbaoten = Label(self.frame2hd,text='...'+hd_ht+' đã rời phòng',bg='SteelBlue2',fg='#FFCC00',font=('Helve 20 bold'),width=50)
               
                                    self.thongbaoten.place(x=100,y=10)
                                    
                                    callsavehd_basic.execute("SELECT * FROM hoatdong WHERE timeoff > CURRENT_TIMESTAMP() AND time REGEXP(CURRENT_DATE())")
                                    demsv = 0
                                    for row2 in callsavehd_basic.fetchall():
                                        #print('row2: ',row2)
                                        demsv +=1
                                       
                                    self.slsv = Label(self.frame2hd, text = int(demsv), bg='LightCyan1',fg = "Brown",font=('Arial 14 bold'))                

                                    self.slsv.place(x=520,y=110)
                                    
                                else:
                                    pass
                                
                                
                            print('hd_timehd_time la: ',hd_time)
                            callsavehd_basic.execute(f"DELETE FROM hoatdongtemp WHERE time = '{hd_time}'")
                            callsavehd_basic.execute("commit")
                            callsavehd_basic.execute(f"DELETE FROM luuanhhd WHERE mssv = '{hd_ms}'")
                            callsavehd_basic.execute("commit")
                        else:
                            pass
                    
                    self.tree2.insert(parent='',index='end',text="",values=(hd_sl, hd_id,hd_ht,hd_ms,hd_nhom,hd_time,hd_timeoff))
                
                    #self.tree4.insert(parent='',index='end',text="",values=(hd_ht))
            else:
                pass


            '''
            for child in self.tree2.get_children():
                a = self.tree2.item(child)["values"]
                print('a la: ',a[5])   
            '''
       
        self.tree2.after(480,self.apidata_basic)
        
    def apidata(self): #in san ra database
        data = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
    
        goi = data.cursor()
        unix = time.time()
        
        goi.execute("SELECT * FROM mnlab ORDER BY date ASC  ")
        #self.tree.delete(*self.tree.get_children())
        #self.tree3.delete(*self.tree3.get_children())
        count = 0
        for row in goi.fetchall():
            count +=1
            #print(row)
            i=row[0] #stt
            o=row[1]    #id
            p=row[2]    #ht
            k=row[3]    #ms
            ii=row[4]   #nhom
            oo=row[5]   #gt
            pp=row[6]   #ns
            kk=row[7]   #mail
            sdt=row[8]   #sdt
            date = row[9]
            tdt = row[11]
            
          
            
            self.tree.insert(parent='',index='end',text="",values=(count, o, p,k,date))
            #self.tree2.delete(parent='',index='end',text="sasad",values=(%s,%s,%s,%s,%s,%s))
            self.tree3.insert(parent='',index='end',text="sasad",values=(count,o,p,oo,k,kk,sdt,ii,tdt))
            
        ################
        
        self.tongsosv = Label(self.frame2manage, text = int(count), bg='LightCyan1',fg = "Brown",font=('Arial 12 bold'),width=5)                
        self.tongsosv.place(x=560,y=110)
        savehd = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
        callsavehd = savehd.cursor()
        unix = time.time()
        #date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        callsavehd.execute("DELETE FROM hoatdongtemp")
        callsavehd.execute("commit")
        callsavehd.execute("SELECT * FROM hoatdong WHERE timeoff REGEXP(CURRENT_DATE()) AND timeoff < CURRENT_TIMESTAMP() AND time REGEXP(CURRENT_DATE())")
        #self.tree2.delete(*self.tree2.get_children())       
        #self.tree4.delete(*self.tree4.get_children())
        for rowhd in callsavehd.fetchall():
           
            hd_sl=rowhd[5]     
            hd_id=rowhd[0]        
            hd_ht=rowhd[1]
            hd_ms=rowhd[2]
            hd_nhom=rowhd[3]
            hd_time=rowhd[4]
            hd_timeoff=rowhd[6]
            
            
            self.tree2.insert(parent='',index='end',text="",values=(hd_sl, hd_id,hd_ht,hd_ms,hd_nhom,hd_time,hd_timeoff))
        callsavehd.execute("SELECT * FROM hoatdong WHERE timeoff > CURRENT_TIMESTAMP() AND time REGEXP(CURRENT_DATE())")
        demsv = 0
        for rowhd2 in callsavehd.fetchall():
            demsv +=1
            hd_sl2=rowhd2[5]     
            hd_id2=rowhd2[0]        
            hd_ht2=rowhd2[1]
            hd_ms2=rowhd2[2]
            hd_nhom2=rowhd2[3]
            hd_time2=rowhd2[4]
            hd_timeoff2=rowhd2[6]

            self.thongbaoten = Label(self.frame2hd,text='...'+hd_ht2+' vào gần đây nhất',bg='SteelBlue2',fg='#FFCC00',font=('Helve 20 bold'),width=50)
            self.thongbaoten.place(x=100,y=10)

            print('hd_timeoff2: ',hd_timeoff2)
            self.tree2.insert(parent='',index='end',text="",values=(hd_sl2, hd_id2,hd_ht2,hd_ms2,hd_nhom2,hd_time2))

            callsavehd.execute("insert into hoatdongtemp values('"+ hd_id2 +"','"+ hd_ht2 +"','"+ hd_time2 +"','"+ hd_ms2 +"','/media/vudat/New Volume/Laptrinh/Python/GUI/anhhoitraii.jpg')")
            callsavehd.execute("commit")
        #hd_timeoff2=rowhd2[6]
        self.slsv = Label(self.frame2hd, text = int(demsv), bg='LightCyan1',fg = "Brown",font=('Arial 14 bold'))                
        self.slsv.place(x=520,y=110)
        
        callsavehd.execute("SELECT * FROM hoatdongtemp")
        for rowhd4 in callsavehd.fetchall():
            hd_id4 = rowhd4[0]
            hd_ms4 = rowhd4[3]
            hd_ht4 = rowhd4[1]

            s = ttk.Style()
            s.configure('Treeview', font=('Arial 12'),rowheight=40)
            # Insert image to #0 

            callsavehd.execute("SELECT * FROM mnlab")
            for truyimg in callsavehd.fetchall():
                truyhinhanh = truyimg[1] 
                if hd_id4 == truyhinhanh:
                    po=truyimg[10]
                    if po =='':
                        po ='/media/vudat/New Volume/Laptrinh/Python/GUI/working/Boapp/unnamed.png'
                    print('po la:',po)
                    #image = Image.open('/media/vudat/New Volume/Laptrinh/Python/GUI/anhhoitraii.jpg')
                    image = Image.open(po)
                    # The (450, 350) is (height, width)
                    image = image.resize((38, 38), Image.ANTIALIAS)
            
                    #file='tuiohoinghi.jpg'
                    self._img = ImageTk.PhotoImage(image)
                    self.tree4.insert(parent='',index='end',text="",image=self._img,values=(hd_ht4,hd_ms4))
        
        callsavehd.execute("SELECT * FROM mailcontent order by tinhtrang='Already' DESC")
       
        for content in callsavehd.fetchall():
            maildetai = content[0]
            #print('id sai: ',his_id)
            mailchude = content[1]
            #print('hoten sai: ',his_hoten)
            mailnoidung = content[2]
            #print('mssv sai: ',his_mssv)
            maildate = content[3]
            mailtt = content[4]

         

            self.tree5.insert(parent='',index='end',text="",values=(maildetai, mailchude, mailnoidung,maildate,mailtt))
        
        
        callsavehd.execute("SELECT * FROM luuanhhd")
        self.saveaddress =[]
        for luuanh in callsavehd.fetchall():
            image = luuanh[0]
            self.saveaddress.append(image)
        print('hinh anh luu la: ',self.saveaddress)

        callsavehd.execute("SELECT * FROM ghichu WHERE deadline > CURRENT_TIMESTAMP()")
       
        for showghichu in callsavehd.fetchall():
            noidung = showghichu[0]
            #print('id sai: ',his_id)
            deadline = showghichu[1]
            #print('hoten sai: ',his_hoten)
     
       

         

            self.tree6.insert(parent='',index='end',text="",values=(noidung, deadline))
        

        '''
        for child in self.tree2.get_children():
            a = self.tree2.item(child)["values"]
            print('a la: ',a[6])
       
        self.tree2.after(3000,self.apidata)

        '''
class inputport():
    def __init__(self,win):
        self.win=win
        self.geo=win.geometry("700x500-550+250")
        self.title=win.title('Login to QLSVlab')

        self.config=win.configure(bg='#CB356B')
        self.res=win.resizable(width=False,height=False)

        portNo = StringVar()
        self.entry1=Entry(self.win,textvariable=portNo)
        self.entry1.pack()  

class caidathd:
    def __init__(self,win):
        self.win=win
        self.geo=win.geometry("500x500-600+300")
        self.title=win.title("Đăng kí")
        self.config=win.configure(bg='#FFFF99')

        kgtgoff=Label(win,text="Khoảng thời gian off",fg="black",font=("Arial","18","bold"),bg="#FFFF99")
        kgtgoff.place(x=160,y=90)
       
        time=Label(win,text='TIME',fg="red",font=("Arial","25","bold"),bg="#FFFF99").place(x=16,y=180)
        labelhour=Label(win,text='Giờ',fg="red",font=("Arial","18","bold"),bg="#FFFF99").place(x=140,y=150)
        labelminute=Label(win,text='Phút',fg="red",font=("Arial","18","bold"),bg="#FFFF99").place(x=250,y=150)
        labelsecond=Label(win,text='Giây',fg="red",font=("Arial","18","bold"),bg="#FFFF99").place(x=360,y=150)

        thietlap= Button(win,text='Thiết lập',width=16,bg='SteelBlue2',fg="black",command=self.settg, font=("Arial","12","bold") )
        thietlap.place(x=180,y=250)
        self.gio=Entry(win,width=6,font=('Arial 25 bold'))
        self.gio.place(x=100,y=180)
        #hour.insert('00')
        self.phut=Entry(win,width=6,font=('Arial 25 bold'))
        self.phut.place(x=220,y=180)
        self.giay=Entry(win,width=6,font=('Arial 25 bold'))
        self.giay.place(x=340,y=180)

        con = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
        calltime = con.cursor()
        calltime.execute("SELECT * FROM qltime")
        for qltime in calltime.fetchall():
            self.gio.insert(0,qltime[0])
            self.phut.insert(0,qltime[1])
            self.giay.insert(0,qltime[2])
    def settg(self):
        gio = self.gio.get()
        phut = self.phut.get()
        giay = self.giay.get()
        if(gio =="" or phut=="" or giay =="" ):
            MessageBox.showinfo("Nhắc nhở","Điền đầy đủ thông tin - Trống viết '00'")
        else:
            con = mysql.connect(host="localhost",user="root",password="",database="qlsvlab")
            cursor = con.cursor()
         

            #cursor.execute(f"insert into qltime (hour,minute,second) values('{tt}','"+ self.id +"','"+ self.hoten +"','"+ self.mssv +"','"+ self.nhom +"','"+ self.gioitinh +"','"+ self.namsinh +"','"+ self.email +"','"+ self.sdt +"','"+ date +"','"+ self.fln +"')")
            cursor.execute(f"Update qltime set hour='{gio}', minute='{phut}',second='{giay}'")
            cursor.execute("commit")
            
     
            MessageBox.showinfo("Insert Status","Inserted Successfully")
            #self.top2.withdraw()
            self.win.destroy()
            print('haha')
        
   

        

        
class main:
    if __name__=='__main__':
        #ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0)
        doc=bodyapp(root,ser)

        
        root.mainloop()
        