# Alien colours #3
colour_list: list[str] = ['🟢', '🟡', '🔴']
alien_color: str = 'green'
scores: int = 0

def check_alien_color(color: str) -> int:
    global scores
    if color == 'green':
        scores += 5
        print_scores(scores, colour_list[0])
    elif color == 'yellow':
        scores += 10
        print_scores(scores, colour_list[1])
    elif color == 'red':
        scores += 15
        print_scores(scores, colour_list[2])
    return scores

def print_scores(scores: int, icon: str) -> None:
    print(f"{icon} You just earned {scores} points for shooting the alien.")
    return None

check_alien_color(alien_color)
alien_color = 'yellow'
check_alien_color(alien_color)
alien_color = 'red'
check_alien_color(alien_color)
alien_color = 'green'
check_alien_color(alien_color)
