# Import
import logging

# Settings
CONF_DIR = "test.txt"
CODE_DIR = ""

# Functions
def parse(file_dir=CONF_DIR):
    result = [line.strip() for line in open(file_dir)]
    return result

def mark(data_raw):
    users_keyword = 'users:'
    groups_keyword = 'groups:'
    data_users = []
    data_groups = []

    if users_keyword not in data_raw:
        logging.warning(" Keyword '" + users_keyword + "' not declared in your config file!")
    if groups_keyword not in data_raw:
        logging.warning(" Keyword '" + groups_keyword + "' not declared in your config file!")

    

    result = [data_users, data_groups]
    return result

# Main
print(mark(parse()))