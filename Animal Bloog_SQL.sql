CREATE TABLE User (
	id integer PRIMARY KEY AUTOINCREMENT,
	Name varchar,
	Surname varchar,
	Email varchar,
	Password varchar,
	Country_id string
);

CREATE TABLE Animal (
	id integer PRIMARY KEY AUTOINCREMENT,
	Name string,
	description string
);

CREATE TABLE Kind (
	id integer PRIMARY KEY AUTOINCREMENT,
	Name string,
	description string PRIMARY KEY AUTOINCREMENT,
	country string PRIMARY KEY AUTOINCREMENT,
	file text PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE City (
	id integer PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE Country (
	id integer PRIMARY KEY AUTOINCREMENT,
	Name string PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE Review (
	id integer PRIMARY KEY AUTOINCREMENT,
	AnimalName_id string PRIMARY KEY AUTOINCREMENT,
	user_id string PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE "Animal Name" (
	id integer PRIMARY KEY AUTOINCREMENT,
	color string PRIMARY KEY AUTOINCREMENT,
	food string PRIMARY KEY AUTOINCREMENT,
	psychology string PRIMARY KEY AUTOINCREMENT,
	file text PRIMARY KEY AUTOINCREMENT,
	country_id string PRIMARY KEY AUTOINCREMENT
);

