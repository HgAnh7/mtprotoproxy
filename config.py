import os

# Cổng proxy (Railway bắt buộc phải dùng biến PORT)
PORT = int(os.environ.get("PORT", 443))

# Đọc USERS từ biến môi trường: "username1:secret1;username2:secret2"
# Mỗi secret phải là 32 ký tự hex, không có "ee" ở đầu
USERS = {}
users_env = os.environ.get("USERS")
if users_env:
    for pair in users_env.split(";"):
        if ":" in pair:
            name, secret = pair.split(":", 1)
            USERS[name.strip()] = secret.strip()
else:
    # Mặc định
    USERS = {
        "tg": "00000000000000000000000000000001"
    }

# Chế độ proxy
MODES = {
    "classic": os.environ.get("MODE_CLASSIC", "false").lower() == "true",
    "secure": os.environ.get("MODE_SECURE", "false").lower() == "true",
    "tls": os.environ.get("MODE_TLS", "true").lower() == "true",  # Bật TLS mặc định
}

# Tên miền cho chế độ TLS (bắt buộc nếu bật TLS)
TLS_DOMAIN = os.environ.get("TLS_DOMAIN", "www.google.com")

# Tag quảng cáo proxy từ @MTProxybot
AD_TAG = os.environ.get("AD_TAG")
