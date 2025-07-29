
import curses
import random
import datetime
from items import threats, defense_upgrades, offense_tools
from game_utils import save_game
from player import Player
from config import MOVES_PER_DAY

MAP_FILE = "art/map.asc"

def load_ascii_art(filename):
    """Load ASCII art from a file."""
    with open(filename, 'r') as file:
        return file.readlines()

def display_screen(stdscr, ascii_art, start_y=7):
    """Display ASCII art on the screen using curses."""
    for i, line in enumerate(ascii_art, start=start_y):
        if i >= curses.LINES:
            break
        stdscr.addstr(i, 3, line.rstrip(), curses.color_pair(1))

def display_stats(stdscr, player):
    stdscr.addstr(2, 3, f"Name: {player.name}  Level: {player.level}  XP: {player.xp}  Crypto: {player.money}")
    stdscr.addstr(3, 3, f"HP: {player.hp}/{player.max_hp}  Attack: {player.attack}  Defense: {player.defense}")
    stdscr.addstr(4, 3, f"Skills: {', '.join(player.skills)}  Tools: {', '.join(player.tools)}")
    stdscr.addstr(5, 3, f"Daily Moves: {player.daily_moves}/{MOVES_PER_DAY}")

def explore(stdscr, player):
    # Reset moves if a new day has started
    player.reset_moves_if_new_day()
    
    # Check daily move limit
    if player.daily_moves >= MOVES_PER_DAY:
        stdscr.addstr(4, 0, f"You have reached the maximum of {MOVES_PER_DAY} moves for today. Please wait until tomorrow.")
        stdscr.refresh()
        stdscr.getch()
        return

    # Increment the daily move counter
    player.daily_moves += 1

    stdscr.clear()
    display_stats(stdscr, player)
    stdscr.addstr(5, 0, "You venture into the digital world...")
    stdscr.refresh()
    curses.napms(1000)

    event = random.choices(
        population=["threat", "money", "patch", "nothing"],
        weights=[0.5, 0.2, 0.2, 0.1]
    )[0]

    if event == "threat":
        threat = random.choice(threats)
        stdscr.addstr(7, 0, f"A wild {threat['name']} appears!")
        stdscr.refresh()
        start_combat(stdscr, player, threat)
    elif event == "money":
        money_found = random.randint(5, 30)
        player.money += money_found
        stdscr.addstr(7, 0, f"You found {money_found} crypto!")
    elif event == "patch":
        hp_recovered = random.randint(10, 30)
        player.hp = min(player.max_hp, player.hp + hp_recovered)
        stdscr.addstr(7, 0, f"You found a security patch and recovered {hp_recovered} HP!")
    else:
        stdscr.addstr(7, 0, "You find nothing of interest.")

    stdscr.addstr(9, 0, "Press any key to return to town...")
    stdscr.getch()

def start_combat(stdscr, player, threat):
    stdscr.clear()
    display_stats(stdscr, player)
    stdscr.addstr(4, 0, f"You engage in combat with {threat['name']}!")

    while player.hp > 0 and threat["hp"] > 0:
        display_combat_status(stdscr, player, threat)
        stdscr.addstr(6, 0, "1. Attack\n2. Run")
        stdscr.refresh()
        choice = stdscr.getch()

        if choice == ord('1'):
            process_attack(stdscr, player, threat)
        elif choice == ord('2'):
            stdscr.addstr(8, 0, "You ran away!")
            stdscr.refresh()
            curses.napms(1000)
            return

        stdscr.refresh()
        curses.napms(1000)

    conclude_combat(stdscr, player, threat)

def display_combat_status(stdscr, player, threat):
    stdscr.addstr(5, 0, f"Your HP: {player.hp}  |  Threat HP: {threat['hp']}")

