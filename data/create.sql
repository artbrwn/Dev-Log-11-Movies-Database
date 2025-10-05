CREATE TABLE "comentario" (
	"id"	INTEGER,
	"id_pelicula"	TEXT NOT NULL,
	"persona"	TEXT NOT NULL,
	"comentario"	TEXT NOT NULL,
	"fecha"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);