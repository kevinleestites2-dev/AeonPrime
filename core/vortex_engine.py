import os
import json
import time
from datetime import datetime

class AeonVortex:
    """
    AeonPrime: The High-Velocity Vortex.
    Centripetal Intelligence — signal refinement and expulsion.
    """
    def __init__(self):
        self.root = "aeon_prime"
        self.core_dir = os.path.join(self.root, "core")
        self.vortex_state = os.path.join(self.core_dir, "vortex_state.json")
        
        if not os.path.exists(self.core_dir):
            os.makedirs(self.core_dir)

    def manifest_vortex(self):
        """Initializes the centripetal pull."""
        state = {
            "status": "VORTEX_ACTIVE",
            "velocity": "MACH_1",
            "last_circulation": datetime.now().isoformat()
        }
        with open(self.vortex_state, 'w') as f:
            json.dump(state, f, indent=4)

    def spin(self):
        """The core loop: Pulling signal in, spinning it, and refining it."""
        print("--- [AEON] PULLING SIGNAL... ---")
        time.sleep(1)
        print("--- [AEON] REFINING... ---")
        time.sleep(1)
        print("--- [AEON] EXPELLED: PURE SIGNAL. ---")

if __name__ == "__main__":
    vortex = AeonVortex()
    vortex.manifest_vortex()
    vortex.spin()
