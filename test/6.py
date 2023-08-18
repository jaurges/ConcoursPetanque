def create_txt_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(str(content))

# Exemple d'utilisation
file_path = "test.txt"


content = []
for i in range(50):
    var = "équipe" + str(i)
    content.append(var)

create_txt_file(file_path, content)