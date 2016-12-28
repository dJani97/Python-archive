FILE_TO_READ = "sample_file.txt"
FILE_TO_WRITE = "untitled_output.txt"

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def write_file(content, name="untitled_output.txt"):
    file = open(name, "w")
    for line in szoveg:
        file.write(line)
    file.close()



szoveg = []
with open (FILE_TO_READ, "r") as file:
    for line in file:
        szoveg.append(line)
        
for line in szoveg:
    num = szoveg.index(line)
    line = text_to_bits(line) #, "utf-8"  # bytes()
    print (line)
    szoveg[num] = line



write_file(szoveg, FILE_TO_WRITE)

print("Done!")
