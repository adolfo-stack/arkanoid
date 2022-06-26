from arkanoid import ANCHO, ALTO
from arkanoid.game import Arkanoid


if __name__ == "__main__":
    print(f"El tamaño de la pantalla es: {ANCHO} X {ALTO}")
    juego = Arkanoid()
    juego.jugar()