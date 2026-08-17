from random import sample
from libs.randomise import geometric_rand_unbounded, rand_letter

class Lottery:
    """A simple attempt to model a lottery."""

    def __init__(self):
        """Init a lottery instance"""
        self._randomise_number: tuple[int, ...] = tuple(geometric_rand_unbounded(0.5) for _ in range(10))
        self._randomise_letter: tuple[str, ...] = tuple(rand_letter() for _ in range(5))
        self._combined_list: tuple[any, ...] = (*self._randomise_number, *self._randomise_letter)
        # choice() is sample with replacement, so we can have duplicates in the ticket list
        # sample() is sample without replacement, so we cannot have duplicates in the ticket list
        self._ticket_list: list[any] = sample(self._combined_list, 4)

    def show_ticket_list(self):
        """Prints the ticket list"""
        print(f"The winning ticket list is: {self._ticket_list}")

    def get_the_winning_ticket(self):
        """Prints random ticket lists until the winning ticket is found"""
        my_ticket: list[any] = sample(self._combined_list, 4)
        count: int = 0
        while self._ticket_list != my_ticket:
            my_ticket = sample(self._combined_list, 4)
            print(f"Your ticket list is: {my_ticket}")
            count += 1
        print("You won!")
        print(f"It took {count} attempts to win.")

if __name__ == "__main__":
    my_lottery = Lottery()
    my_lottery.show_ticket_list()
    my_lottery.get_the_winning_ticket()
