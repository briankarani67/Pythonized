import bcrypt

def hash_password(password):
    password_bin = password.encode("utf-8")

    hashed_password = bcrypt.hashpw(
        password_bin,
        bcrypt.gensalt()
    )

    return hashed_password.decode("utf-8")

def verify_password(password, hashed_password):
    password_bin = password.encode("utf-8")

    hashed_bin = hashed_password.encode("utf-8")

    return bcrypt.checkpw(
        password_bin,
        hashed_bin
    )