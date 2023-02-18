def RLE_encode(original_msg):
    encode_msg = ""
    serial_count = 1
    
    for i in range(0, len(original_msg)-1):    
        if (original_msg[i] == original_msg[i+1]):
            serial_count += 1
        else:
            encode_msg += str(serial_count) + original_msg[i]
            serial_count = 1
        
        if (i == len(original_msg)-2):
            encode_msg += str(serial_count) + original_msg[-1]
    
    return encode_msg

def RLE_decode(encode_msg):
    decode_msg = ""
    count = ""

    for i in encode_msg:
        if i.isdigit():
            count += i
        elif i.isalpha() or not i.isalnum():
            decode_msg += int(count)*i
            count = ""

    return decode_msg

def RLE_compression_ratio(encoded_msg, original_msg):
    return len(original_msg)/len(encoded_msg)

# Test Case 1: "Gooooooooooooo!"
assert RLE_encode("Gooooooooooooo!") == "1G13o1!"
assert RLE_decode("1G13o1!") == "Gooooooooooooo!"
assert RLE_compression_ratio(RLE_encode("Gooooooooooooo!"), "Gooooooooooooo!") == 15/7

# Test Case 2: "BBBBEEEEEEEECCCCDAAAAA"
assert RLE_encode("BBBBEEEEEEEECCCCDAAAAA") == "4B8E4C1D5A"
assert RLE_decode("4B8E4C1D5A") == "BBBBEEEEEEEECCCCDAAAAA"
assert RLE_compression_ratio(RLE_encode("BBBBEEEEEEEECCCCDAAAAA"), "BBBBEEEEEEEECCCCDAAAAA") == 22/10

# Test Case 3: "multimedia"
assert RLE_encode("multimedia") == "1m1u1l1t1i1m1e1d1i1a"
assert RLE_decode("1m1u1l1t1i1m1e1d1i1a") == "multimedia"
assert RLE_compression_ratio(RLE_encode("multimedia"), "multimedia") == 10/20