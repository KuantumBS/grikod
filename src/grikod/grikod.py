def ikili_2_gri_kod(i2grik: str) -> str | None:
    """Converts a binary string to its corresponding Gray Code."""
    try:
        # Convert binary string to integer
        i2grikod = int(i2grik, 2)
    except ValueError:
        # Return an error message if input is not a valid binary string
        return "Error: Please enter a valid binary number."
    
    # Apply Gray Code transformation
    i2grikod ^= (i2grikod >> 1)
    
    # Return the result as a binary string with preserved length
    return bin(i2grikod)[2:].zfill(len(i2grik))


# Main program loop
while True:
    i2grik = input("Enter a binary number (or 'q' to quit): ")
    if i2grik.lower() == 'q':
        print("Exiting...")
        break
    
    gri_kod = ikili_2_gri_kod(i2grik)
    if gri_kod is not None:
        print("Gray Code number:", gri_kod)
        
