from PIL import Image
from pyzbar import pyzbar

def reverse():

    img = Image.open("visit_card.png")
    saida = pyzbar.decode(img)
    print(saida)
if __name__ == "__main__":
    reverse()
