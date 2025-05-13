from fastapi.security import OAuth2AuthorizationCodeBearer
from authlib.integrations.starlette_client import OAuth
from fastapi import Depends, HTTPException, status
import yaml

# Load configuration
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Initialize OAuth
oauth = OAuth()
oauth.register(
    name="auth_provider",
    client_id=config["oauth"]["client_id"],
    client_secret=config["oauth"]["client_secret"],
    authorize_url=config["oauth"]["auth_url"],
    access_token_url=config["oauth"]["token_url"],
    client_kwargs={"scope": "openid profile email"}
)

# OAuth2 scheme for FastAPI
oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=config["oauth"]["auth_url"],
    tokenUrl=config["oauth"]["token_url"],
    auto_error=True
)

async def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    try:
        user = await oauth.auth_provider.userinfo(token=token)
        return user["sub"]  # User ID from OAuth provider
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )