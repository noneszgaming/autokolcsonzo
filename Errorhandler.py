
def catch_all_exceptions(method):
    def wrapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except Exception as e:
            print(f"Exception occurred in {method.__name__}: {e}")

            import time
            for i in range(5, 0, -1):
                print(f"Újraindítás {i} másodperc múlva...")
                time.sleep(1)

            from main import main
            main()

    return wrapper


