-- SQL script to create the database for DB1 of project in TDT4145.
--    By: 
--    Group 113
--    Christer Justad Krane
--    Karl Krane Frostrud
--    Nikolai Thougaard

-- Insert data
INSERT INTO Theater VALUES (1, 'Trondelag Teater', 'Trondheim');

INSERT INTO TheaterHall VALUES (1, 'Hovedscenen', 524, 1);
INSERT INTO TheaterHall VALUES (2, 'Gamle scene', 332, 1);
INSERT INTO TheaterHall VALUES (3, 'Studioscenen', 150, 1);
INSERT INTO TheaterHall VALUES (4, 'Teaterkjelleren', 60, 1);
INSERT INTO TheaterHall VALUES (5, 'Teaterkafeen', 100, 1);

INSERT INTO Play VALUES (1, 'Kongsemnene av Henrik Ibsen', 450, 380, 280, null, 420, 360, 'winter', 1);
INSERT INTO Play VALUES (2, 'Storst av alt er kjaerligheten av Jonas Corell Petersen', 350, 300, 220, 220, 320, 270, 'winter', 2);

INSERT INTO Performance VALUES (1, '2024-02-01', '19:00', 1);
INSERT INTO Performance VALUES (2, '2024-02-02', '19:00', 1);
INSERT INTO Performance VALUES (3, '2024-02-03', '19:00', 1);
INSERT INTO Performance VALUES (4, '2024-02-05', '19:00', 1);
INSERT INTO Performance VALUES (5, '2024-02-06', '19:00', 1);

INSERT INTO Performance VALUES (6, '2024-02-03', '18:30', 2);
INSERT INTO Performance VALUES (7, '2024-02-06', '18:30', 2);
INSERT INTO Performance VALUES (8, '2024-02-07', '18:30', 2);
INSERT INTO Performance VALUES (9, '2024-02-12', '18:30', 2);
INSERT INTO Performance VALUES (10, '2024-02-13', '18:30', 2);
INSERT INTO Performance VALUES (11, '2024-02-14', '18:30', 2);

INSERT INTO Employee VALUES (1, 'butusov@theater.no', 'Yury Butusov', 'Innleid', 1); 
INSERT INTO Employee VALUES (2, 'shishkin-hokusai@theater.no', 'Aleksandr Shishkin-Hokusai', 'Innleid', 1); 
INSERT INTO Employee VALUES (3, 'myren@theater.no', 'Eivind Myren', 'Fast ansatt', 1); 
INSERT INTO Employee VALUES (4, 'stokke@theater.no', 'Mina Rype Stokke', 'Innleid', 1); 

INSERT INTO Employee VALUES (5, 'petersen@theater.no', 'Jonas Corell Petersen', 'Innleid', 2);
INSERT INTO Employee VALUES (6, 'gehrt@theater.no', 'David Gehrt', 'Midlertidig ansatt', 2);
INSERT INTO Employee VALUES (7, 'tonder@theater.no', 'Gaute Tonder', 'Innleid', 2);
INSERT INTO Employee VALUES (8, 'mikaelsen@theater.no', 'Magnus Mikaelsen', 'Innleid', 2);
INSERT INTO Employee VALUES (9, 'spender@theater.no', 'Kristoffer Spender', 'Innleid', 2);

INSERT INTO Task VALUES (1, 'Regissor');
INSERT INTO Task VALUES (2, 'Scenografi');
INSERT INTO Task VALUES (3, 'Kostyme');
INSERT INTO Task VALUES (4, 'Lysdesign');
INSERT INTO Task VALUES (5, 'Dramaturg');
INSERT INTO Task VALUES (6, 'Musikalsk ansvarlig');

INSERT INTO Role VALUES (1, 'Haakon Haakonssonn', 1);
INSERT INTO Role VALUES (2, 'Inga fra Vartejg (Haakons mor)', 1);
INSERT INTO Role VALUES (3, 'Skule jarl', 1);
INSERT INTO Role VALUES (4, 'Fru Ragnhild (Skules hustru)', 1);
INSERT INTO Role VALUES (5, 'Margrete (Skules datter)', 1);
INSERT INTO Role VALUES (6, 'Sigrid (Skules soster)', 1);
INSERT INTO Role VALUES (7, 'Ingebjorg', 1);
INSERT INTO Role VALUES (8, 'Biskop Nikolas', 1);
INSERT INTO Role VALUES (9, 'Gregorius Jonssonn', 1);
INSERT INTO Role VALUES (10, 'Paal Flida', 1);
INSERT INTO Role VALUES (11, 'Tronder', 1);
INSERT INTO Role VALUES (12, 'Baard Bratte', 1);
INSERT INTO Role VALUES (13, 'Jatgeir Skald', 1);
INSERT INTO Role VALUES (14, 'Dagfinn Bonde', 1);
INSERT INTO Role VALUES (15, 'Peter (prest og Ingebjorgs sonn)', 1);

