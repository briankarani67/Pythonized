import bcrypt

def hash_password(password):
    password_bin = password.encode("utf-8")

    hashed_password = bcrypt.hashpw(
        password_bin,
        bcrypt.gensalt()
    )

    return hashed_password.decode("utf-8")

