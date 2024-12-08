-- alter the character set of the existing database, table and column
USE hbtn_0c_0;
ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;