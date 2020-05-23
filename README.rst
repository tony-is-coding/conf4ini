gen4id
======

Installation
>>>>>>>>>>>>>

.. code-block::

    pip install conf4ini

Usage
>>>>>>>>

.. code-block::

    from pathlib import Path
    from pprint import pprint

    from conf4ini import Config

    # not specified path
    conf_no_path = Config()
    pprint(conf_no_path)

    with specified the settings path
    conf_with_path = Config(Path(__file__).resolve().parent / 'dev')
    pprint(conf_with_path)


More
>>>>>>>>>

To Be Continue ....






