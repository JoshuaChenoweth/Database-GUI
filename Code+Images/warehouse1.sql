create database if not exists warehouse1;

use warehouse1;

CREATE TABLE Guest_User (
	Guest_User_Name varchar(45) primary key,
	Guest_fname varchar(40),
    Guest_lname varchar(40),
    Guest_password char(20),
    Guest_address varchar(255),
    Guest_Phone_Number varchar(15)
);

INSERT INTO Guest_User (Guest_User_Name, Guest_fname, Guest_lname, Guest_password, Guest_address, Guest_Phone_Number)
VALUES 
('guest1', 'John', 'Doe', 'password1', '123 Main St', 1234567890),
('guest2', 'Jane', 'Smith', 'password2', '456 Oak St', 9876543210),
('guest3', 'Mike', 'Johnson', 'password3', '789 Pine St', 5551234567),
('guest4', 'Emily', 'Williams', 'password4', '101 Elm St', 1112223333),
('guest5', 'David', 'Miller', 'password5', '202 Maple St', 9998887777),
('guest6', 'Sarah', 'Jones', 'password6', '303 Birch St', 4445556666),
('guest7', 'Chris', 'Davis', 'password7', '404 Cedar St', 7776665555),
('guest8', 'Lisa', 'Anderson', 'password8', '505 Walnut St', 2223334444),
('guest9', 'Tom', 'Moore', 'password9', '606 Pineapple St', 6667778888),
('guest10', 'Amy', 'Wilson', 'password10', '707 Orange St', 3334445555);
    
CREATE TABLE Admin_User (
	Admin_User_Name varchar(45) primary key,
	Admin_Email varchar(40),
    Admin_fname varchar(40),
    Admin_lname varchar(40),
    Admin_Password char(20),
    Admin_Recovery_Email varchar(40)
);

INSERT INTO Admin_User (Admin_User_Name, Admin_Email, Admin_fname, Admin_lname, Admin_Password, Admin_Recovery_Email)
VALUES 
('admin1', 'john.doe@admincompany.com', 'John', 'Doe', 'password1', 'john.recovery@admincompany.com'),
('admin2', 'jane.smith@admincompany.com', 'Jane', 'Smith', 'password2', 'jane.recovery@admincompany.com'),
('admin3', 'mike.johnson@admincompany.com', 'Mike', 'Johnson', 'password3', 'mike.recovery@admincompany.com'),
('admin4', 'emily.williams@admincompany.com', 'Emily', 'Williams', 'password4', 'emily.recovery@admincompany.com'),
('admin5', 'david.miller@admincompany.com', 'David', 'Miller', 'password5', 'david.recovery@admincompany.com'),
('admin6', 'sarah.jones@admincompany.com', 'Sarah', 'Jones', 'password6', 'sarah.recovery@admincompany.com'),
('admin7', 'chris.davis@admincompany.com', 'Chris', 'Davis', 'password7', 'chris.recovery@admincompany.com'),
('admin8', 'lisa.anderson@admincompany.com', 'Lisa', 'Anderson', 'password8', 'lisa.recovery@admincompany.com'),
('admin9', 'tom.moore@admincompany.com', 'Tom', 'Moore', 'password9', 'tom.recovery@admincompany.com'),
('admin10', 'amy.wilson@admincompany.com', 'Amy', 'Wilson', 'password10', 'amy.recovery@admincompany.com');
CREATE TABLE Supplier (
    Supplier_ID int primary key,
    Supplier_Name varchar(45),
    Supplier_Address varchar(255),
    Supplier_Email varchar(45),
    Supplier_Contact_Number varchar(255)
);

ALTER TABLE Supplier
MODIFY COLUMN Supplier_Contact_Number VARCHAR(255);

