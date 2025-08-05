#Project 5 : Blood Bank Management System(CRUD+Addititonal features)

IdCounter=1
donors={}
Inventory={'A+':0,'A-':0,'B+':0,'B-':0,'AB+':0,'AB-':0,'O+':0,'O-':0}
requests=[]
log=[]
def RegisterDonor():
    global IdCounter
    print("\n\tREGISTER DONOR\n")
    name=input("Enter name: ")
    age=input("Enter age: ")
    gender=input("Enter gender (M/F): ")
    blood_group=input("Enter blood group : ").upper()
    contact=input("Enter contact number: ")
    donor_id="D"+str(IdCounter)
    IdCounter+=1
    donors[donor_id]={'name':name,'age':age,'gender':gender,'blood_group':blood_group,'contact':contact}
    print(f"Donor Registered Successfully. Donor ID: {donor_id}")
def DonorInfo():
    print("\n\tDONOR INFO\n")
    print("1.View all donors\n2.Update donor info")
    ch=input("choose option: ")
    if ch=='1':
        if not donors:
            print("No donor records found.")
        else:
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}".format("ID","Name","Age","Gender","Blood Group","Contact"))
            print("-"*126)
            for donorID,i in donors.items():
                print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}".format(donorID,i['name'],i['age'],i['gender'],i['blood_group'],i['contact']))
    elif ch=='2':
        donorID=input("Enter Donor ID to Update: ")
        if donorID in donors:
            print("Leave blank to keep unchanged.")
            name=input("New Name: ")
            age=input("New Age: ")
            gender=input("New Gender: ")
            blood_group=input("New Blood Group: ")
            contact=input("New Contact: ")
            if name:donors[donorID]['name']=name
            if age:donors[donorID]['age']=age
            if gender:donors[donorID]['gender']=gender
            if blood_group:donors[donorID]['blood_group']=blood_group.upper()
            if contact:donors[donorID]['contact']=contact
            print("Donor updated.")
        else:
            print("Donor not found.")
def deleteDonor():
    print("\nDELETE DONOR\n")
    donorID=input("Enter donor ID: ")
    if donorID in donors:
        del donors[donorID]
        print("Donor deleted")
    else:
        print("Donor id not found.")
def AddDonation():
    print("\n\tADD DONATION\n")
    donorID=input("Enter Donor ID: ")
    if donorID in donors:
        group=donors[donorID]['blood_group']
        units=int(input("Enter Units Donated: "))
        Inventory[group]+=units
        log.append(f"{donors[donorID]['name']} donated {units} units of {group}")
        print(f"{units} units of {group} added to inventory")
    else:
        print("Invalid donor id")
def ViewInventory():
    print("\nBLOOD INVENTORY\n")
    for bg,qty in Inventory.items():
        print(f"{bg} : {qty} units")
def RequestBlood():
    print("\nBLOOD REQUEST\n")
    name=input("enter hospital/patient Name: ")
    group=input("enter required blood Group: ").upper()
    units=int(input("enter units needed: "))
    if group in Inventory:
        if Inventory[group]>=units:
            Inventory[group]-=units
            requests.append({'name': name,'group': group,'units': units})
            log.append(f"{name} received {units} unit(s) of {group}")
            print(f"{units} units of {group} issued.")
        else:
            print(f"Only {Inventory[group]} units available.")
    else:
        print("Invalid blood group.")
def Transactions():
    print("\nTRANSACTION LOG\n")
    if not log:
        print("No transactions yet.")
    else:
        for i in log:
            print(i)
    print("-"*50)

while True:
    print("-"*50)
    print("BLOOD BANK MANAGEMENT SYSTEM")
    print("-"*50)
    print("1.Register Donor\n2.Donor Info\n3.Delete Donor\n4.Add Donation")
    print("5.View Inventory\n6.Request Blood\n7.View Log\n8.Exit")
    c=input("Enter your choice: ")
    if c=='1':
        RegisterDonor()
    elif c=='2':
        DonorInfo()
    elif c=='3':
        deleteDonor()
    elif c=='4':
        AddDonation()
    elif c=='5':
        ViewInventory()
    elif c=='6':
        RequestBlood()
    elif c=='7':
        Transactions()
    elif c=='8':
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
