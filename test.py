from unittest import TestLoader, TextTestRunner


if __name__ == '__main__':
    loader = TestLoader()
    tests = loader.discover('./backend/tests')
    runner = TextTestRunner()
    runner.run(tests)