INSERT INTO Supplier (Supplier_ID, Supplier_Name, Supplier_Address, Supplier_Email, Supplier_Contact_Number)
VALUES 
(1, 'Supplier1', '123 Main St', 'supplier1@example.com', 1234567890),
(2, 'Supplier2', '456 Oak St', 'supplier2@gmail.com', 9876543210),
(3, 'Supplier3', '789 Pine St', 'supplier3@yahoo.com', 5551234567),
(4, 'Supplier4', '101 Elm St', 'supplier4@outlook.com', 1112223333),
(5, 'Supplier5', '202 Maple St', 'supplier5@example.com', 9998887777),
(6, 'Supplier6', '303 Birch St', 'supplier6@gmail.com', 4445556666),
(7, 'Supplier7', '404 Cedar St', 'supplier7@yahoo.com', 7776665555),
(8, 'Supplier8', '505 Walnut St', 'supplier8@outlook.com', 2223334444),
(9, 'Supplier9', '606 Pineapple St', 'supplier9@example.com', 6667778888),
(10, 'Supplier10', '707 Orange St', 'supplier10@gmail.com', 3334445555);



CREATE TABLE Item (
    Item_ID int primary key,
    Item_Name varchar(40),
    Supplier_ID int,
    Height int,
    Weight int,
    Stored_Time datetime,
    type_of_item varchar(50),
    Storage_Condition varchar(50),
    foreign key (Supplier_ID) references Supplier(Supplier_ID)
);

INSERT INTO Item (Item_ID, Item_Name, Supplier_ID, Height, Weight, Stored_Time, type_of_item, Storage_Condition)
VALUES 
(1, 'Item1', 1, 10, 5, '2023-11-10 12:00:00', 'Electronics', 'Dry Storage'),
(2, 'Item2', 2, 15, 8, '2023-11-10 12:30:00', 'Clothing', 'Cool Storage'),
(3, 'Item3', 3, 8, 3, '2023-11-10 13:00:00', 'Electronics', 'Dry Storage'),
(4, 'Item4', 4, 12, 6, '2023-11-10 13:30:00', 'Books', 'Dry Storage'),
(5, 'Item5', 5, 18, 10, '2023-11-10 14:00:00', 'Furniture', 'Dry Storage'),
(6, 'Item6', 6, 25, 12, '2023-11-10 14:30:00', 'Electronics', 'Dry Storage'),
(7, 'Item7', 7, 14, 7, '2023-11-10 15:00:00', 'Clothing', 'Cool Storage'),
(8, 'Item8', 8, 20, 15, '2023-11-10 15:30:00', 'Electronics', 'Dry Storage'),
(9, 'Item9', 9, 22, 18, '2023-11-10 16:00:00', 'Furniture', 'Dry Storage'),
(10, 'Item10', 10, 30, 25, '2023-11-10 16:30:00', 'Books', 'Dry Storage');
    
CREATE TABLE Borrowed_History (
	Borrowed_Item_ID int primary key,
	Item_ID int,
    Borrowed_Duration double,
    Return_Date date,
    Return_Condition varchar(45),
    Guest_User_Name varchar(45),
	foreign key (Guest_User_Name) references Guest_User(Guest_User_Name),
    foreign key (Item_ID) references Item(Item_ID)
);
INSERT INTO Borrowed_History (Borrowed_Item_ID, Item_ID, Borrowed_Duration, Return_Date, Return_Condition, Guest_User_Name)
VALUES 
(1, 1, 7.5, '2023-11-15', 'Good', 'guest1'),
(2, 2, 5.0, '2023-11-18', 'Excellent', 'guest2'),
(3, 3, 3.5, '2023-11-20', 'Fair', 'guest3'),
(4, 4, 2.0, '2023-11-22', 'Good', 'guest4'),
(5, 5, 10.0, '2023-11-25', 'Excellent', 'guest5'),
(6, 6, 8.0, '2023-11-28', 'Good', 'guest6'),
(7, 7, 6.5, '2023-11-30', 'Excellent', 'guest7'),
(8, 8, 4.0, '2023-12-03', 'Fair', 'guest8'),
(9, 9, 9.5, '2023-12-05', 'Good', 'guest9'),
(10, 10, 7.0, '2023-12-08', 'Excellent', 'guest10');

