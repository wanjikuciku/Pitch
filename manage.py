from app import create_app
from flask_script import Manager,Server





#creating app
app = create_app("production")
app = create_app('test')

manager = Manager(app)
manager.add_command("server",Server)

@manager.command
def test():
    """
    Run the unit tests
    """
    import unittest
    tests = unittest.TestLoader().discover("test")
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == "__main__":
    manager.run()