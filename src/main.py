from src.cameras import *

if __name__ == "__main__":
    cam = Camera()

    try:
        while cam.running:
            cam.main_loop()
    finally:
        cam.quit()