CREATE TABLE Favorite_item (
    Favorite_ID int primary key,
    Item_ID int,
    Favorite_date date,
    comments text,
    Guest_User_Name varchar(45),
    foreign key (Guest_User_Name) references Guest_User(Guest_User_Name),
    foreign key (Item_ID) references Item(Item_ID)
);
INSERT INTO Favorite_item (Favorite_ID, Item_ID, Favorite_date, comments, Guest_User_Name)
VALUES 
(1, 1, '2023-11-15', 'This is a great item!', 'guest1'),
(2, 2, '2023-11-18', 'Love the design.', 'guest2'),
(3, 3, '2023-11-20', 'Very useful.', 'guest3'),
(4, 4, '2023-11-22', 'Awesome book!', 'guest4'),
(5, 5, '2023-11-25', 'Comfortable furniture.', 'guest5'),
(6, 6, '2023-11-28', 'Impressive electronics.', 'guest6'),
(7, 7, '2023-11-30', 'Cool clothing item.', 'guest7'),
(8, 8, '2023-12-03', 'Nice gadget!', 'guest8'),
(9, 9, '2023-12-05', 'Stylish furniture.', 'guest9'),
(10, 10, '2023-12-08', 'Great read!', 'guest10');

CREATE TABLE Request (
	Request_Id int primary key,
    Guest_User_Name varchar(45),
    Item_Id int,
    Borrowed_Duration double,
    Request_Type varchar(45),
    Request_Status varchar(45),
    Return_Date date,
    foreign key (Guest_User_Name) references Guest_User(Guest_User_Name),
    foreign key (Item_ID) references Item(Item_ID)
);
INSERT INTO Request (Request_Id, Guest_User_Name, Item_Id, Borrowed_Duration, Request_Type, Request_Status, Return_Date)
VALUES 
(1, 'guest1', 1, 7.5, 'Borrow', 'Pending', NULL),
(2, 'guest2', 2, 5.0, 'Borrow', 'Approved', '2023-11-18'),
(3, 'guest3', 3, 3.5, 'Borrow', 'Rejected', NULL),
(4, 'guest4', 4, 2.0, 'Return', 'Pending', NULL),
(5, 'guest5', 5, 10.0, 'Return', 'Approved', '2023-11-25'),
(6, 'guest6', 6, 8.0, 'Borrow', 'Pending', NULL),
(7, 'guest7', 7, 6.5, 'Return', 'Rejected', NULL),
(8, 'guest8', 8, 4.0, 'Borrow', 'Approved', '2023-12-03'),
(9, 'guest9', 9, 9.5, 'Return', 'Pending', NULL),
(10, 'guest10', 10, 7.0, 'Borrow', 'Approved', '2023-12-08');

CREATE TABLE Orders(
	Orders_ID int primary key,
	Orders_Date date,
	Orders_Status varchar(45),
	Orders_Type varchar(45),
	Address varchar(255),
	Price decimal, 
	Payment_Method varchar(45),
	Sales_Discounts varchar(45),
    Item_ID int,
    foreign key (Item_ID) references Item(Item_ID)
);

INSERT INTO Orders (Orders_ID, Orders_Date, Orders_Status, Orders_Type, Address, Price, Payment_Method, Sales_Discounts, Item_ID)
VALUES 
(1, '2023-11-15', 'Shipped', 'Online', '123 Main St', 150.00, 'Credit Card', '10% off', 1),
(2, '2023-11-18', 'Delivered', 'In-Store', '456 Oak St', 80.00, 'Cash', '5% off', 2),
(3, '2023-11-20', 'Processing', 'Online', '789 Pine St', 120.00, 'PayPal', '15% off', 3),
(4, '2023-11-22', 'Canceled', 'In-Store', '101 Elm St', 50.00, 'Credit Card', 'No discount', 4),
(5, '2023-11-25', 'Shipped', 'Online', '202 Maple St', 200.00, 'Credit Card', '10% off', 5),
(6, '2023-11-28', 'Delivered', 'In-Store', '303 Birch St', 300.00, 'Cash', '5% off', 6),
(7, '2023-11-30', 'Processing', 'Online', '404 Cedar St', 80.00, 'PayPal', '15% off', 7),
(8, '2023-12-03', 'Canceled', 'In-Store', '505 Walnut St', 150.00, 'Credit Card', 'No discount', 8),
(9, '2023-12-05', 'Shipped', 'Online', '606 Pineapple St', 250.00, 'Credit Card', '10% off', 9),
(10, '2023-12-08', 'Delivered', 'In-Store', '707 Orange St', 120.00, 'Cash', '5% off', 10);

