import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from controller.system import SystemController


def main():
    controller = SystemController()
    controller.initialize_all_tables()


if __name__ == '__main__':
    main()
