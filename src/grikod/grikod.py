from __future__ import annotations


def ikili_2_gri_kod(i2grik: str) -> str:
    """Bir ikili sayıyı Gri Koda dönüştürür. Converts a binary string to its corresponding Gray Code."""
    
    try:
        # İkili sayıyı tam sayıya dönüştür: Convert string to integer
        i2grikod = int(i2grik, 2)
    except ValueError:
        # Eğer ikili değilse uyarı mesajı verir: If it’s not binary, it displays a warning message.
        print("\033[1;31mLütfen ondalık sayı yerine ikili sayı giriniz:\nPlease enter a binary number instead of a decimal number.\033[0m")
        return None  # Eğer sayı ikili değilse işlem devam etmez: If the number is not binary, the process does not continue.

    # Gri Kod dönüşümünü uygula: Apply Gray Code transformation
    i2grikod ^= (i2grikod >> 1)

    # Return the result as a binary string
    return bin(i2grikod)[2:]


# Kullanıcıdan ikili giriş alın: Get binary input from the user
i2grik = input(f"Bir ikili sistem (0, 1; Örnek: 101) sayısı giriniz: \nEnter a binary number (0, 1; Example: 101): ")
gri_kod = ikili_2_gri_kod(i2grik)

# Gri Kod sonucunu yazdır: Print the Gray Code result
print("Gri Kod sayısı: Gray Code number:", gri_kod)