CREATE TABLE Returns (
    Returns_ID int primary key, 
    Item_ID int,
    Orders_ID int, 
    Guest_User_Name varchar(45),
    Orders_Date date, 
    Guest_address varchar(255),
    foreign key (Guest_User_Name) references Guest_User(Guest_User_Name),
    foreign key (Item_ID) references Item(Item_ID),
    foreign key (Orders_ID) references Orders(Orders_ID)
);

INSERT INTO Returns (Returns_ID, Item_ID, Orders_ID, Guest_User_Name, Orders_Date, Guest_address)
VALUES 
(1, 1, 1, 'guest1', '2023-11-15', '123 Main St'),
(2, 2, 2, 'guest2', '2023-11-18', '456 Oak St'),
(3, 3, 3, 'guest3', '2023-11-20', '789 Pine St'),
(4, 4, 4, 'guest4', '2023-11-22', '101 Elm St'),
(5, 5, 5, 'guest5', '2023-11-25', '202 Maple St'),
(6, 6, 6, 'guest6', '2023-11-28', '303 Birch St'),
(7, 7, 7, 'guest7', '2023-11-30', '404 Cedar St'),
(8, 8, 8, 'guest8', '2023-12-03', '505 Walnut St'),
(9, 9, 9, 'guest9', '2023-12-05', '606 Pineapple St'),
(10, 10, 10, 'guest10', '2023-12-08', '707 Orange St');
CREATE TABLE Department(
	Department_ID int primary key, 
	Department_Name varchar(45),
	Manager_Name varchar(45),
	Quantity int,
	Department_Type varchar(45)
);

INSERT INTO Department (Department_ID, Department_Name, Manager_Name, Quantity, Department_Type)
VALUES 
(1, 'IT', 'John Smith', 10, 'Technical'),
(2, 'HR', 'Jane Doe', 5, 'Administrative'),
(3, 'Finance', 'Mike Johnson', 8, 'Financial'),
(4, 'Marketing', 'Emily Williams', 6, 'Marketing'),
(5, 'Operations', 'David Miller', 12, 'Operational'),
(6, 'Customer Service', 'Sarah Jones', 15, 'Service'),
(7, 'Research and Development', 'Chris Davis', 7, 'Development'),
(8, 'Sales', 'Lisa Anderson', 20, 'Sales'),
(9, 'Quality Assurance', 'Tom Moore', 9, 'Quality'),
(10, 'Purchasing', 'Amy Wilson', 11, 'Procurement');
-- Guest User name query test
SELECT Guest_User_Name, Guest_fname, Guest_lname
FROM Guest_User
LIMIT 5;
-- Admin User name query test
SELECT Admin_User_Name, Admin_Email, Admin_fname, Admin_lname
FROM Admin_User
LIMIT 5;
-- Supllier ID name query test
SELECT Supplier_ID, Supplier_Name, Supplier_Address, Supplier_Email, Supplier_Contact_Number
FROM Supplier
LIMIT 5;
-- Item_ID name query test
SELECT Item_ID, Item_Name, Height, Weight
FROM Item
WHERE Weight > 5
LIMIT 5;
-- Borrowed Item name query test
SELECT Borrowed_Item_ID, Item_ID, Borrowed_Duration, Return_Date, Return_Condition, Guest_User_Name
FROM Borrowed_History
LIMIT 5;
-- Favorite ID name query test
SELECT Favorite_ID, Item_ID, Favorite_date, comments, Guest_User_Name
FROM Favorite_item
LIMIT 5;
-- Request ID name query test
SELECT Request_Id, Guest_User_Name, Item_Id, Borrowed_Duration, Request_Type, Request_Status, Return_Date
FROM Request
LIMIT 5;
-- Department ID name query test
SELECT Department_ID, Department_Name, Manager_Name, Quantity
FROM Department
LIMIT 5;
-- primary key constraints
INSERT INTO Guest_User (Guest_User_Name, Guest_fname, Guest_lname, Guest_password, Guest_address, Guest_Phone_Number)
VALUES ('guest1', 'John', 'Doe', 'password1', '123 Main St', '1234567890');
-- foreign key constraint
INSERT INTO Orders (Orders_ID, Orders_Date, Orders_Status, Orders_Type, Address, Price, Payment_Method, Sales_Discounts, Item_ID)
VALUES (11, '2023-12-10', 'Processing', 'Online', '123 Main St', 100.00, 'Credit Card', '5% off', 99);
-- Unique Key Constraint
INSERT INTO Supplier (Supplier_ID, Supplier_Name, Supplier_Address, Supplier_Email, Supplier_Contact_Number)
VALUES (11, 'Supplier11', '123 Main St', 'supplier1@example.com', '1234567890');
-- Data type jey constraint
INSERT INTO Guest_User (Guest_User_Name, Guest_fname, Guest_lname, Guest_password, Guest_address, Guest_Phone_Number)
VALUES ('guest11', 'John', 'Doe', 'password11', '123 Main St', 'invalid_phone');

