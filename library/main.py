"""
MAIN
"""

from library.query import full_crudquery
from library.transform import load


def main():
    """Main function for the Transform-Load and CRUD Query script"""

    # transform and load
    load()

    # query
    full_crudquery()


if __name__ == "__main__":
    main()
