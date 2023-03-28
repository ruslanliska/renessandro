from mj_request import MJRequest

if __name__ == "__main__":
    mj_runner = MJRequest()
    try:
        mj_runner.mj_request()
    finally:
        mj_runner.close_selenium_driver()
