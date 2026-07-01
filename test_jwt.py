from app.utils.auth import create_access_token

token = create_access_token(
    {"sub": "nandhini@example.com"}
)

print(token)