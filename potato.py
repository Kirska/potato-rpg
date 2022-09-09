"""
Adapted from one page RPG by Oliver Darkshire.
https://twitter.com/deathbybadger/status/1567425842526945280
"""
from random import randint


class PotatoRpg:
    destiny = 0
    potatoes = 0
    orcs = 0
    orc_removal_cost = 1

    def __init__(self):

        self.events = {
            1: self.garden,
            2: self.garden,
            3: self.door,
            4: self.door,
            5: self.orc_increase,
            6: self.orc_increase,
        }
        
        while True:
            print(f"""
            Current values:
            {self.destiny} destiny
            {self.potatoes} potatoes
            {self.orcs} orcs

            {self.orc_removal_cost} potato(es) orc removal cost

            Options:
            1. Roll an event
            2. Remove an orc
            3. Run away (quit)

            """)
            match input("Enter your choice: "):
                case "1":
                    self.event()
                case "2":
                    self.remove_orc()
                case "3":
                    return
                case _:
                    print("Invalid choice")
            
            if self.has_user_reached_end_of_the_game():
                return

    @staticmethod
    def roll():
        return randint(1, 6)

    def event(self):
        roll = self.roll()
        print(f"You rolled a {roll}")
        self.events[roll]()

    def remove_orc(self):
        if self.orcs == 0:
            print("No orcs to remove.")
            input("Press enter to continue...")
            return

        if self.potatoes < self.orc_removal_cost:
            print("You don't have enough potatoes to remove an orc.")
            input("Press enter to continue...")
            return
        
        self.potatoes -= self.orc_removal_cost
        self.orcs -= 1
        print(f"""
        You have removed an orc.
        You now have {self.potatoes} potato(es) and {self.orcs} orc(s).
        """)
        input("Press enter to continue...")

    def garden(self):
        print("You enter the garden.")
        input("Press enter to continue...")

        roll = self.roll()
        print(f"\nYou rolled a {roll} in the garden.")
        
        match roll:
            case 1:
                self.potatoes += 1
                print("You happily root about all day in your garden.")
                print("You have gained 1 potato.")
            case 2:
                self.potatoes += 1
                self.destiny += 1
                print("You narrowly avoid a visitor by hiding in a potato sack.")
                print("You have gained 1 potato and 1 destiny.")
            case 3:
                self.destiny += 1
                self.orcs += 1
                print("A hooded stranger lingers outside your farm.")
                print("You have gained 1 destiny and 1 orc.")
            case 4:
                self.orcs += 1
                self.potatoes -= 1
                print("Your field is ravaged in the night by unseen enemies.")
                print("You have gained 1 orc and lost 1 potato.")
            case 5:
                self.potatoes -= 1
                print("You trade potatoes for other delicious foodstuffs.")
                print("You have lost 1 potato.")
            case 6:
                self.potatoes += 2
                print("You burrow into a bumper crop of potatoes. Do you cry with joy? Possibly.")
                print("You have gained 2 potatoes.")
        input("Press enter to continue...")

    def door(self):
        print("You hear a knock at the door.")
        input("Press enter to continue...")

        roll = self.roll()
        print(f"\nYou rolled a {roll} at the door.")
        
        match roll:
            case 1:
                self.orcs += 1
                print("A distant cousin. They are after your potatoes. They may snitch on you.")
                print("You have gained 1 orc.")
            case 2:
                self.destiny += 1
                print("A dwarven stranger. You refuse them entry. Ghastly creatures.")
                print("You have gained 1 destiny.")
            case 3:
                self.destiny += 1
                self.orcs += 1
                print("A wizard strolls by. You pointedly draw the curtains.")
                print("You have gained 1 destiny and 1 orc.")
            case 4:
                self.orcs += 2
                self.potatoes -= 1
                print("There are rumors of war in the reaches. You eat some potatoes.")
                print("You have gained 2 orcs and lost 1 potato.")
            case 5:
                self.destiny += 1
                print("It's an elf. They are not serious people.")
                print("You have gained 1 destiny.")
            case _:
                self.potatoes += 2
                print("It's a sack of potatoes from a generous neighbor.")
                print("You really must remember to pay them a visit one of these years.")
                print("You have gained 2 potatoes.")
        input("Press enter to continue...")

    def orc_increase(self):
        self.orc_removal_cost += 1
        print(f"""
        The world is now a darker more dangerous place.
        Orc removal cost increased to {self.orc_removal_cost}.
        """)
        input("Press enter to continue...")
        
    def _ensure_scores_never_less_than_zero(self):
        if self.potatoes < 0:
            self.potatoes = 0
        if self.destiny < 0:
            self.destiny = 0
        if self.orcs < 0:
            self.orcs = 0

    def has_user_reached_end_of_the_game(self):
        self._ensure_scores_never_less_than_zero()

        if self.destiny >= 10 and self.orcs < 10:
            print("""
            An interfering bard or wizards has turns up at your doorstep
            with a quest, and you are whisked away against your will on
            an adventure.
            """)
            return True
        if self.potatoes >= 10:
            print("""
            You have enough potatoes that you can go underground and not
            return to the surface until the danger is past. You nestle
            down into your burrow and enjoy your well earned rest.
            """)
            return True
        if self.orcs >= 10:
            print("""
            Orcs finally find your potato farm. Alas, orcs are not so
            interested in potatoes as they are in eating you, and you
            end up in a cookpot.
            """)
            return True

        return False


if __name__ == '__main__':
    PotatoRpg()