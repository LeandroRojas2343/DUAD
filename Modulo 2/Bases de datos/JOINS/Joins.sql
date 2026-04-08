CREATE TABLE Authors (
    ID INT PRIMARY KEY,
    Name VARCHAR(100)
);

CREATE TABLE Books (
    ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Author INT,
    FOREIGN KEY (Author) REFERENCES Authors(ID)
);

CREATE TABLE Customers (
    ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100)
);

CREATE TABLE Rents (
    ID INT PRIMARY KEY,
    BookID INT,
    CustomerID INT,
    State VARCHAR(50),
    FOREIGN KEY (BookID) REFERENCES Books(ID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(ID)
);


/* Authors */
INSERT INTO Authors (ID, Name) VALUES (1,'Miguel de Cervantes');
INSERT INTO Authors (ID, Name) VALUES (2,'Dante Alighieri');
INSERT INTO Authors (ID, Name) VALUES (3,'Takehiko Inoue');
INSERT INTO Authors (ID, Name) VALUES (4,'Akira Toriyama');
INSERT INTO Authors (ID, Name) VALUES (5,'Walt Disney');

/* Books */
INSERT INTO Books (ID, Name, Author) VALUES (1,'Don Quijote',1);
INSERT INTO Books (ID, Name, Author) VALUES (2,'La Divina Comedia',2);
INSERT INTO Books (ID, Name, Author) VALUES (3,'Vagabond 1-3',3);
INSERT INTO Books (ID, Name, Author) VALUES (4,'Dragon Ball 1',4);
INSERT INTO Books (ID, Name, Author) VALUES (5,'The Book of the 5 Rings',NULL);

/* Customers */
INSERT INTO Customers (ID, Name, Email) VALUES (1,'John Doe','j.doe@email.com');
INSERT INTO Customers (ID, Name, Email) VALUES (2,'Jane Doe','jane@doe.com');
INSERT INTO Customers (ID, Name, Email) VALUES (3,'Luke Skywalker','darth.son@email.com');

/* Rents */
INSERT INTO Rents (ID, BookID, CustomerID, State) VALUES (1,1,2,'Returned');
INSERT INTO Rents (ID, BookID, CustomerID, State) VALUES (2,2,2,'Returned');
INSERT INTO Rents (ID, BookID, CustomerID, State) VALUES (3,1,1,'On time');
INSERT INTO Rents (ID, BookID, CustomerID, State) VALUES (4,3,1,'On time');
INSERT INTO Rents (ID, BookID, CustomerID, State) VALUES (5,2,2,'Overdue');


/* 1. Todos los libros y sus autores (incluye libros sin autor) */
SELECT Books.Name AS Book, Authors.Name AS Author
FROM Books
LEFT JOIN Authors
ON Books.Author = Authors.ID;


/* 2. Libros que no tienen autor */
SELECT *
FROM Books
WHERE Author IS NULL;


/* 3. Autores que no tienen libros */
SELECT Authors.*
FROM Authors
LEFT JOIN Books
ON Authors.ID = Books.Author
WHERE Books.ID IS NULL;


/* 4. Libros que han sido rentados */
SELECT DISTINCT Books.*
FROM Books
INNER JOIN Rents
ON Books.ID = Rents.BookID;


/* 5. Libros que nunca han sido rentados */
SELECT Books.*
FROM Books
LEFT JOIN Rents
ON Books.ID = Rents.BookID
WHERE Rents.ID IS NULL;


/* 6. Clientes que nunca han rentado */
SELECT Customers.*
FROM Customers
LEFT JOIN Rents
ON Customers.ID = Rents.CustomerID
WHERE Rents.ID IS NULL;


/* 7. Libros rentados con estado 'Overdue' */
SELECT DISTINCT Books.*
FROM Books
INNER JOIN Rents
ON Books.ID = Rents.BookID
WHERE Rents.State = 'Overdue';