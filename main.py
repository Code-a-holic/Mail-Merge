#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
import os

with open(r"../Mail Merge Project Start/Input/Names/invited_names.txt","r") as f:
    names = f.read().splitlines()

txt_files = []
for z in names:
    txt_files.append(z + ".txt")

with open(r"../Mail Merge Project Start/Input/Letters/starting_letter.txt","r") as f2:
    mail_template = f2.read().splitlines()

location = "../Mail Merge Project Start/Output/ReadyToSend/"

print(len(mail_template))
print(mail_template)

for x in range(len(names)):
    file_path = os.path.join(location, txt_files[x])
    with open(file_path, "w") as f:
        f.write(mail_template[0].replace("[name]", names[x]) + "\n")
        f.write("\n")
        f.write(mail_template[1] + "\n")
        f.write("\n")
        f.write(mail_template[2] + "\n")
        f.write("\n")
        f.write(mail_template[3] + "\n")
        f.write("\n")
        f.write(mail_template[4] + "\n")
        f.write("\n")
        f.write(mail_template[5] + "\n")