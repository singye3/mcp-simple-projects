from fastapi import APIRouter, Depends, HTTPException
from src.database import list_notes, query_notes, add_note, update_note, delete_note
from src.models import Note, NoteCreate, NoteUpdate
from src.auth import get_current_user
from typing import List

router = APIRouter()

@router.get("/notes", response_model=List[Note])
async def get_notes(user_id: str = Depends(get_current_user)):
    return list_notes(user_id)

@router.get("/notes/search", response_model=List[Note])
async def search_notes(keyword: str, user_id: str = Depends(get_current_user)):
    return query_notes(keyword, user_id)

@router.post("/notes", response_model=Note)
async def create_note(note: NoteCreate, user_id: str = Depends(get_current_user)):
    return add_note(note.title, note.content, note.tags, user_id)

@router.put("/notes/{note_id}", response_model=Note)
async def update_note_api(note_id: int, note: NoteUpdate, user_id: str = Depends(get_current_user)):
    updated_note = update_note(note_id, note.title or "", note.content or "", note.tags or "", user_id)
    if not updated_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return updated_note

@router.delete("/notes/{note_id}")
async def delete_note_api(note_id: int, user_id: str = Depends(get_current_user)):
    deleted = delete_note(note_id, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note deleted"}