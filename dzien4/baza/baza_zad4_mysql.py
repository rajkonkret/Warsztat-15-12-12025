import os

import pymysql
from dotenv import load_dotenv

# docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:tag

load_dotenv()

conn = pymysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    port=int(os.getenv("DB_PORT")),
)

with conn.cursor() as cur:
    cur.execute("""
                CREATE TABLE IF NOT EXISTS posts
                (
                    id
                    INT
                    AUTO_INCREMENT
                    PRIMARY
                    KEY,
                    title
                    VARCHAR
                (
                    100
                ),
                    body VARCHAR
                (
                    255
                ));
                """)
    conn.commit()
