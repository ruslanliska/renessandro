from renessandro.openai_api.mj_request import MJConnection

if __name__ == "__main__":
    mj_runner = MJConnection()
    try:
        mj_runner.mj_request()
    finally:
        mj_runner.close_selenium_driver()
