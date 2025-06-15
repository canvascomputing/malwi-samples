from PIL import Image
from pydub import AudioSegment
import numpy as np
import wave
import sys

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
	print(f"Successfully decoded:\n\n{decoded}")
	song.close()
