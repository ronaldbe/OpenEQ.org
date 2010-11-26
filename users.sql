DROP TABLE IF EXISTS "users";
CREATE TABLE "users" (
    "id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , 
    "username" VARCHAR NOT NULL  UNIQUE ,
    "password" VARCHAR NOT NULL ,
    "email" VARCHAR NOT NULL  UNIQUE , 
    "enabled" BOOL NOT NULL , 
    "cansubmit" BOOL NOT NULL ,
    "canapprove" BOOL NOT NULL );
