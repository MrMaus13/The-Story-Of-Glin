
import os
import json
import datetime
import curses

HIGH_SCORES_FILE = "data/high_scores.json"
NEWS_FILE = "data/news.json"

def save_game(player):
    """Save the player's game data to a file."""
    try:
        with open(f"data/{player.name}_save.json", 'w') as f:
            json.dump(player.to_dict(), f)
        print("Game saved successfully.")
    except (IOError, OSError) as e:
        print(f"Error saving game: {e}")

def load_game(PlayerClass):
    """Load the player's game data from a file. Returns a Player instance."""
    if not os.path.exists(f"data/{os.getlogin()}_save.json"):
        return PlayerClass()

    try:
        with open(f"data/{os.getlogin()}_save.json", 'r') as f:
            data = json.load(f)
            return PlayerClass.from_dict(data)
    except (IOError, OSError, json.JSONDecodeError) as e:
        print(f"Error loading game: {e}")
        return PlayerClass()

def load_high_scores(stdscr):
    """Load and display the high scores on the screen using curses."""
    if os.path.exists(HIGH_SCORES_FILE):
        try:
            with open(HIGH_SCORES_FILE, 'r') as f:
                high_scores = json.load(f)
                stdscr.addstr(3, 3, "TOP 5 PLAYERS", curses.color_pair(3))
                for i, score in enumerate(high_scores[:5], start=4):
                    stdscr.addstr(i, 3, f"{i - 3}. {score['name']} - Level {score['level']} - XP {score['xp']}", curses.color_pair(5))
        except (IOError, OSError, json.JSONDecodeError) as e:
            print(f"Error loading high scores: {e}")

def update_high_scores(player):
    """Update the high scores file with the current player's data."""
    high_scores = []
    if os.path.exists(HIGH_SCORES_FILE):
        try:
            with open(HIGH_SCORES_FILE, 'r') as f:
                high_scores = json.load(f)
        except (IOError, OSError, json.JSONDecodeError):
            pass

    high_scores.append({"name": player.name, "level": player.level, "xp": player.xp})
    with open(HIGH_SCORES_FILE, 'w') as f:
        json.dump(high_scores, f)

def display_news(stdscr):
    """Display recent news events on the screen using curses."""
    if os.path.exists(NEWS_FILE):
        try:
            with open(NEWS_FILE, 'r') as f:
                news = json.load(f)
                for i, event in enumerate(news[-5:], start=13):
                    stdscr.addstr(i, 3, f"- {event}", curses.color_pair(5))
        except (IOError, OSError, json.JSONDecodeError) as e:
            print(f"Error displaying news: {e}")

def add_news(event):
    """Add a new event to the news file."""
    news = []
    if os.path.exists(NEWS_FILE):
        try:
            with open(NEWS_FILE, 'r') as f:
                news = json.load(f)
        except (IOError, OSError, json.JSONDecodeError):
            pass

    news.append(event)
    with open(NEWS_FILE, 'w') as f:
        json.dump(news, f)

def is_new_day(last_date):
    """Check if the current day is different from the provided date."""
    return datetime.date.today() != last_date
