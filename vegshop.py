import matplotlib.pyplot as plt
import mysql.connector as db
import pdb,random
con = db.connect(user="root",password="12345@Sv",host="localhost",database='vegshop')

#------------------------------------------OWNER CLASS-------------------------------#

class owner:
    def update_stock(self,qty):
        cur=con.cursor()
        cur.callproc('update_stock',(qty,))
        con.commit()
        cur.close()
        
    def stock_log(self):
        sp=" "
        cur=con.cursor()
        cur.callproc('stock_log')
        print(18*"*",'STOCK_LOGS',17*'*')
        print()
        for row in cur.stored_results():
            a=row.fetchall()
        print(f"Item_Name{sp*10}Prev_day_stock{sp*3}Today_added_stock")
        for i in a:
            a=len(str(i[1]))
            b=len(str(i[2]))
            print(sp*1,i[1],(20-len(i[1]))*sp,i[2],(15-b)*sp,i[3])
        print()
        cur.close()
        
    def insert_stock(self,veg,qty,cp,sp):
        cur=con.cursor()
        cur.callproc('insert_stockk',(veg,qty,cp,sp))
        con.commit()
        cur.close()
        
    def delete_record(self,veg):
        cur=con.cursor()
        cur.callproc('delete_record',(veg,))
        con.commit()
        cur.close()
        
    def revenue(self,a,x,y):
        sp=" "
        cur=con.cursor()
        cur.callproc('exact_revenue',(a,x,y))
        for row in cur.stored_results():
            a=row.fetchall()
        print(18*"*",'REVENUE',17*'*')
        print()
        print(f"Custid{sp*14}Date{sp*11}Profit")
        total=0
        temp_x=[]
        temp_y=[]
        for i in a:
            x=len(str(i[0]))
            z=len(str(i[1]))
            total=total+i[1]
            print(sp*1,i[0],(13-x)*sp,i[2],(10-z)*sp,i[1])
            temp_x.append(i[2])
            temp_y.append(i[1])
        print("-"*42)
        print(sp*18,f'Total profit -- {total} Rs')
        plt.bar(temp_x,temp_y)
        plt.xlabel('Date')
        plt.ylabel('profit')
        plt.title('Revenue')
        plt.grid(True)
        plt.show()
        temp_x.clear()
        temp_y.clear()
        print()
        
        

#-----------------------------CUSTOMER CLASS-------------------------------------#
        
class customer:    
    def menu(self):
        sp=" "
        cur=con.cursor()
        cur.callproc('call_menu')
        for row in cur.stored_results():
            a=row.fetchall()
        cur.close()
        print()
        print(18*"*",'MENU',17*'*')
        print()
        print(f"vegtables{sp*10}avialble_qty{sp*5}price")
        for i in a:
            a=len(str(i[2]))
            print(i[1],(21-len(i[1]))*sp,i[2],(12-a)*sp,i[-1])
        print()
            
    def exist(self,veg):
        cur=con.cursor()
        cur.callproc('Check_item',(veg,))
        for row in cur.stored_results():
            a=row.fetchall()
        cur.close()
        if a[0][0]== "True":
            return True
        else:
            return False
   
    def qty_check(self,veg,qty):
        cur=con.cursor()
        cur.callproc('qty_check',(veg,qty))
        for row in cur.stored_results():
            a=row.fetchall()
        cur.close()
        if a[0][0]== "True":
            return True
        else:
            return False
    def insert(self,custid,veg,qty):
        cur=con.cursor()
        cur.callproc('insertt',(custid,veg,qty))
        con.commit()
        cur.close()
        
    def update_menu(self,veg,qty):
        cur=con.cursor()
        cur.callproc('update_qty',(veg,qty))
        con.commit()
        cur.close()
        
    def basket(self,custid):
        sp=" "
        cur=con.cursor()
        cur.callproc('baskett',(custid,))
        for row in cur.stored_results():
            a=row.fetchall()
        print()
        print(18*"*",'BASKET',17*'*')
        print()
        print(f"Vegtables{sp*15}Total_qty{sp*7}Price")
        x=0
        for i in a:
            x=x+i[2]
            a=len(str(i[1]))
            print(i[0],(25-len(i[0]))*sp,i[1],(12-a)*sp,i[2])
        print("-"*48)
        print(sp*18,f'Total payble amount-- {x} Rs')
        print()
            
    def update_revenue(self,custid):
        cur=con.cursor()
        cur.callproc('update_revenue',(custid,))
        con.commit()
        cur.close()
        
    def delete_item_basket(self,item):
        cur=con.cursor()
        cur.callproc('delete_item_basket',(item,))
        con.commit()
        cur.close()
        
    def modify_qnt_basket(self):
        pass
        
    def truncate_basket(self):
        cur=con.cursor()
        cur.callproc('truncate_basket')
        cur.close()
    
        
