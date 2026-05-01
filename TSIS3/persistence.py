import json
import os

LB_FILE = "leaderboard.json"
SET_FILE = "settings.json"

def load_board():
    if not os.path.exists(LB_FILE):
        return []
    with open(LB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_score(name, score, coins):
    board = load_board()
    board.append({"name": name, "score": score, "coins": coins})
    board = sorted(board, key=lambda x: x["score"], reverse=True)[:10]

    with open(LB_FILE, "w", encoding="utf-8") as f:
        json.dump(board, f, indent=2)

    return board

def load_settings():
    if not os.path.exists(SET_FILE):
        return {"sound": True}
    with open(SET_FILE, "r") as f:
        return json.load(f)

def save_settings(s):
    with open(SET_FILE, "w") as f:
        json.dump(s, f, indent=2)