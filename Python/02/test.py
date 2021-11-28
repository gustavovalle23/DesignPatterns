from factory import create_core


def create_mock():
    def start():
        print('[mock] ...')

    def stop():
        print('[mock] ...')

    return {'start': start, 'stop': stop}


database_mock = create_mock()

core = create_core({
    'database': database_mock
})


try:
    core['start']()
    core['stop']()
except Exception as err:
    print('[index] Uncaught error!')
    print(err)
