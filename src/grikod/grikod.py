from __future__ import annotations


def ikili_2_gri_kod(i2grik: str) -> str:
    """Converts a binary string to its corresponding Gray Code."""
    # Convert string to integer
    i2grikod = int(i2grik, 2)

    # Apply Gray Code transformation
    i2grikod ^= (i2grikod >> 1)

    # Return the result as a binary string
    return bin(i2grikod)[2:]


# Get binary input from the user
i2grik = input("Bir ikili sistem (0, 1; Örnek: 101) sayısı giriniz: ")
gri_kod = ikili_2_gri_kod(i2grik)

# Print the Gray Code result
print("Gri Kod sayısı:", gri_kod)
