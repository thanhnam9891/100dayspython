import time, os

#name = input("Input your name > ").strip().capitalize()
name = input("Input your name > ").strip().capitalize()
bod = input("Input your date of birth > ").strip()
tel = input("Input your telephone number > ").strip()
email = input("Input your email > ").strip()
address = input("Input your address > ").strip()

contactcard = {
  "name": name,
  "bod": bod,
  "tel": tel,
  "email": email,
  "address":address
}
print()
print(f"""Name: {contactcard["name"]}""")
print(f"""DOB: {contactcard["bod"]}""")
print(f"""Tel: {contactcard["tel"]}""")
print(f"""Email: {contactcard["email"]}""")
print(f"""Address: {contactcard["address"]}""")

time.sleep(1.5)
os.system("clear")

print(f""""Hi {contactcard["name"]}. Our dictionary says that you were born on {contactcard['bod']}, we can call you on {contactcard['tel']}, email {contactcard['email']}, or write to {contactcard['address']}""")