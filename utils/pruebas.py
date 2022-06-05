from werkzeug.security import check_password_hash, generate_password_hash
password = "admin"
password_hash = generate_password_hash(password)

print(password_hash)