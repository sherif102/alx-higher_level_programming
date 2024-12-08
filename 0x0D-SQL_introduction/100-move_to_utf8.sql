-- alter the character set of the existing database, table and column
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;