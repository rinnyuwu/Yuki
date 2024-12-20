import sqlite3

DB_PATH = "database/permissions.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS permissions (
                server_id INTEGER,
                role_id INTEGER,
                permissions TEXT,
                PRIMARY KEY (server_id, role_id)
            )
        """)
        conn.commit()

def update_permissions(server_id, role_id, permissions):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        permissions_str = ",".join(permissions)
        cursor.execute("""
            INSERT INTO permissions (server_id, role_id, permissions)
            VALUES (?, ?, ?)
            ON CONFLICT(server_id, role_id) DO UPDATE SET permissions = excluded.permissions
        """, (server_id, role_id, permissions_str))
        conn.commit()

def get_permissions(server_id, role_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT permissions FROM permissions WHERE server_id = ? AND role_id = ?
        """, (server_id, role_id))
        row = cursor.fetchone()
        return row[0].split(",") if row else []

def delete_permissions(server_id, role_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM permissions WHERE server_id = ? AND role_id = ?
        """, (server_id, role_id))
        conn.commit()