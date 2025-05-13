from fastapi import FastAPI, Depends
from modelcontextprotocol import MCP, run_server
from src.mcp_handlers import register_mcp_handlers
from src.api_routes import router as api_router
from src.auth import oauth2_scheme
from src.logger import setup_logger
import yaml
import os

# Initialize FastAPI app
app = FastAPI(title="NotesSync MCP", version="1.0.0")p

# Load configuration
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Setup logging
logger = setup_logger()

# Initialize MCP
mcp = MCP(app, oauth2_config=config["oauth"])

# Register MCP handlers
register_mcp_handlers(mcp)

# Include REST API routes
app.include_router(api_router, prefix="/api", dependencies=[Depends(oauth2_scheme)])

# Startup event
@app.on_event("startup")
async def startup_event():
    logger.info("Starting NotesSync MCP server")
    # Initialize database (already done by init_db.py)

# Run server
if __name__ == "__main__":
    run_server(app, host=config["server"]["host"], port=config["server"]["port"])