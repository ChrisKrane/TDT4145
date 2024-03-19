-- SQL script to create the database for DB1 of project in TDT4145.
--    By: 
--    Group 113
--    Christer Justad Krane
--    Karl Krane Frostrud
--    Nikolai Thougaard

-- Drop existing tables if there are any
DROP TABLE IF EXISTS Theater;
DROP TABLE IF EXISTS TheaterHall;
DROP TABLE IF EXISTS Play;
DROP TABLE IF EXISTS Performance;
DROP TABLE IF EXISTS Employee;
DROP TABLE IF EXISTS Task;
DROP TABLE IF EXISTS Role;
DROP TABLE IF EXISTS Actor;
DROP TABLE IF EXISTS Act;
DROP TABLE IF EXISTS Seat;
DROP TABLE IF EXISTS Ticket;
DROP TABLE IF EXISTS CostumerProfile;
DROP TABLE IF EXISTS RoleInAct;
DROP TABLE IF EXISTS PlaysInRole;
DROP TABLE IF EXISTS Execute;

-- Create tables
CREATE TABLE Theater (
  TheaterID int NOT NULL,
  Name varchar(255),
  Place varchar(255),
  PRIMARY KEY (theaterID)
);

CREATE TABLE TheaterHall (
  HallID int NOT NULL,
  HallName varchar(255),
  Capacity int,
  TheaterID int NOT NULL,
  PRIMARY KEY (HallID),
  FOREIGN KEY (TheaterID) REFERENCES Theater(TheaterID)
);

CREATE TABLE Play (
  PlayID int NOT NULL,
  PlayName varchar(255),
  Season varchar(255) NOT NULL,
  HallID int NOT NULL,
  PRIMARY KEY (PlayID),
  FOREIGN KEY (HallID) REFERENCES TheaterHall(HallID)
);

CREATE TABLE Performance (
  PerformanceID int NOT NULL,
  Date date NOT NULL,
  Time time NOT NULL,
  PlayID int NOT NULL,
  PRIMARY KEY (PerformanceID),
  FOREIGN KEY (PlayID) REFERENCES Play(PlayID)
);

CREATE TABLE Employee (
  EmployeeID int NOT NULL,
  email varchar(255),
  Name varchar(255),
  EmployeeStatus varchar(255),
  PlayID int NOT NULL,
  PRIMARY KEY (EmployeeID),
  FOREIGN KEY (PlayID) REFERENCES Play(PlayID)
);

CREATE TABLE Task (
    TaskID int NOT NULL,
    Description varchar(1000),
    PRIMARY KEY (TaskID)
);

CREATE TABLE Role (
    RoleID int NOT NULL,
    Name varchar(255),
    PlayID int NOT NULL,
    PRIMARY KEY (RoleID),
    FOREIGN KEY (PlayID) REFERENCES Play(PlayID)
);

CREATE TABLE Actor (
    ActorID int NOT NULL,
    Name varchar(255),
    PRIMARY KEY (ActorID)
);

CREATE TABLE Act (
    PlayID int NOT NULL,
    Number int NOT NULL,
    Name varchar(255),
    PRIMARY KEY (PlayID, Number),
    FOREIGN KEY (PlayID) REFERENCES Play(PlayID)
);

CREATE TABLE Seat (
    SeatNumber int NOT NULL,
    RowNumber int NOT NULL,
    Area varchar(255) NOT NULL,
    HallID int NOT NULL,
    PRIMARY KEY (SeatNumber, RowNumber, Area, HallID),
    FOREIGN KEY (HallID) REFERENCES TheaterHall(HallID)
);

CREATE TABLE Ticket (
    TicketID int NOT NULL,
    Price float,
    CostumerGroup varchar(255),
    TimeOfSale datetime,
    PerformanceID int NOT NULL,
    CostumerID int NOT NULL,
    SeatNumber int,
    RowNumber int,
    Area varchar(255),
    HallID int NOT NULL,
    PRIMARY KEY (TicketID),
    FOREIGN KEY (PerformanceID) REFERENCES Performance(PerformanceID),
    FOREIGN KEY (CostumerID) REFERENCES Costumer(CostumerID)
);

CREATE TABLE CostumerProfile (
    CostumerID int NOT NULL,
    PhoneNumber varchar(255),
    Name varchar(255),
    Address varchar(255),
    PRIMARY KEY (CostumerID) 
);

CREATE TABLE RoleInAct (
    RoleID int NOT NULL,
    PlayID int NOT NULL,
    Number int NOT NULL,
    PRIMARY KEY (RoleID, PlayID, Number),
    FOREIGN KEY (RoleID) REFERENCES Role(RoleID),
    FOREIGN KEY (PlayID, Number) REFERENCES Act(PlayID, Number)
);

CREATE TABLE PlaysInRole (
    RoleID int NOT NULL,
    ActorID int NOT NULL,
    PRIMARY KEY (RoleID, ActorID),
    FOREIGN KEY (RoleID) REFERENCES Role(RoleID),
    FOREIGN KEY (ActorID) REFERENCES Actor(ActorID)
);

CREATE TABLE Execute (
    EmployeeID int NOT NULL,
    TaskID int NOT NULL,
    PRIMARY KEY (EmployeeID, TaskID),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
    FOREIGN KEY (TaskID) REFERENCES Task(TaskID)
);