-- Start/User Authentication page
CREATE VIEW Start_Page AS
SELECT 'Welcome' AS Message;

-- Main Menu page
CREATE VIEW Main_Menu_Page AS
SELECT 'View Orders' AS Menu_Option
UNION
SELECT 'Make Requests'
UNION
SELECT 'View Favorites'
UNION
SELECT 'Return Items'
UNION
SELECT 'Borrow Items';

-- View available items page
CREATE VIEW Available_Items AS
SELECT * FROM Item;

-- View item details page
CREATE VIEW Item_Details AS
SELECT * FROM Item;

-- Select item and duration page
CREATE VIEW Item_Selection AS
SELECT * FROM Item;

-- Check availability page
CREATE VIEW Check_Availability AS
SELECT
    Item_ID,
    CASE
        WHEN CURRENT_DATE <= Stored_Time THEN 'Item Available'
        ELSE 'Item Unavailable'
    END AS Availability_Status
FROM Item;

-- Item available page
CREATE VIEW Item_Available AS
SELECT
    i.Item_ID,
    i.Item_Name,
    i.Type_of_item,
    i.Stored_Time,
    o.Order_ID,
    o.Order_Date,
    o.Address
FROM Item i
JOIN Orders o ON i.Item_ID = o.Item_ID;

-- Item unavilable page
CREATE VIEW Item_Unavailable AS
SELECT
    Item_ID,
    'Item Unavailable' AS Availability_Status
FROM Item
WHERE CURRENT_DATE > Stored_Time;

-- End page
CREATE VIEW End_Page AS
SELECT
    o.Order_ID,
    o.Order_Status,
    o.Order_Type,
    o.Address,
    o.Price,
    o.Payment_Method,
    o.Sales_Discounts,
    i.Item_Name,
    i.Type_of_item
FROM Orders o
JOIN Item i ON o.Item_ID = i.Item_ID;

