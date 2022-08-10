import asyncio
import argparse

from transfile.backend.peer import Peer
from transfile.backend.tracker import Tracker
from transfile.frontend.terminal import TrackerTerminal, PeerTerminal


def main():
    arg_parser = argparse.ArgumentParser(description=__doc__)
    arg_parser.add_argument('option', metavar='OPTION', type=str, nargs=1)
    results = arg_parser.parse_args()

    loop = asyncio.get_event_loop()

    obj = None
    terminal = None
    
    if results.option[0] == 'tracker':
        obj = Tracker()
        terminal = TrackerTerminal(obj)

    elif results.option[0] == 'peer':
        obj = Peer()
        loop.run_until_complete(obj.start(('localhost', 0)))
        terminal = PeerTerminal(obj)
    else:

        print("Either try tracker or peer")
        exit(0)
    try:
        loop.run_until_complete(terminal.cmdloop())

    except (KeyboardInterrupt, EOFError):
        pass

    finally:
        loop.run_until_complete(obj.stop())
        loop.close()


if __name__ == '__main__':
    main()