INSERT INTO Role VALUES (16, 'Sunniva Du Mond Nordal', 2);
INSERT INTO Role VALUES (17, 'Jo Saberniak', 2);
INSERT INTO Role VALUES (18, 'Marte M. Steinholt', 2);
INSERT INTO Role VALUES (19, 'Tor Ivar Hagen', 2);
INSERT INTO Role VALUES (20, 'Trond-Ove Skrodal', 2);
INSERT INTO Role VALUES (21, 'Natalie Grondahl Tangen', 2);
INSERT INTO Role VALUES (22, 'Aasmund Flaten', 2);

INSERT INTO Actor VALUES (1, 'Arturo Scotti');
INSERT INTO Actor VALUES (2, 'Ingunn Beate Strige Oyen');
INSERT INTO Actor VALUES (3, 'Hans Petter Nilsen');
INSERT INTO Actor VALUES (4, 'Madeleine Brandtzaeg Nilsen');
INSERT INTO Actor VALUES (5, 'Synnove Fossum Eriksen');
INSERT INTO Actor VALUES (6, 'Emma Caroline Deichmann');
INSERT INTO Actor VALUES (7, 'Thomas Jensen Takyi');
INSERT INTO Actor VALUES (8, 'Per Bogstad Gulliksen');
INSERT INTO Actor VALUES (9, 'Isak Holmen Sorensen');
INSERT INTO Actor VALUES (10, 'Fabian Heidelberg Lunde');
INSERT INTO Actor VALUES (11, 'Emil Olafsson');
INSERT INTO Actor VALUES (12, 'Snorre Ryen Tondel');
INSERT INTO Actor VALUES (13, 'Sunniva Du Mond Nordal');
INSERT INTO Actor VALUES (14, 'Jo Saberniak');
INSERT INTO Actor VALUES (15, 'Marte M. Steinholt');
INSERT INTO Actor VALUES (16, 'Tor Ivar Hagen');
INSERT INTO Actor VALUES (17, 'Trond-Ove Skrodal');
INSERT INTO Actor VALUES (18, 'Natalie Grondahl Tangen');
INSERT INTO Actor VALUES (19, 'Aasmund Flaten');

INSERT INTO Act VALUES (1, 1, null);
INSERT INTO Act VALUES (1, 2, null);
INSERT INTO Act VALUES (1, 3, null);
INSERT INTO Act VALUES (1, 4, null);
INSERT INTO Act VALUES (1, 5, null);
INSERT INTO Act VALUES (2, 1, null);

