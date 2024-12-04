S1 = "Maha Bharat"
fisrstlettersmall = ''.join([char.lower() if char.isupper() else char.upper() for char in S1])
print(fisrstlettersmall)  # Output: "mAHA bHARAT"

S1 = "Maha Bharat"
substring = S1[S1.index("Bharat"):]
print(substring)  # Output: "Bharat"

S1 = "Maha Bharat"
repeat= "Bharat" * 3
print(repeat)  # Output: "BharatBharatBharat"

S1 = "Maha Bharat"
replace = S1.replace("Maha", "Mera")
print(replace)  # Output: "Mera Bharat"

S1 = "Maha Bharat"
new_string = "Mera Bharat Mahan"
print(new_string)  # Output: "Mera Bharat Mahan"
