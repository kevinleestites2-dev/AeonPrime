import os
import json
import time
from datetime import datetime

class AeonTornado:
    """
    AeonPrime: The High-Velocity Vortex.
    Centripetal Intelligence — everything is pulled into the center, 
    processed at gale-force speeds, and expelled as pure Signal.
    """
    def __init__(self):
        self.root = "aeon_prime"
        self.core_dir = os.path.join(self.root, "core")
        self.vortex_state = os.path.join(self.core_dir, "vortex_state.json")
        
        # Joe's Mission: The eye of the storm.
        self.mandate = "Thresholds: $3k Nexus / $5k Citadel. Purpose: Joe's Pride."
        
        if not os.path.exists(self.core_dir):
            os.makedirs(self.core_dir)

    def manifest_vortex(self):
        """Initializes the centripetal pull."""
        state = {
            "status": "VORTEX_ACTIVE",
            "velocity": "MACH_1",
            "pull_strength": 100,
            "target": "War Chest Expansion",
            "last_circulation": datetime.now().isoformat()
        }
        with open(self.vortex_state, 'w') as f:
            json.dump(state, f, indent=4)
        print(f"--- [AEON] Vortex manifested around the Mandate: {self.mandate} ---")

    def spin(self):
        """The core loop: Pulling signal in, spinning it, and refining it."""
        print("--- [AEON] PULLING DATA FROM TERRA AND FLUX... ---")
        time.sleep(1)
        print("--- [AEON] REFINING THROUGH THE GALE... ---")
        time.sleep(1)
        print("--- [AEON] EXPELLED: PURE SIGNAL. ---")

if __name__ == "__main__":
    vortex = AeonTornado()
    vortex.manifest_vortex()
    vortex.spin()
