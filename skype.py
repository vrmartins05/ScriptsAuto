from skpy import Skype
import os.path
from getpass import getpass


if os.path.exists('.tokens-my-user'):
    sk = Skype(tokenFile='.tokens-my-user')
    print(sk.conn.tokenExpiry)
else:
    sk = Skype('desenvolvimento13@soitic.com', getpass(), '.tokens-my-user')

print(sk.user)