-- Normalization:
-- 1NF:
	-- Guest_User Table:
    CREATE TABLE Guest_User (
    Guest_User_Name VARCHAR(45) PRIMARY KEY,
    Guest_Fname VARCHAR(40),
    Guest_Lname VARCHAR(40),
    Guest_Password CHAR(20),
    Guest_Address VARCHAR(255),
    Guest_Phone_Number INT
);

	-- Admin_User Table:
    CREATE TABLE Admin_User (
    Admin_User_Name VARCHAR(45) PRIMARY KEY,
    Admin_Email VARCHAR(40),
    Admin_Fname VARCHAR(40),
    Admin_Lname VARCHAR(40),
    Admin_Password CHAR(20),
    Admin_Recovery_Email VARCHAR(40)
);

	-- Supplier Table:
    CREATE TABLE Supplier (
    Supplier_ID INT PRIMARY KEY,
    Supplier_Name VARCHAR(45),
    Supplier_Address VARCHAR(255),
    Supplier_Email VARCHAR(45),
    Supplier_Contact_Number INT
);

	-- Item Table:
    CREATE TABLE Item (
    Item_ID INT PRIMARY KEY,
    Item_Name VARCHAR(40),
    Supplier_ID INT,
    Height DECIMAL,
    Weight DECIMAL,
    Stored_Time DATETIME,
    Type_of_Item VARCHAR(45),
    Storage_Condition VARCHAR(45),
    FOREIGN KEY (Supplier_ID) REFERENCES Supplier(Supplier_ID)
);

	-- Borrowed_History Table
    CREATE TABLE Borrowed_History (
    Borrowed_Item_ID INT PRIMARY KEY,
    Item_ID INT,
    Borrowed_Duration DOUBLE,
    Return_Date DATE,
    Return_Condition VARCHAR(45),
    Guest_User_Name VARCHAR(45),
    FOREIGN KEY (Guest_User_Name) REFERENCES Guest_User(Guest_User_Name),
    FOREIGN KEY (Item_ID) REFERENCES Item(Item_ID)
);

	-- Favorite_Item Table:
    CREATE TABLE Favorite_Item (
    Favorite_ID INT PRIMARY KEY,
    Item_ID INT,
    Favorite_Date DATE,
    Comments TEXT,
    Guest_User_Name VARCHAR(45),
    FOREIGN KEY (Guest_User_Name) REFERENCES Guest_User(Guest_User_Name),
    FOREIGN KEY (Item_ID) REFERENCES Item(Item_ID)
);

	-- Request Table:
    CREATE TABLE Request (
    Request_ID INT PRIMARY KEY,
    Guest_User_Name VARCHAR(45),
    Item_ID INT,
    Borrowed_Duration DOUBLE,
    Request_Type VARCHAR(45),
    Request_Status VARCHAR(45),
    Return_Date DATE,
    FOREIGN KEY (Guest_User_Name) REFERENCES Guest_User(Guest_User_Name),
    FOREIGN KEY (Item_ID) REFERENCES Item(Item_ID)
);

	-- Orders Table:
    CREATE TABLE Orders (
    Order_ID INT PRIMARY KEY,
    Order_Date DATE,
    Order_Status VARCHAR(45),
    Order_Type VARCHAR(45),
    Guest_Address VARCHAR(255),
    Price DECIMAL,
    Payment_Method VARCHAR(45),
    Sales_Discounts VARCHAR(45),
    Item_ID INT,
    FOREIGN KEY (Item_ID) REFERENCES Item(Item_ID)
);

	-- Returns Table:
    CREATE TABLE Returns (
    Returns_ID INT PRIMARY KEY,
    Item_ID INT,
    Orders_ID INT,
    Guest_User_Name VARCHAR(45),
    Orders_Date DATE,
    Guest_Address VARCHAR(255),
    FOREIGN KEY (Guest_User_Name) REFERENCES Guest_User(Guest_User_Name),
    FOREIGN KEY (Item_ID) REFERENCES Item(Item_ID),
    FOREIGN KEY (Orders_ID) REFERENCES Orders(Order_ID)
);

	-- Department Table:
    CREATE TABLE Department (
    Department_ID INT PRIMARY KEY,
    Department_Name VARCHAR(45),
    Manager_Name VARCHAR(45),
    Quantity INT,
    Department_Type VARCHAR(45)
);

-- 2NF: no partial dependencies, tables already in 2NF

-- 3NF:
	-- Orders Table:
    -- Splitting Orders table into two tables to eliminate transitive dependencies
CREATE TABLE Orders (
    Order_ID INT PRIMARY KEY,
    Order_Date DATE,
    Order_Status VARCHAR(45),
    Guest_Address VARCHAR(255),
    Price DECIMAL,
    Payment_Method VARCHAR(45),
    Sales_Discounts VARCHAR(45)
);

CREATE TABLE Order_Items (
    Order_ID INT,
    Item_ID INT,
    PRIMARY KEY (Order_ID, Item_ID),
    FOREIGN KEY (Order_ID) REFERENCES Orders(Order_ID),
    FOREIGN KEY (Item_ID) REFERENCES Item(Item_ID)
);

select * from Item;
select * from Guest_user;
select * from admin_user;
select * from supplier;
