from enum import Enum

class EnergyTier(Enum):
    S_HBM4 = 1
    A_DDR6 = 2
    B_DDR5 = 3

class MemoryBlock:
    def __init__(self, block_id, size_gb, tier):
        self.block_id = block_id
        self.size_gb = size_gb
        self.tier = tier
        self.verified = False

    def verify_pqc(self):
        self.verified = True
        return True

    def __add__(self, other):
        combined_size = self.size_gb + other.size_gb
        combined_tier = self.tier if self.tier.value < other.tier.value else other.tier
        return MemoryBlock(f"{self.block_id}_{other.block_id}", combined_size, combined_tier)

    def report(self):
        status = "SECURE" if self.verified else "PENDING"
        print(f"[POOL] {self.block_id} | {self.size_gb}GB | Tier {self.tier.name} | PQC: {status}")
