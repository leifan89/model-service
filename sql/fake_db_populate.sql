CREATE DATABASE mydb;

\c mydb

CREATE TABLE IF NOT EXISTS category (
  name varchar(10) primary key,
  category varchar(10),
  location varchar(10)
);

INSERT INTO category VALUES ('name1', 'category1', 'loc1');
INSERT INTO category VALUES ('name2', 'category1', 'loc2');
INSERT INTO category VALUES ('name3', 'category1', 'loc3');
INSERT INTO category VALUES ('name4', 'category2', 'loc4');
INSERT INTO category VALUES ('name5', 'category2', 'loc5');
INSERT INTO category VALUES ('name6', 'category3', 'loc6');
