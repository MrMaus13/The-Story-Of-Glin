
# main.py

import os
import curses
import datetime
from player import Player
from game_utils import save_game, load_game, load_high_scores, update_high_scores, display_news
from gameplay import main_menu

def init_colors():
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Green text on black
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # Red text on black
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK) # Yellow text on black
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)   # Cyan text on black
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK) # Magenta text on black
    curses.init_pair(6, curses.COLOR_BLUE, curses.COLOR_BLACK)    # Blue text on black

def check_player_status(player):
    """Check if the player died today and quit if necessary."""
    today = datetime.date.today()
    if player.last_death_date == today:
        print(f"Sorry {player.name}, you died today. You can only log in tomorrow.")
        exit()

def character_creation(stdscr, player):
    title_art = """
    ***************************************
    *      Welcome to The Story of Glin    *
    ***************************************
    """
    stdscr.clear()
    stdscr.addstr(0, 0, title_art, curses.color_pair(1))

    # Get system login name as default
    login_name = os.getlogin()
    player.name = login_name
    stdscr.addstr(5, 0, f"Welcome, {player.name}! Prepare for your adventure.\nPress any key to continue...",curses.color_pair(4)| curses.A_BOLD)
    stdscr.getch()

def main(stdscr):
    init_colors()  # Initialize colors
    player = load_game(Player)
    
    # Check if player died today
    #check_player_status(player)


    character_creation(stdscr, player)

    stdscr.clear()
    stdscr.border()  # Add border around the main window
    stdscr.addstr(0, 2, " THE STORY OF GLIN ", curses.color_pair(3) | curses.A_BOLD)
    stdscr.refresh()

    # Display high scores and news
    stdscr.addstr(2, 2, "High Scores:",curses.color_pair(2) | curses.A_BOLD)
    load_high_scores(stdscr)
    stdscr.addstr(12, 2, "Recent News:",curses.color_pair(2) | curses.A_BOLD)
    display_news(stdscr)
    stdscr.addstr(22, 2, "Press any key to start the game...",curses.color_pair(4)| curses.A_BOLD)
    stdscr.getch()

    main_menu(stdscr, player)
    update_high_scores(player)
    save_game(player)

if __name__ == "__main__":
    curses.wrapper(main)
