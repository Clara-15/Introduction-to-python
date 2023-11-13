message = "For your shade is beautiful."
email ="rachaelclara95@gmail.com"
position = "1,2"
phonenumber = "0718959518"
hobbies = "coding, hiking, baking, camping and volunteering"

words = message.split (" ")
email_parts =email.split("@")
user_id =email_parts[0]
hobbies_parts =hobbies.split(" ")
position_parts = position.split(",")

print(words[4])
print(email_parts)
print(position_parts[1])
print(hobbies_parts[2])