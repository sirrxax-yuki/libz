import importlib
import os
import sys
from pip._internal import main as _main

sys.path.append(
    os.path.join(
        os.path.join(
            os.path.join(
                os.path.dirname(__file__),
                os.pardir,
            ),
            'backend',
        ),
        'src',
    )
)

def _import(module):
    try:
        globals()[module] = importlib.import_module(module)
    except ImportError:
        print(f"pip install {module} - start.")
        _main(['install', module])
        print(f"pip install {module} - done.")

def main():
    _import('python-dotenv')
    _import('sqlalchemy')
    _import('sqlalchemy-utils')
    _import('mysql-connector-python')

    from controller.system import SystemController

    controller = SystemController()
    print("initialize all tables - start.")
    controller.initialize_all_tables()
    print("initialize all tables - done.")


if __name__ == '__main__':
    main()