obj=customer()
own_obj=owner()
#print(f'{120*'-'}\n{" "*60}WELCOME TO RYTHUBAZAR{" "*60}\n{120*'-'}')
while True:
    print('----Type of access---- \n1.Owner\n2.Customer\n3.exit')
    log=int(input('choose type:'))

#--------------------------------------OWNER ACCESS------------------------------------------------#
    
    if log == 1:                                              #check_stock
        while True:
            print('1.Check stock\n2.Update stock\n3.insert items\n4.delete records\n5.stock Logs\n6.Revenue\n7.Exit')
            inp=int(input('choose one option from above:'))
            if inp==1:
                obj.menu()
                print('1.Main menu\n2.Exit')
                x=int(input('choose one option from above:'))
                if x == 2:
                    break
                
            elif inp == 2:                                    #update_stock
                qty=int(input('enter how much qty you want to add the stock:'))
                if qty>0:
                    own_obj.update_stock(qty)
                    print()
                    print('1.Main menu\n2.Exit')
                    x=int(input('choose one option from above:'))
                    if x == 2:
                        break
                else:
                    print('--Invalid Quantity--')
                    
            elif inp==3:                                    #insert_items
                veg=input('enter item name:')
                qty=int(input('enter qty:'))
                if qty>0:
                    cp=int(input('enter cost price:'))
                    if cp>0:
                        sp=int(input('enter sell price:'))
                        if sp>0:
                            own_obj.insert_stock(veg,qty,cp,sp)
                            print('1.Main menu\n2.Exit')
                            x=int(input('choose one option from above:'))
                            if x==2:
                                break
                        else:
                            print('--Invalid Sellprice--')
                            
                    else:
                        print('--Invalid Costprice--')
                        
                else:
                    print('--Invalid Quantity--')
                    
            elif inp==4:                                    #delete records
                veg=input('enter item name to delete record:')
                res=obj.exist(veg)
                if res==True:
                    own_obj.delete_record(veg)
                    print('1.Main menu\n2.Exit')
                    x=int(input('choose one option from above:'))
                    if x==2:
                        break
                else:
                    print('''--Item doesn't exist in Stock--''')
                    print()
                    print('1.Main menu\n2.Exit')
                    x=int(input('choose one option from above:'))
                    if x==2:
                        break
                    
            elif inp==5:                                    #Stock_logs
                own_obj.stock_log()
                print('1.Main menu\n2.Exit')
                x=int(input('choose one option from above:'))
                if x==2:
                    break
            elif inp==6:                    # revenue 
                print('type of revenue:\n1.Specific day\n2.specific month\n3.complete year\n4.Today')
                type=int(input('from above choose one:'))
                if type == 1: 
                    a='day'
                    x=int(input('enter specific month:'))
                    if x>=1 and x<=12:
                        y=int(input('enter specific Day:'))
                        if y>=1 and y<=31:
                            own_obj.revenue(a,x,y)
                        else:
                            print('--Invalid Day--')
                    else:
                        print('--Invalid month--')
                elif type == 2:
                    a='month'
                    x=int(input('enter specific year:'))
                    y=int(input('enter specific month:'))
                    if y>=1 and y<=12:
                        own_obj.revenue(a,x,y)
                    else:
                        print('--Invalid Month--')  
                elif type==3:
                    a='none'
                    own_obj.revenue(a,0,0)
                elif type == 4:
                    a='today'
                    own_obj.revenue(a,0,0)
                else:
                    print('--Invalid option--')
            elif inp==7:
                break 
            else:
                print('invalid input')
                print()
                print('1.Main menu\n2.Exit')
                x=int(input('choose one option from above:'))
                if x==2:
                    break
                
