import os

PORT = int(os.environ.get("PORT", 443))

USERS = {}
users_env = os.environ.get("USERS")
if users_env:
    for pair in users_env.split(";"):
        if ":" in pair:
            name, secret = pair.split(":", 1)
            USERS[name.strip()] = secret.strip()

MODES = {
    "tls": os.environ.get("MODE_TLS", "true").lower() == "true"
}

TLS_DOMAIN = os.environ.get("TLS_DOMAIN", "www.cloudflare.com")
