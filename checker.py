# checker.py

# Imports
import json
from pathlib import Path

# Constants
TEST_FOLLOWING = Path("followers_and_following/following.json")
TEST_FOLLOWERS = Path("followers_and_following/followers_1.json")

# Takes in a Path object. Converts the following json into a list of usernames.
def get_following(following_path : Path) -> list[str]:
	with open(following_path, "r") as following_json:
		following_list = []
		following_dict = json.load(following_json)

		for section in following_dict["relationships_following"]:
			following_list.append(section["string_list_data"][0]["value"])

		return following_list

# Takes in a Path object. Converts the follower json into a list of usernames.
def get_followers(follower_path : Path) -> list[str]:
	with open(follower_path, "r") as follower_json:
		follower_return_list = []
		follower_file_list = json.load(follower_json)

		for section in follower_file_list:
			follower_return_list.append(section["string_list_data"][0]["value"])

		return follower_return_list

# Takes in two lists of usernames. Compares them to see which usernames 
# are missing between the two. Returns a tuple w/ two lists of missing names
def compare_following_and_followers(following : list[str], followers : list[str]) -> tuple[list[str]]:
	missing_from_followers = []
	missing_from_following = []

	for following_name in following:
		if following_name not in followers:
			missing_from_followers.append(following_name)

	for follower_name in followers:
		if follower_name not in following:
			missing_from_following.append(follower_name)

	return (missing_from_followers, missing_from_following)

# Takes in a tuple w/ two lists of usernames. Prints out each one.
def print_difference(results : tuple[list[str]]) -> None:	
	print(str(len(results[0])) + " people missing from followers:")
	for name in sorted(results[0]):
		print(name)

	print("\n" + str(len(results[1])) + " people missing from following:")
	for name in sorted(results[1]):
		print(name)

# Main function
def main():	
	following = get_following(TEST_FOLLOWING)
	followers = get_followers(TEST_FOLLOWERS)

	results = compare_following_and_followers(following, followers)
	print_difference(results)


if __name__ == "__main__":
	main()
