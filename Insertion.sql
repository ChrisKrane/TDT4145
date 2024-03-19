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

INSERT INTO TheaterHall VALUES (1, 'Hovedscenen', 524, 1);
INSERT INTO TheaterHall VALUES (2, 'Gamle scene', 332, 1);
INSERT INTO TheaterHall VALUES (3, 'Studioscenen', 150, 1);
INSERT INTO TheaterHall VALUES (4, 'Teaterkjelleren', 60, 1);
INSERT INTO TheaterHall VALUES (5, 'Teaterkafeen', 100, 1);

INSERT INTO Play VALUES (1, 'Kongsemnene av Henrik Ibsen', 450, 380, 280, null, 420, 360, 'winter', 1);
INSERT INTO Play VALUES (2, 'Størst av alt er kjærligheten av Jonas Corell Petersen', 350, 300, 220, 220, 320, 270, 'winter', 2);

INSERT INTO Performance VALUES (1, '2024-02-01', '19:00', 1);
INSERT INTO Performance VALUES (2, '2024-02-02', '19:00', 1);
INSERT INTO Performance VALUES (3, '2024-02-03', '19:00', 1);
INSERT INTO Performance VALUES (4, '2024-02-05', '19:00', 1);
INSERT INTO Performance VALUES (5, '2024-02-06', '19:00', 1);

INSERT INTO Performance VALUES (6, '2024-02-03', '18:30', 2);
INSERT INTO Performance VALUES (7, '2024-02-06', '18:30', 2);
INSERT INTO Performance VALUES (8, '2024-02-06', '18:30', 2);
INSERT INTO Performance VALUES (9, '2024-02-12', '18:30', 2);
INSERT INTO Performance VALUES (10, '2024-02-13', '18:30', 2);
INSERT INTO Performance VALUES (11, '2024-02-14', '18:30', 2);

