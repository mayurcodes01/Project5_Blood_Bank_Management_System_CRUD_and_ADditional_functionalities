
#  Project 5: Blood Bank Management System (CRUD + Additional Features)

This is a console-based Blood Bank Management System developed using Python. The project was assigned as part of the training at **Kiran Academy**.

The system supports donor registration, blood inventory management, blood donation tracking, and request handling — all via a simple text-based interface. It demonstrates core programming concepts like data structures, control flow, functions, and CRUD operations.

---

##  Features

- **Donor Registration**  
  Register new donors with details like name, age, gender, blood group, and contact info.

- **View & Update Donors**  
  Display all registered donors and update donor details.

- **Delete Donor**  
  Remove a donor from the system by ID.

- **Add Donation**  
  Log a blood donation and update the inventory accordingly.

- **Inventory Management**  
  View the current stock of all blood groups.

- **Blood Requests**  
  Request blood units for a patient or hospital and update inventory if available.

- **Transaction Log**  
  Maintain a simple log of all donation and issue transactions.

---

##  Technologies Used

- Python (Core)
- Data Structures: Dictionary, List
- Concepts: CRUD, Functions, Loops, Conditional Statements

---

##  Sample Data Structures

```python
donors = {
    'D1': {
        'name': 'John Doe',
        'age': '30',
        'gender': 'M',
        'blood_group': 'A+',
        'contact': '9876543210'
    }
}

Inventory = {
    'A+': 5, 'A-': 2, 'B+': 3, 'B-': 1,
    'AB+': 4, 'AB-': 0, 'O+': 6, 'O-': 2
}
