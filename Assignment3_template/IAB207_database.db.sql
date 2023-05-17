BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Event" (
	"event_id"	INTEGER,
	"user_id"	INTEGER,
	"event_name"	TEXT,
	"event_location"	TEXT,
	"event_date"	DATE,
	"event_time"	TIME,
	"event_description"	TEXT,
	"event_category"	TEXT,
	"event_image"	BLOB,
	"event_ticket_quantity"	INTEGER,
	"event_ticket_price"	DECIMAL,
	"event_status"	TEXT,
	PRIMARY KEY("event_id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "User"("user_id")
);
CREATE TABLE IF NOT EXISTS "Order" (
	"order_id"	INTEGER,
	"user_id"	INTEGER,
	"ticket_id"	INTEGER,
	"date_ordered"	DATE,
	"number_of_tickets"	INTEGER,
	FOREIGN KEY("user_id") REFERENCES "User"("user_id"),
	FOREIGN KEY("ticket_id") REFERENCES "Ticket"("ticket_id")
);
CREATE TABLE IF NOT EXISTS "Ticket" (
	"ticket_id"	INTEGER,
	"event_id"	INTEGER,
	"ticket_type"	TEXT,
	PRIMARY KEY("ticket_id" AUTOINCREMENT),
	FOREIGN KEY("event_id") REFERENCES "Event"("event_id")
);
CREATE TABLE IF NOT EXISTS "User" (
	"user_id"	INTEGER,
	"name"	TEXT,
	"email_address"	TEXT,
	"password"	TEXT,
	"phone_number"	TEXT,
	PRIMARY KEY("user_id")
);
CREATE TABLE IF NOT EXISTS "Comment" (
	"comment_id"	INTEGER,
	"user_id"	INTEGER,
	"event_id"	INTEGER,
	"comment"	TEXT,
	"comment_date"	DATE,
	PRIMARY KEY("comment_id" AUTOINCREMENT),
	FOREIGN KEY("event_id") REFERENCES "Event"("event_id"),
	FOREIGN KEY("user_id") REFERENCES "User"("user_id")
);
COMMIT;
