CREATE TABLE measurement (
	id serial PRIMARY KEY,
	name VARCHAR ( 100 ) UNIQUE NOT NULL,
	location VARCHAR ( 150 ) NOT NULL,
	timestamp TIMESTAMP NOT null,
	puser VARCHAR ( 255 ) NOT NULL,
	value float NOT NULL,
	scale VARCHAR(2) not null,
	comment VARCHAR(250)
)