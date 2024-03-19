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

-- Insert data

INSERT INTO Theater VALUES (1, 'Trøndelag Teater', 'Trondheim');