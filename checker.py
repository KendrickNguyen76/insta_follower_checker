# checker.py

# Imports
import json
from pathlib import Path

# Constants
TEST_FOLLOWING = Path("followers_and_following/following.json")
TEST_FOLLOWERS = Path("followers_and_following/followers_1.json")


def get_following(following_path : Path) -> list[str]:
	with open(following_path, "r") as following_json:
		following_dict = json.load(following_json)

		print(following_dict)

if __name__ == "__main__":
	get_following(TEST_FOLLOWING)
