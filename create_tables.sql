DROP TABLE pokemon;

CREATE TABLE pokemon
(Pokemon varchar,
Number int,
height float,
weight float,
HP int,
Attack int,
Defence int,
SpAtk int,
SpDef int,
Speed int,
total int,
Sprite varchar
);

COPY pokemon
FROM '[REPLCE WITH PATH]\pokemon-csv-files\pokemon-all-data.csv'
DELIMITER ','
CSV HEADER;

DROP TABLE moves;

CREATE TABLE moves
(Move varchar,
type varchar,
Category varchar,
Power varchar,
Accuracy varchar,
PowerPoints int
);

COPY moves
FROM '[REPLCE WITH PATH]\pokemon-csv-files\move-data.csv'
DELIMITER ','
CSV HEADER;

DROP TABLE typeRelations;

CREATE TABLE typeRelations
(DefType varchar,
AtkType varchar,
Relation varchar
);

COPY typeRelations
FROM '[REPLCE WITH PATH]\pokemon-csv-files\type-relation-data.csv'
DELIMITER ','
CSV HEADER;

DROP TABLE pokemonAbilities;

CREATE TABLE pokemonAbilities
(Pokemon varchar,
Ability varchar,
Hidden varchar
);

COPY pokemonAbilities
FROM '[REPLCE WITH PATH]\pokemon-csv-files\pokemon-ability-data.csv'
DELIMITER ','
CSV HEADER;

DROP TABLE eggData;

CREATE TABLE eggData
(Pokemon varchar,
Egg_Group varchar
);

COPY eggData
FROM '[REPLCE WITH PATH]\pokemon-csv-files\pokemon-egg-data.csv'
DELIMITER ','
CSV HEADER;

DROP TABLE evolutionData;

CREATE TABLE evolutionData
(Pokemon varchar,
Pre_Evolution varchar,
Method varchar
);

COPY evolutionData
FROM '[REPLCE WITH PATH]\pokemon-csv-files\pokemon-evolution-data.csv'
DELIMITER ','
CSV HEADER;

DROP TABLE pokemonMove;

CREATE TABLE pokemonMove
(Pokemon varchar,
Move varchar,
Source varchar
);

COPY pokemonMove
FROM '[REPLCE WITH PATH]\pokemon-csv-files\pokemon-move-data.csv'
DELIMITER ','
CSV HEADER;

DROP TABLE pokemonTypes;

CREATE TABLE pokemonTypes
(Pokemon varchar,
Type varchar
);

COPY pokemonTypes
FROM '[REPLCE WITH PATH]\pokemon-csv-files\pokemon-type-data.csv'
DELIMITER ','
CSV HEADER;

