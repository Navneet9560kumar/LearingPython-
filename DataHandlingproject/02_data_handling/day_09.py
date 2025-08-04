import base64
import os


VALUE_FILE= "vault.txt"


def ecode(text):
      base64.b64decode(text.encode()).decode()



def decode(text):
      base64.b64decode(text.encode()).decode()


def password_strength(password):
      length = len(password)

      has_upper = any( c.isupper()   for c  in password)
      has_dight = any( c.isdigit()  for c  in password)
      has_special = any( c in "!@#$%^&* ().,<>"  for c  in password)


      sum([length >=8 , has_upper, has_dight, has_special ])

      return["Weak","Medium", "Strong", "very Strong "][min(score , 3)]



def add_credential():
      websites = input("Websites: ").strip()
      username= input("Username: ").strip()
      password = input("password: ").strip()

      strength = password_strength(password)

      line = f"{websites}||{username}||{password}"
      encoded_line = encode(line)

      with
      