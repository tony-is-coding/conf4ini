from pathlib import PurePath
from collections import defaultdict


class Config(defaultdict):
    """ a simple config reader for *.ini files
    :
    """

    def __init__(self, search_path=None):
        super().__init__(dict)

        #  adjust path

        if search_path is None:
            search_path = "."
        if isinstance(search_path, PurePath):
            search_path = str(search_path)
        self.search_path = search_path + "/settings.ini"

        self.read_file()

    default_factory = dict

    def read_file(self):
        try:
            with open(self.search_path, "r") as f:
                lines = f.readlines()
        except FileExistsError:
            ...
        except IOError:
            ...
        except ValueError:
            ...

        temp_stack = []

        for line in lines:  # type:str
            if line.startswith(("#", "//", "--")) or line == "\n":
                continue
            if line.startswith("["):
                temp_stack.clear()
                temp_stack.append(line.split("[")[1].split("]")[0])
            else:
                # todo: checkout the same config under a parent-config-class
                name, value = line.split("=")  # type: str
                # strip
                name = name.strip().strip("\n")
                value = value.strip().strip("\n")
                if value.isalnum():
                    value = int(value)
                self[temp_stack[0]][name] = value


__all__ = ['Config']
