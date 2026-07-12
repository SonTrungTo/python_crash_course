# Alien colours
alien_color: str = 'green'
scores: int = 0

def check_alien_color(color: str) -> int:
    global scores
    if color == 'green':
        scores += 5
        print(f"You just earned {scores} points for shooting the alien.")
        return scores
    return 0

check_alien_color(alien_color)
alien_color = 'yellow'
check_alien_color(alien_color)
alien_color = 'red'
check_alien_color(alien_color)
alien_color = 'green'
check_alien_color(alien_color)
