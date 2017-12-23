import skimage
from skimage import data
import numpy as np
import binascii

# ENCODING

image = skimage.io.imread('resized.bmp')
s = "CAT" #encoded word
s1 =  ' '.join(format(ord(i),'b').zfill(8) for i in s)
arr_bin = []
for val in s1.split():
	arr_bin.append(val) #array to store bin repr. of the string to be encoded

encode_final = ""
for val in arr_bin:
	encode_final = encode_final + val
bit_length = len(arr_bin)
orig = "{0:b}".format(bit_length) # number of bytes to be encoded
to_be_padded = 32 - len(orig)
final = '0'*to_be_padded + orig # padded with 0's to the left
encode_final = final + encode_final
count = 0
encoded_image = []
for arr in image:
	temp1 = []
	for each in arr:
		if(count < len(encode_final)):
			temp = "{0:08b}".format(each)
			temp_arr = list(temp)
			temp_arr[7] = encode_final[count]
			count = count + 1
			temp = "".join(temp_arr)
			changed_bit = int(temp,2)
			temp1.append(changed_bit)
		else:
			temp1.append(each)
	encoded_image.append(temp1)

encoded_numpy = np.array(encoded_image) # encoded image matrix

# DECODING

flattened_numpy = encoded_numpy.flatten()
address_array = flattened_numpy[0:32]
length_encode = ''
for val in address_array:
	temp = "{0:08b}".format(val)
	length_encode = length_encode + temp[7]

int_size = int(length_encode,2)
decode_array = flattened_numpy[32:32 + (int_size*8) + 1]

str1 = ''
decoded_word = ''
for val in decode_array:
	if(len(str1) == 8):
		str1 = int(str1,2)
		decoded_word = decoded_word + str1.to_bytes((str1.bit_length() + 7) // 8, 'big').decode()
		str1 = ''
	str1 = str1 + "{0:08b}".format(val)[7]

print(decoded_word) # decoded word