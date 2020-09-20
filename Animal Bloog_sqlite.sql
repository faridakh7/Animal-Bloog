CREATE TABLE User (
	id integer PRIMARY KEY AUTOINCREMENT,
	Name varchar,
	Surname varchar,
	Email varchar,
	Password varchar
);

CREATE TABLE Animal (
	id integer PRIMARY KEY AUTOINCREMENT,
	Name string,
	description text
);

CREATE TABLE Kind (
	id integer PRIMARY KEY AUTOINCREMENT,
	Name string,
	description string PRIMARY KEY AUTOINCREMENT,
	file text PRIMARY KEY AUTOINCREMENT,
	post_id integer
);

CREATE TABLE "Animal Name_Post" (
	id integer PRIMARY KEY AUTOINCREMENT,
	title string,
	food string PRIMARY KEY AUTOINCREMENT,
	psychology string PRIMARY KEY AUTOINCREMENT,
	file varchar PRIMARY KEY AUTOINCREMENT,
	create_time datetime,
	update_time date
);

CREATE TABLE Comment (
	id integer PRIMARY KEY AUTOINCREMENT,
	text string,
	create_time date,
	user_id integer,
	post_id integer
);

CREATE TABLE Reply (
	id integer PRIMARY KEY AUTOINCREMENT,
	user_id integer,
	comment_id integer
);

CREATE TABLE Gallery (
	id integer PRIMARY KEY AUTOINCREMENT,
	file varchar PRIMARY KEY AUTOINCREMENT,
	title varchar PRIMARY KEY AUTOINCREMENT
);

