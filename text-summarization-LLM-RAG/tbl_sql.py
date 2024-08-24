from config import TABLE1, TABLE2


TABLE_SQL = {
    TABLE2: f"""
    CREATE TABLE IF NOT EXISTS {TABLE2} (
        id INT AUTO_INCREMENT,
        category TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
        vendors TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
        label VARCHAR(12),
        page_content TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
        Date TIMESTAMP,
        SHARD KEY (id),
        SORT KEY (Date)
    );
    """,
    TABLE1: f"""
    CREATE TABLE IF NOT EXISTS {TABLE1} (
        id INT AUTO_INCREMENT,
        category TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
        vendors TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
        label VARCHAR(12),
        page_content TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
        Date TIMESTAMP,
        SHARD KEY (id),
        SORT KEY (Date)
    );
    """,
}