#-----------------------------CUSTOMER ACCESS-------------------------------------------#
                
    elif log == 2:
        obj.menu()
        custid=random.randint(5000,9999)
        print(f'custid:{custid}')   
        while True:
            veg=input("enter veg name:")
            res=obj.exist(veg)
            if res == True:
                qty=int(input("enter quantity:"))
                if qty>0:
                    chk=obj.qty_check(veg,qty)
                    if chk == True:
                        obj.insert(custid,veg,qty)
                        obj.update_menu(veg,qty)
                        x=input("you want more vegtables(yes/no):")
                        if x =='no':
                            obj.basket(custid)
                            mod=input('you want any modifications in basket(yes/no):')
                            if mod == 'yes':
                                type=int(input('1.delete item\n2.modify quantity\nchoose one:'))
                                if type == 1:
                                    item=input('enter item name to delete from basket:')
                                    obj. delete_item_basket(item)
                                    a=input('you want to buy more items(yes/no):')
                                    if a == 'no':
                                        obj.basket(custid)
                                        obj.update_revenue(custid)
                                        obj.truncate_basket()
                                        a=input('you want make the another bill(yes/no):')
                                        if a =='yes':
                                            obj.menu()
                                            custid=random.randint(5000,9999)
                                            print(f'custid:{custid}')   
                                        else:
                                            break
                                    else:
                                        pass
                                elif type == 2:
                                    item=input('enter item name to modify from basket:')
                                    qty=int(input('enter qty:'))
                                    obj. delete_item_basket(item)
                                    chk=obj.qty_check(item,qty)
                                    obj.insert(custid,item,qty)
                                    obj.update_menu(item,qty)
                                    a=input('you want buy more items(yes/no):')
                                    if a == 'no':
                                        obj.basket(custid)
                                        obj.update_revenue(custid)
                                        obj.truncate_basket()
                                        a=input('you want make the another bill(yes/no):')
                                        if a =='yes':
                                            obj.menu()
                                            custid=random.randint(5000,9999)
                                            print(f'custid:{custid}')   
                                        else:
                                            break
                                    else:
                                        pass
                                else:
                                    print('--Invalid option--')
                                    obj.update_revenue(custid)
                                    obj.truncate_basket()
                                    a=input('you want make the another bill(yes/no):')
                                    if a =='yes':
                                        obj.menu()
                                        custid=random.randint(5000,9999)
                                        print(f'custid:{custid}')   
                                    else:
                                        break
                            else:
                                obj.update_revenue(custid)
                                obj.truncate_basket()
                                a=input('you want make the another bill(yes/no):')
                                if a =='yes':
                                    obj.menu()
                                    custid=random.randint(5000,9999)
                                    print(f'custid:{custid}')   
                                else:
                                    break
                    else:
                        print('--Required Quantity is not availble--') 
                        x=input("you want more vegtables(yes/no):")
                        if x=='no':
                            obj.basket(custid)
                            mod=input('you want any modifications in basket(yes/no):')
                            if mod == 'yes':
                                type=int(input('1.delete item\n2.modify quantity\nchoose one:'))
                                if type == 1:
                                    item=input('enter item name to delete from basket:')
                                    obj. delete_item_basket(item)
                                    a=input('you want to buy more items(yes/no):')
                                    if a == 'no':
                                        obj.basket(custid)
                                        obj.update_revenue(custid)
                                        obj.truncate_basket()
                                        a=input('you want make the another bill(yes/no):')
                                        if a =='yes':
                                            obj.menu()
                                            custid=random.randint(5000,9999)
                                            print(f'custid:{custid}')   
                                        else:
                                            break
                                    else:
                                        pass
                                elif type == 2:
                                    item=input('enter item name to modify from basket:')
                                    qty=int(input('enter qty:'))
                                    obj. delete_item_basket(item)
                                    chk=obj.qty_check(item,qty)
                                    obj.insert(custid,item,qty)
                                    obj.update_menu(item,qty)
                                    a=input('you want to buy more items(yes/no):')
                                    if a == 'no':
                                        obj.basket(custid)
                                        obj.update_revenue(custid)
                                        obj.truncate_basket()
                                        a=input('you want make the another bill(yes/no):')
                                        if a =='yes':
                                            obj.menu()
                                            custid=random.randint(5000,9999)
                                            print(f'custid:{custid}')   
                                        else:
                                            break
                                    else:
                                        pass
                                else:
                                    print('--Invalid option--')
                                    obj.update_revenue(custid)
                                    obj.truncate_basket()
                                    a=input('you want make the another bill(yes/no):')
                                    if a =='yes':
                                        custid=random.randint(5000,9999)
                                        print(f'custid:{custid}')   
                                    else:
                                        break
                            else:
                                obj.update_revenue(custid)
                                obj.truncate_basket()
                                a=input('you want make the another bill(yes/no):')
                                if a =='yes':
                                    custid=random.randint(5000,9999)
                                    print(f'custid:{custid}')   
                                else:
                                    break
                else:
                    print('--Invalid Quantity--') 
                    x=input("you want more vegtables(yes/no):")
                    if x =='no':
                        obj.basket(custid)
                        obj.update_revenue(custid)
                        obj.truncate_basket()
                        break   
            else:
                print('--Required item is not available--')
                x=input("you want to buy another vegtable(yes/no):")
                if x =='no':
                    obj.basket(custid)
                    mod=input('you want any modifications in basket(yes/no):')
                    if mod == 'yes':
                        type=int(input('1.delete item\n2.modify quantity\nchoose one:'))
                        if type == 1:
                            item=input('enter item name to delete from basket:')
                            obj. delete_item_basket(item)
                            a=input('you want to buy more items(yes/no):')
                            if a == 'no':
                                obj.basket(custid)
                                obj.update_revenue(custid)
                                obj.truncate_basket()
                                a=input('you want make the another bill(yes/no):')
                                if a =='yes':
                                    obj.menu()
                                    custid=random.randint(5000,9999)
                                    print(f'custid:{custid}')   
                                else:
                                    break
                            elif type == 2:
                                item=input('enter item name to modify from basket:')
                                qty=int(input('enter qty:'))
                                obj. delete_item_basket(item)
                                chk=obj.qty_check(item,qty)
                                obj.insert(custid,item,qty)
                                obj.update_menu(item,qty)
                                a=input('you want to buy more items(yes/no):')
                                if a == 'no':
                                    obj.basket(custid)
                                    obj.update_revenue(custid)
                                    obj.truncate_basket()
                                    a=input('you want make the another bill(yes/no):')
                                    if a =='yes':
                                        obj.menu()
                                        custid=random.randint(5000,9999)
                                        print(f'custid:{custid}')   
                                    else:
                                        break
                                elif a == 'yes':
                                    pass
                                else:
                                    print('--Invalid option--')
                                    obj.update_revenue(custid)
                                    obj.truncate_basket()
                                    a=input('you want make the another bill(yes/no):')
                                    if a =='yes':
                                        custid=random.randint(5000,9999)
                                        print(f'custid:{custid}')   
                                    else:
                                        break
                            else:
                                obj.update_revenue(custid)
                                obj.truncate_basket()
                                a=input('you want make the another bill(yes/no):')
                                if a =='yes':
                                    custid=random.randint(5000,9999)
                                    print(f'custid:{custid}')   
                                else:
                                    break
                    
                              
    elif log == 3:
        break
    else:
        print('--Invalid input,Choose correct option--')
con.close()
