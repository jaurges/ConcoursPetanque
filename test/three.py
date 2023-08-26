from test_one import MiniBuffer

# Création d'une instance de "mini fichier tampon"
buffer = MiniBuffer()


# Dans une autre partie du code
received_data = buffer.read()
print("Received data:", received_data)  # Cela affichera "Received data: 42"
