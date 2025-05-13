import sqlite3
from typing import List, Dict, Any
from src.logger import logger
import yaml

# Load configuration
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

DB_PATH = config["database"]["path"]

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def list_notes(user_id: str) -> List[Dict[str, Any]]:
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM notes WHERE user_id = ?", (user_id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]
    except Exception as e:
        logger.error(f"Error listing notes: {str(e)}")
        raise

def query_notes(keyword: str, user_id: str) -> List[Dict[str, Any]]:
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM notes WHERE user_id = ? AND (title LIKE ? OR content LIKE ? OR tags LIKE ?)"
        cursor.execute(query, (user_id, f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]
    except Exception as e:
        logger.error(f"Error querying notes: {str(e)}")
        raise

def add_note(title: str, content: str, tags: str, user_id: str) -> Dict[str, Any]:
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO notes (title, content, tags, user_id, created_at) VALUES (?, ?, ?, ?, datetime('now'))",
            (title, content, tags, user_id)
        )
        conn.commit()
        note_id = cursor.lastrowid
        cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
        note = dict(cursor.fetchone())
        conn.close()
        return note
    except Exception as e:
        logger.error(f"Error adding note: {str(e)}")
        raise

def update_note(note_id: int, title: str, content: str, tags: str, user_id: str) -> Dict[str, Any]:
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE notes SET title = ?, content = ?, tags = ?, updated_at = datetime('now') WHERE id = ? AND user_id = ?",
            (title, content, tags, note_id, user_id)
        )
        conn.commit()
        cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
        note = dict(cursor.fetchone())
        conn.close()
        return note
    except Exception as e:
        logger.error(f"Error updating note: {str(e)}")
        raise

def delete_note(note_id: int, user_id: str) -> bool:
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM notes WHERE id = ? AND user_id = ?", (note_id, user_id))
        conn.commit()
        deleted = cursor.rowcount > 0
        conn.close()
        return deleted
    except Exception as e:
        logger.error(f"Error deleting note: {str(e)}")
        raise