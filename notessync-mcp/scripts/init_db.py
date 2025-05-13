import sqlite3
import yaml

# Load configuration
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

DB_PATH = config["database"]["path"]

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create notes table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            tags TEXT,
            user_id TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT
        )
    """)

    # Insert sample data
    sample_notes = [
        ("Meeting Notes", "Discussed project timelines.", "work, meeting", "user1"),
        ("Todo List", "Buy groceries, finish MCP project.", "personal, todo", "user1"),
        ("Idea", "AI-powered note organizer.", "idea, tech", "user1")
    ]
    cursor.executemany(
        "INSERT INTO notes (title, content, tags, user_id, created_at) VALUES (?, ?, ?, ?, datetime('now'))",
        sample_notes
    )

    conn.commit()
    conn.close()
    print("Database initialized with sample data.")

if __name__ == "__main__":
    init_db()