import cs50
from passlib.apps import custom_app_context as pwd_context

# encrypting a password...
hash = pwd_context.encrypt("somepass")
 # verifying a password...
ok = pwd_context.verify("somepass")
print(hash)
print(ok)