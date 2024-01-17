-- Change to the database
USE hbtn_0c_0;

-- Convert the database character set and collation
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Convert the table character set and collation
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the field character set and collation
ALTER TABLE first_table CHANGE name name VARCHAR(256) COLLATE utf8mb4_unicode_ci;