INSERT INTO RoleInAct VALUES (1, 1, 1);
INSERT INTO RoleInAct VALUES (1, 1, 2);
INSERT INTO RoleInAct VALUES (1, 1, 3);
INSERT INTO RoleInAct VALUES (1, 1, 4);
INSERT INTO RoleInAct VALUES (1, 1, 5);
INSERT INTO RoleInAct VALUES (2, 1, 1);
INSERT INTO RoleInAct VALUES (2, 1, 3);
INSERT INTO RoleInAct VALUES (3, 1, 1);
INSERT INTO RoleInAct VALUES (3, 1, 2);
INSERT INTO RoleInAct VALUES (3, 1, 3);
INSERT INTO RoleInAct VALUES (3, 1, 4);
INSERT INTO RoleInAct VALUES (3, 1, 5);
INSERT INTO RoleInAct VALUES (4, 1, 1);
INSERT INTO RoleInAct VALUES (4, 1, 5);
INSERT INTO RoleInAct VALUES (5, 1, 1);
INSERT INTO RoleInAct VALUES (5, 1, 2);
INSERT INTO RoleInAct VALUES (5, 1, 3);
INSERT INTO RoleInAct VALUES (5, 1, 4);
INSERT INTO RoleInAct VALUES (5, 1, 5);
INSERT INTO RoleInAct VALUES (6, 1, 1);
INSERT INTO RoleInAct VALUES (6, 1, 2);
INSERT INTO RoleInAct VALUES (6, 1, 5);
INSERT INTO RoleInAct VALUES (7, 1, 4);
INSERT INTO RoleInAct VALUES (8, 1, 1);
INSERT INTO RoleInAct VALUES (8, 1, 2);
INSERT INTO RoleInAct VALUES (8, 1, 3);
INSERT INTO RoleInAct VALUES (9, 1, 1);
INSERT INTO RoleInAct VALUES (9, 1, 2);
INSERT INTO RoleInAct VALUES (9, 1, 3);
INSERT INTO RoleInAct VALUES (9, 1, 4);
INSERT INTO RoleInAct VALUES (9, 1, 5);
INSERT INTO RoleInAct VALUES (10, 1, 1);
INSERT INTO RoleInAct VALUES (10, 1, 2);
INSERT INTO RoleInAct VALUES (10, 1, 3);
INSERT INTO RoleInAct VALUES (10, 1, 4);
INSERT INTO RoleInAct VALUES (10, 1, 5);
INSERT INTO RoleInAct VALUES (13, 1, 4);
INSERT INTO RoleInAct VALUES (14, 1, 1);
INSERT INTO RoleInAct VALUES (14, 1, 2);
INSERT INTO RoleInAct VALUES (14, 1, 3);
INSERT INTO RoleInAct VALUES (14, 1, 4);
INSERT INTO RoleInAct VALUES (14, 1, 5);
INSERT INTO RoleInAct VALUES (15, 1, 3);
INSERT INTO RoleInAct VALUES (15, 1, 4);
INSERT INTO RoleInAct VALUES (15, 1, 5);

INSERT INTO RoleInAct VALUES (16, 2, 1);
INSERT INTO RoleInAct VALUES (17, 2, 1);
INSERT INTO RoleInAct VALUES (18, 2, 1);
INSERT INTO RoleInAct VALUES (19, 2, 1);
INSERT INTO RoleInAct VALUES (20, 2, 1);
INSERT INTO RoleInAct VALUES (21, 2, 1);
INSERT INTO RoleInAct VALUES (22, 2, 1);

INSERT INTO PlaysInRole VALUES (1, 1);
INSERT INTO PlaysInRole VALUES (2, 2);
INSERT INTO PlaysInRole VALUES (3, 3);
INSERT INTO PlaysInRole VALUES (4, 4);
INSERT INTO PlaysInRole VALUES (5, 5);
INSERT INTO PlaysInRole VALUES (6, 6);
INSERT INTO PlaysInRole VALUES (7, 6);
INSERT INTO PlaysInRole VALUES (8, 7);
INSERT INTO PlaysInRole VALUES (9, 8);
INSERT INTO PlaysInRole VALUES (10, 9);
INSERT INTO PlaysInRole VALUES (11, 9);
INSERT INTO PlaysInRole VALUES (12, 10);
INSERT INTO PlaysInRole VALUES (11, 10);
INSERT INTO PlaysInRole VALUES (13, 11);
INSERT INTO PlaysInRole VALUES (14, 11);
INSERT INTO PlaysInRole VALUES (15, 12);

INSERT INTO PlaysInRole VALUES (16, 13);
INSERT INTO PlaysInRole VALUES (17, 14);
INSERT INTO PlaysInRole VALUES (18, 15);
INSERT INTO PlaysInRole VALUES (19, 16);
INSERT INTO PlaysInRole VALUES (20, 17);
INSERT INTO PlaysInRole VALUES (21, 18);
INSERT INTO PlaysInRole VALUES (22, 19);

INSERT INTO Execute VALUES (1, 1);
INSERT INTO Execute VALUES (1, 6);
INSERT INTO Execute VALUES (2, 2);
INSERT INTO Execute VALUES (2, 3);
INSERT INTO Execute VALUES (3, 4);
INSERT INTO Execute VALUES (4, 5);
INSERT INTO Execute VALUES (5, 1);
INSERT INTO Execute VALUES (6, 2);
INSERT INTO Execute VALUES (6, 3);
INSERT INTO Execute VALUES (7, 6);
INSERT INTO Execute VALUES (8, 4);
INSERT INTO Execute VALUES (9, 5);


























