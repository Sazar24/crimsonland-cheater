def setProjectPath():
    """
    ! Deprecated!
    No need to use it thanks to source linked below.
    Source: https://qavalidation.com/2021/03/how-to-resolve-modulenotfounderror-no-module-named-src.html/
    -------
    source: https://stackoverflow.com/questions/43728431/relative-imports-modulenotfounderror-no-module-named-x
    """
    import os
    import sys

    dir_path = os.path.dirname(os.path.realpath(__file__))
    parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
    sys.path.insert(0, parent_dir_path)

#
#  another solutions:
#  https://stackoverflow.com/questions/51049663/python3-6-error-modulenotfounderror-no-module-named-src
