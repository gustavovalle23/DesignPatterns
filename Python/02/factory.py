def create_database_connection():
    def start():
        print('> [database] Starting done!')
        raise Exception('Connection failed.')

    def stop():
        print('> [database] Stoping done!')

    return {'start': start, 'stop': stop}


def create_core(configurations: dict = {}):
    database = configurations.get('database') or create_database_connection()

    def start():
        database['start']()
        print('> [core] Starting done!')

    def stop():
        print('> [core] Stopping done!')

    return {'start': start, 'stop': stop}


if __name__ == '__main__':

    core = create_core()

    try:
        core['start']()
        core['stop']()
    except Exception as err:
        print('[index] Uncaught error!')
        print(err)
