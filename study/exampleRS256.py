from fastapi_users.authentication import JWTStrategy

PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
# Your RSA public key in PEM format goes here
-----END PUBLIC KEY-----"""

PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
# Your RSA private key in PEM format goes here
-----END RSA PRIVATE KEY-----"""


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=PRIVATE_KEY,
        lifetime_seconds=3600,
        algorithm="RS256",
        public_key=PUBLIC_KEY,
    )


print(get_jwt_strategy())
print(get_jwt_strategy().__dict__)