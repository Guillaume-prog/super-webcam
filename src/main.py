from src.cameras import *

if __name__ == "__main__":
    cam = Camera(16, 9)

    try:
        while cam.running:
            cam.main_loop()
    finally:
        cam.quit()

