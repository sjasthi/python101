##############################################################
#  Pet Shelter Manager — SOLUTION KEY
#  Python 101 | Learn and Help Program
#  Metropolitan State University
##############################################################


class Pet:
    # ══════════════════════════════════════════════════════════
    # Task 1: Class Variables (15 pts)
    # These are SHARED by every Pet object
    # ══════════════════════════════════════════════════════════
    total_pets    = 0
    adopted_count = 0
    shelter_name  = "Happy Tails Shelter"

    # ══════════════════════════════════════════════════════════
    # Task 2: Constructor — __init__ (15 pts)
    # Runs automatically when a new Pet object is created
    # ══════════════════════════════════════════════════════════
    def __init__(self, name, species, age, is_adopted=False):
        # Instance variables — unique to each pet
        self.name       = name
        self.species    = species
        self.age        = age
        self.is_adopted = is_adopted

        # Increment the CLASS variable using the class name
        # (NOT self.total_pets — that would create an instance variable!)
        Pet.total_pets += 1

    # ══════════════════════════════════════════════════════════
    # Task 3: Magic Methods (15 pts)
    # ══════════════════════════════════════════════════════════

    def __str__(self):
        """User-friendly string — called by print()"""
        status = "Adopted 🏠" if self.is_adopted else "Available"
        return f"{self.name} ({self.species}) - Age: {self.age} years - Status: {status}"

    def __repr__(self):
        """Developer-friendly string — called by repr()"""
        return f"Pet('{self.name}', '{self.species}', {self.age}, {self.is_adopted})"

    # ══════════════════════════════════════════════════════════
    # Task 4: Instance Methods (20 pts)
    # ══════════════════════════════════════════════════════════

    # ── 4a: adopt() — 8 pts ──
    def adopt(self, owner_name):
        """Marks a pet as adopted and records the owner."""
        if self.is_adopted:
            print(f"{self.name} has already been adopted!")
        else:
            self.is_adopted = True
            self.owner = owner_name              # new instance variable
            Pet.adopted_count += 1               # update class variable
            print(f"🎉 {self.name} has been adopted by {owner_name}!")

    # ── 4b: get_info() — 6 pts ──
    def get_info(self):
        """Returns a dictionary with the pet's data."""
        info = {
            "name":    self.name,
            "species": self.species,
            "age":     self.age,
            "adopted": self.is_adopted
        }
        # Only include owner if the pet has been adopted
        if self.is_adopted:
            info["owner"] = self.owner
        return info

    # ── 4c: celebrate_birthday() — 6 pts ──
    def celebrate_birthday(self):
        """Increases age by 1 and prints a birthday message."""
        self.age += 1
        print(f"🎂 Happy Birthday, {self.name}! Now {self.age} years old.")

    # ══════════════════════════════════════════════════════════
    # Task 5: Class Method & Static Method (15 pts)
    # ══════════════════════════════════════════════════════════

    # ── 5a: shelter_stats() — 10 pts ──
    @classmethod
    def shelter_stats(cls):
        """Returns shelter-wide statistics using class variables."""
        available = cls.total_pets - cls.adopted_count
        return (
            f"📊 {cls.shelter_name} Stats:\n"
            f"   Total pets: {cls.total_pets} | "
            f"Adopted: {cls.adopted_count} | "
            f"Available: {available}"
        )

    # ── 5b: is_senior() — 5 pts ──
    @staticmethod
    def is_senior(species, age):
        """
        Utility method — determines if a pet is a senior.
        Dogs: age >= 7  |  Cats: age >= 10  |  Others: age >= 5
        """
        if species == "Dog":
            return age >= 7
        elif species == "Cat":
            return age >= 10
        else:
            return age >= 5


# ══════════════════════════════════════════════════════════════
# Task 6: Test Script (20 pts)
# ══════════════════════════════════════════════════════════════

# ── Step 1: Create at least 3 pets (4 pts) ──
buddy   = Pet("Buddy", "Dog", 3)
whiskers = Pet("Whiskers", "Cat", 12)
thumper = Pet("Thumper", "Rabbit", 2)

# ── Step 2: Print each pet — tests __str__ (2 pts) ──
print("── All Pets ──")
print(buddy)
print(whiskers)
print(thumper)

# ── Step 3: Print repr() of one pet — tests __repr__ (2 pts) ──
print(f"\nDeveloper view: {repr(buddy)}")

# ── Step 4: Adopt 2 pets, then try adopting one again (3 pts) ──
print("\n── Adoptions ──")
buddy.adopt("Sarah")
whiskers.adopt("Mike")
buddy.adopt("Jake")        # should print "already adopted"

# ── Step 5: Celebrate a birthday (2 pts) ──
print("\n── Birthday ──")
thumper.celebrate_birthday()

# ── Step 6: Print get_info() for adopted and non-adopted (3 pts) ──
print("\n── Pet Info ──")
print(f"Buddy's info:   {buddy.get_info()}")
print(f"Thumper's info: {thumper.get_info()}")

# ── Step 7: Print shelter_stats() (2 pts) ──
print(f"\n{Pet.shelter_stats()}")

# ── Step 8: Use is_senior() on at least 2 pets (2 pts) ──
print("\n── Senior Check ──")
print(f"Is Buddy (Dog, {buddy.age}) a senior?    {Pet.is_senior(buddy.species, buddy.age)}")
print(f"Is Whiskers (Cat, {whiskers.age}) a senior? {Pet.is_senior(whiskers.species, whiskers.age)}")
print(f"Is Thumper (Rabbit, {thumper.age}) a senior? {Pet.is_senior(thumper.species, thumper.age)}")
