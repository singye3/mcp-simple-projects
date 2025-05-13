import pytest
from src.database import get_db_connection, list_notes, add_note, query_notes, update_note, delete_note

@pytest.fixture
def db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes")
    conn.commit()
    yield conn
    conn.close()

def test_add_note(db):
    note = add_note("Test Note", "Content", "test", "user1")
    assert note["title"] == "Test Note"
    assert note["user_id"] == "user1"

def test_list_notes(db):
    add_note("Note 1", "Content 1", "tag1", "user1")
    add_note("Note 2", "Content 2", "tag2", "user1")
    notes = list_notes("user1")
    assert len(notes) == 2

def test_query_notes(db):
    add_note("Project Note", "Project content", "project", "user1")
    notes = query_notes("project", "user1")
    assert len(notes) == 1
    assert notes[0]["title"] == "Project Note"

def test_update_note(db):
    note = add_note("Old Title", "Old Content", "old", "user1")
    updated = update_note(note["id"], "New Title", "New Content", "new", "user1")
    assert updated["title"] == "New Title"

def test_delete_note(db):
    note = add_note("Note", "Content", "tag", "user1")
    deleted = delete_note(note["id"], "user1")
    assert deleted
    notes = list_notes("user1")
    assert len(notes) == 0