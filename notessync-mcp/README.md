# NotesSync MCP

A professional notes management system integrated with Anthropic's Model Context Protocol (MCP). Allows users to manage notes via Claude Desktop or a REST API.

## Features

* MCP server with resources (list notes) and tools (query, add, update, delete notes).
* SQLite database with user IDs, timestamps, and tags.
* OAuth 2.1 authentication.
* REST API for non-MCP clients.
* Structured logging and error handling.
* Unit tests with Pytest.
* Deployment-ready for Heroku.

## Setup

### Clone Repository:

```bash
git clone <repository-url>
cd notessync-mcp
```

### Install Dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Initialize Database:

```bash
python scripts/init_db.py
```

### Configure Environment:

Create `config/config.yaml`:

```yaml
database:
  path: notes.db
server:
  host: 0.0.0.0
  port: 8000
oauth:
  client_id: your_client_id
  client_secret: your_client_secret
  auth_url: https://auth-provider.com/authorize
  token_url: https://auth-provider.com/token
```

### Run Server:

```bash
python src/main.py
```

## Configure Claude Desktop

Go to `Settings > Developer > Edit Config` and add:

```json
{
  "servers": [
    {
      "name": "NotesSync MCP",
      "url": "http://localhost:8000",
      "auth": {
        "type": "oauth2",
        "client_id": "your_client_id",
        "client_secret": "your_client_secret",
        "authorization_url": "https://auth-provider.com/authorize",
        "token_url": "https://auth-provider.com/token"
      }
    }
  ]
}
```

## Testing

Run tests:

```bash
pytest tests/
```

## Deployment

### Heroku Setup:

```bash
heroku create notessync-mcp
git push heroku main
```

### Set Config Vars:

```bash
heroku config:set CONFIG_YAML="$(cat config/config.yaml)"
```

## API Documentation

See [docs/api.md](docs/api.md) for REST API details.

## Contributing

1. Fork the repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature/xyz
   ```
3. Commit changes:

   ```bash
   git commit -m "Add xyz"
   ```
4. Push to branch:

   ```bash
   git push origin feature/xyz
   ```
5. Open a pull request.
