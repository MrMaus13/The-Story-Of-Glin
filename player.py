
# player.py
from game_utils import add_news
import datetime
from config import XP_PER_LEVEL_MULTIPLIER, HP_INCREMENT_PER_LEVEL, ATTACK_INCREMENT_PER_LEVEL, DEFENSE_INCREMENT_PER_LEVEL

class Player:
    def __init__(self, name="", hp=100, max_hp=100, money=50, xp=0, level=1, attack=10, defense=5, 
                 skills=None, tools=None, daily_moves=0, last_reset_date=None, last_death_date=None):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.money = money
        self.xp = xp
        self.level = level
        self.attack = attack
        self.defense = defense
        self.skills = skills if skills is not None else ["Hacking"]
        self.tools = tools if tools is not None else ["Laptop"]
        self.daily_moves = daily_moves
        self.last_reset_date = datetime.date.today() if last_reset_date is None else last_reset_date
        self.last_death_date = last_death_date

    def can_level_up(self):
        return self.xp >= self.level * XP_PER_LEVEL_MULTIPLIER

    def level_up(self):
        if self.can_level_up():
            self.level += 1
            self.xp -= self.level * XP_PER_LEVEL_MULTIPLIER
            self.max_hp += HP_INCREMENT_PER_LEVEL
            self.attack += ATTACK_INCREMENT_PER_LEVEL
            self.defense += DEFENSE_INCREMENT_PER_LEVEL
            add_news(f"{self.name} leveled up to Level {self.level}!")
        else:
            print("Not enough XP to level up.")

    def reset_moves_if_new_day(self):
        if datetime.date.today() != self.last_reset_date:
            self.daily_moves = 0
            self.last_reset_date = datetime.date.today()

    def check_login_restriction(self):
        today = datetime.date.today()
        if self.last_death_date == today:
            return True
        elif self.last_death_date is not None and self.last_death_date < today:
            self.hp = self.max_hp  # Restore HP if it's a new day after death
        return False

    def to_dict(self):
        data = self.__dict__.copy()
        data['last_reset_date'] = self.last_reset_date.isoformat()  # Convert date to string
        data['last_death_date'] = self.last_death_date.isoformat() if self.last_death_date else None
        return data

    @classmethod
    def from_dict(cls, data):
        data['last_reset_date'] = datetime.date.fromisoformat(data['last_reset_date'])  # Convert string to date
        if data['last_death_date']:
            data['last_death_date'] = datetime.date.fromisoformat(data['last_death_date'])
        return cls(**data)
