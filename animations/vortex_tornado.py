import time
import sys
import random

def render_tornado():
    colors = ["\033[94m", "\033[96m", "\033[97m", "\033[90m"] # Blues, Cyans, Whites, Grays
    reset = "\033[0m"
    
    layers = [
        "      ~~~~~      ",
        "    ~~~~~~~~~    ",
        "  ~~~~~~~~~~~~~  ",
        " ~~~~~~~~~~~~~~~ ",
        "  ~~~~~~~~~~~~~  ",
        "    ~~~~~~~~~    ",
        "      ~~~~~      ",
        "       ~~~       ",
        "        ~        "
    ]
    
    print("\n--- [AEON] THE GALE IS CONDENSING. THE TORNADO IS BORN. ---\n")
    
    try:
        for _ in range(50): # 50 frames of rotation
            for i, layer in enumerate(layers):
                # Shift the layer string to simulate rotation
                shift = (time.time() * 10 + i) % len(layer.strip())
                rotated = layer[int(shift):] + layer[:int(shift)]
                color = random.choice(colors)
                sys.stdout.write(f"\r{color}{' ' * (i)}{rotated.strip()}{reset}")
                sys.stdout.flush()
                time.sleep(0.05)
            sys.stdout.write("\n")
    except KeyboardInterrupt:
        print(f"\n{reset}--- [AEON] Vortex Sustained. ---")

if __name__ == "__main__":
    render_tornado()
