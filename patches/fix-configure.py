from pathlib import Path

path = Path("configure")
source = path.read_text()
needle = 'if test -z "${am__fastdepCXX_TRUE}" && test -z "${am__fastdepCXX_FALSE}"; then'
assert source.count(needle) == 1, "Unsupported upstream configure layout"
source = source.replace(needle, "am__fastdepCXX_TRUE='#'\nam__fastdepCXX_FALSE=\n" + needle)
path.write_text(source)
