from one import MiniBuffer

# Création d'une instance de "mini fichier tampon"
buffer = MiniBuffer()

# Dans une partie du code
data_to_share = 42
buffer.write(data_to_share)

# Dans une autre partie du code
received_data = buffer.read()
print("Received data:", received_data)  # Cela affichera "Received data: 42"
