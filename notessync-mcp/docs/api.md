# NotesSync MCP API Documentation

## Base URL
`http://localhost:8000/api` (or your deployed URL)

## Authentication
All endpoints require OAuth 2.1 Bearer token in the `Authorization` header.

## Endpoints

### GET /notes
List all notes for the authenticated user.
- **Response**: `List[Note]`
- **Example**:
  ```json
  [
    {
      "id": 1,
      "title": "Meeting Notes",
      "content": "Discussed project timelines.",
      "tags": "work, meeting",
      "user_id": "user1",
      "created_at": "2025-05-13T14:05:00",
      "updated_at": null
    }
  ]