def process_attack(stdscr, player, threat):
    damage = max(1, player.attack - random.randint(0, threat["attack"] // 2))
    threat["hp"] -= damage
    stdscr.addstr(8, 0, f"You dealt {damage} damage!")

    if threat["hp"] > 0:
        threat_damage = max(1, threat["attack"] - random.randint(0, player.defense // 2))
        player.hp -= threat_damage
        stdscr.addstr(9, 0, f"The {threat['name']} dealt {threat_damage} damage!")

def conclude_combat(stdscr, player, threat):
    if player.hp > 0:
        stdscr.addstr(11, 0, f"You defeated the {threat['name']}!")
        player.money += threat["money"]
        player.xp += threat["xp"]
        stdscr.addstr(12, 0, f"You earned {threat['money']} crypto and {threat['xp']} XP!")
    else:
        stdscr.addstr(11, 0, "You were defeated... Game over.")
        stdscr.addstr(12, 0, "You can log in again tomorrow with restored HP.")
        player.last_death_date = datetime.date.today()  # Record the death date
        save_game(player)  # Save the game to preserve death status
        stdscr.getch()
        exit()

    stdscr.refresh()
    stdscr.getch()
def shop(stdscr, player):
    while True:
        stdscr.clear()
        display_stats(stdscr, player)
        stdscr.addstr(4, 0, "Welcome to the dark web!")
        stdscr.addstr(5, 0, "1. Defensive Upgrades\n2. Offensive Tools\n3. Exit")
        stdscr.refresh()

        choice = stdscr.getch()
        if choice == ord('1'):
            visit_defense_shop(stdscr, player)
        elif choice == ord('2'):
            visit_offense_shop(stdscr, player)
        elif choice == ord('3'):
            break

def visit_defense_shop(stdscr, player):
    while True:
        stdscr.clear()
        display_stats(stdscr, player)
        stdscr.addstr(4, 0, "Defense Upgrades - Buy protective gear")
        for i, item in enumerate(defense_upgrades):
            stdscr.addstr(i + 5, 0, f"{i + 1}. {item['name']} (Defense: {item['defense']}, Cost: {item['cost']} money)")
        stdscr.addstr(len(defense_upgrades) + 5, 0, "0. Exit")
        stdscr.refresh()

        choice = stdscr.getch() - ord('0')
        if choice == 0:
            break
        elif 1 <= choice <= len(defense_upgrades):
            item = defense_upgrades[choice - 1]
            if player.money >= item['cost']:
                player.money -= item['cost']
                player.defense += item['defense']
                stdscr.addstr(len(defense_upgrades) + 6, 0, f"You bought {item['name']}!")
            else:
                stdscr.addstr(len(defense_upgrades) + 6, 0, "Not enough money!")
            stdscr.refresh()
            stdscr.getch()

def visit_offense_shop(stdscr, player):
    while True:
        stdscr.clear()
        display_stats(stdscr, player)
        stdscr.addstr(4, 0, "Offense Tools - Buy hacking tools")
        for i, item in enumerate(offense_tools):
            stdscr.addstr(i + 5, 0, f"{i + 1}. {item['name']} (Attack: {item['attack']}, Cost: {item['cost']} money)")
        stdscr.addstr(len(offense_tools) + 5, 0, "0. Exit")
        stdscr.refresh()

        choice = stdscr.getch() - ord('0')
        if choice == 0:
            break
        elif 1 <= choice <= len(offense_tools):
            item = offense_tools[choice - 1]
            if player.money >= item['cost']:
                player.money -= item['cost']
                player.attack += item['attack']
                stdscr.addstr(len(offense_tools) + 6, 0, f"You bought {item['name']}!")
            else:
                stdscr.addstr(len(offense_tools) + 6, 0, "Not enough money!")
            stdscr.refresh()
            stdscr.getch()

def visit_inn(stdscr, player):
    while True:
        stdscr.clear()
        display_stats(stdscr, player)
        stdscr.addstr(4, 0, "Cyber Cafe - Rest and relax")
        stdscr.addstr(5, 0, "1. Buy Energy Drink (10 crypto)\n2. Talk to the Unix Guru\n3. Exit")
        stdscr.refresh()

        choice = stdscr.getch()
        if choice == ord('1'):
            if player.money >= 10:
                player.money -= 10
                player.hp = player.max_hp
                stdscr.addstr(7, 0, "You bought a Energy Drink and feel fully refreshed!")
            else:
                stdscr.addstr(7, 0, "Not enough crypto!")
            stdscr.refresh()
            stdscr.getch()
        elif choice == ord('2'):
            visit_unix_guru(stdscr,player)
        elif choice == ord('3'):
            break

def visit_unix_guru(stdscr, player):
    stdscr.clear()
    stdscr.addstr(0, 0, "You enter the Cybercafe and meet the Unix Guru.")
    stdscr.addstr(2, 0, "The Unix Guru can help you level up if you have enough XP.")
    stdscr.addstr(4, 0, "Press 'L' to level up or any other key to leave.")
    key = stdscr.getch()
    if key in [ord('L'), ord('l')]:
        if player.can_level_up():
            player.level_up()
            stdscr.addstr(6, 0, "You have leveled up! Congratulations!")
        else:
            stdscr.addstr(6, 0, "You don't have enough XP to level up.")
    else:
        stdscr.addstr(6, 0, "You decide to leave the Cybercafe.")

    stdscr.addstr(8, 0, "Press any key to continue...")
    stdscr.getch()

def main_menu(stdscr, player):

    # Reset moves if a new day has started
    player.reset_moves_if_new_day()

    # Check if player is dead
    if player.check_login_restriction():
        stdscr.clear()
        stdscr.addstr(10, 0, f"Sorry {player.name}, you died today. You can only log in tomorrow.")
        stdscr.refresh()
        stdscr.getch()
        stdscr.refresh()
        exit()
    else:
        stdscr.clear()
        stdscr.addstr(10, 0, f"You have returned from your defeat {player.name}, your feel refreshed!")
        stdscr.refresh()
        stdscr.getch()
        stdscr.refresh()

    while True:
        stdscr.clear()
        stdscr.border('|', '|', '-', '-', '/', '\\', '\\', '/')

        stdscr.addstr(0, 2, " THE STORY OF GLIN ", curses.color_pair(3) | curses.A_BOLD)
        display_stats(stdscr, player)
        ascii_art = load_ascii_art(MAP_FILE)

        height, _ = stdscr.getmaxyx()
        art_start = 7
        if art_start + len(ascii_art) + 5 >= height:
            art_start = max(0, height - (len(ascii_art) + 6))
        options_start = art_start + len(ascii_art) + 1

        display_screen(stdscr, ascii_art, start_y=art_start)

        if options_start + 4 < height:
            stdscr.addstr(options_start, 3, "Your options")
            stdscr.addstr(options_start + 1, 3, "1. Explore", curses.color_pair(3) | curses.A_BOLD)
            stdscr.addstr(options_start + 2, 3, "2. Visit Darkweb", curses.color_pair(3) | curses.A_BOLD)
            stdscr.addstr(options_start + 3, 3, "3. Visit Cybercafe", curses.color_pair(3) | curses.A_BOLD)
            stdscr.addstr(options_start + 4, 3, "4. Save and Exit", curses.color_pair(3) | curses.A_BOLD)
        stdscr.refresh()

        choice = stdscr.getch()
        if choice == ord('1'):
            explore(stdscr, player)
        elif choice == ord('2'):
            shop(stdscr, player)
        elif choice == ord('3'):
            visit_inn(stdscr, player)
        elif choice == ord('4'):
            save_game(player)
            stdscr.clear()
            stdscr.addstr(10, 0, "Game saved. Goodbye!")
            stdscr.refresh()
            stdscr.getch()
            break
