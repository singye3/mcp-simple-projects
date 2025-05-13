from modelcontextprotocol import MCP
from src.database import list_notes, query_notes, add_note, update_note, delete_note
from src.auth import get_current_user
from fastapi import Depends

def register_mcp_handlers(mcp: MCP):
    @mcp.resource
    async def notes_resource(user_id: str = Depends(get_current_user)) -> list:
        return list_notes(user_id)

    @mcp.tool
    async def query_notes_tool(keyword: str, user_id: str = Depends(get_current_user)) -> list:
        return query_notes(keyword, user_id)

    @mcp.tool
    async def add_note_tool(title: str, content: str, tags: str, user_id: str = Depends(get_current_user)) -> dict:
        return add_note(title, content, tags, user_id)

    @mcp.tool
    async def update_note_tool(note_id: int, title: str, content: str, tags: str, user_id: str = Depends(get_current_user)) -> dict:
        return update_note(note_id, title, content, tags, user_id)

    @mcp.tool
    async def delete_note_tool(note_id: int, user_id: str = Depends(get_current_user)) -> bool:
        return delete_note(note_id, user_id)