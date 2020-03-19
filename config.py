import os
from dotenv import load_dotenv
from pathlib import Path  # python3 only


# Here is a functional example. The "semantics" here
# are each time this code is imported:
#
# * construct the environment path
# * load the environment given the constructed path
# * set the `SECRET` constant by evaluating os.getenv('your key')
#
# Note: importing this kind of code invokes/runs the code, this
#       means that the environment will be loaded on every import,
#       this code has __side effects__.
#
# pathlib has redefined `/` for the the superclass of
# `Path`––`PurePath`. The redefinition of __truediv__
# is what makes `Path('.') / .env` syntax possible.
env_path = Path('.') / '.env'

# Load the environment.
load_dotenv(dotenv_path=env_path)

# Set the secret from the loaded environment.
SECRET = os.getenv("KEY")

# Use the secret.
# built = Builder(token=SECRET)


# Here is an OOP example.
# The semantics here are:
# 
# * on import, load the code from this module
# * when `Config`s constructor is called, load the environment
# * 
class Config:
    def __init__(self, env_path):
        self.env_path = env_path
        load_dotenv(dotenv_path=env_path)

    def get_secret(self, key):
        return os.getenv(key)

class Builder:
    def __init__(self, token):
        self.token = token

    def sign(self):
        # md5, etc
        return "hashed"


# Configuration is assumed to be more involved
# than just this, but this demos building
# configuration and then using this `config`
# value to `Build` upon.
config = Config(env_path=env_path)

b0 = Builder(config.get_secret("KEY0"))
assert(b0.token == "VALUE0")

b1 = Builder(config.get_secret("KEY1"))
assert(b1.token == "VALUE1")

b2 = Builder(config.get_secret("KEY2"))
assert(b2.token == "VALUE2")