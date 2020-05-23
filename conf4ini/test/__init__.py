from pathlib import Path

from conf4ini import Config

if __name__ == "__main__":
    from pprint import pprint

    # no define path
    conf_no_path = Config()
    pprint(conf_no_path)

    conf_with_path = Config(Path(__file__).resolve().parent / 'dev')
    pprint(conf_with_path)
