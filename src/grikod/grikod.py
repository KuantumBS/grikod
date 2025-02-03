class InvalidBinaryError(Exception):
    pass

def ikili_2_gri_kod(i2grik: str) -> str:
    """Converts a binary string to its corresponding Gray Code."""
    if len(i2grik) > 64:
        raise InvalidBinaryError("Error: Binary number is too long (max 64 bits).")
    
    try:
        i2grikod = int(i2grik, 2)
    except ValueError:
        raise InvalidBinaryError("Error: Please enter a valid binary number.")
    
    i2grikod ^= (i2grikod >> 1)
    return bin(i2grikod)[2:].zfill(len(i2grik))

# Main program loop
while True:
    i2grik = input("Enter a binary number (or 'q' to quit): ")
    if i2grik.lower() == 'q':
        print("Exiting...")
        break
    
    try:
        gri_kod = ikili_2_gri_kod(i2grik)
        print("Gray Code number:", gri_kod)
    except InvalidBinaryError as e:
        print(e)
        
