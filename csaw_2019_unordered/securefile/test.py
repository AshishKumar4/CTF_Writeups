import base64
import getpass
import os
import sys
import requests

api_base = os.environ.get('SFS_API', 'http://web.chal.csaw.io:1001/api/v1/')

session = requests.Session()

def api_register(username, password):
    resp = session.post(api_base + 'register', data={"username": username, "password": password}).json()
    return resp['status'] == 'ok'

def api_login(username, password):
    resp = session.post(api_base + 'login', data={"username": username, "password": password}).json()
    return resp['status'] == 'ok'

def api_get_file(path):
    resp = session.post(api_base + 'file/read', data={"path": path})
    #if resp.status_code == 200:
    #    return base64.b64decode(resp.content)
    return resp.content

def api_update_file(path, content):
    resp = session.post(api_base + 'file/edit', data={"path": path, "content": content}).json()
    return resp['status'] == 'ok'

def api_create_file(path, content):
    return api_update_file(path, content)

def api_delete_file(path):
    resp = session.post(api_base + 'file/delete', data={"path": path}).json()
    return resp['status'] == 'ok'

def api_list_files(path='/'):
    resp = session.post(api_base + 'file/list', data={"path": path}).json()
    if resp['status'] == 'ok':
        return resp['data']
    return None

def api_create_symlink(path, target):
    resp = session.post(api_base + 'file/symlink', data={"path": path, "target": target}).json()
    return resp['status'] == 'ok'

if __name__ == "__main__":
    try:
        input = raw_input
    except NameError:
        pass

    username = 'vitctf'
    if username is None:
        username = input('Username: ')

    password = 'vitctf'
    if password is None:
        password = getpass.getpass('Password: ')

    if not api_login(username, password):
        print("Invalid username or password")
        sys.exit(1)


#U2FsdGVkX18vg7gzzc/Q2XG2O5vpgFvBvX7nv4mLxfsuKQxvSrMjHu11kDPfUIYVtJ9b5ohVP7olboQV5MDOjQ==