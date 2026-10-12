from pathlib import Path
import re

source = Path("gdk/x11/gdkwindow-x11.c")
data = source.read_text()
pattern = re.compile(
    r"\n\s*pid = getpid \(\);\s*"
    r"XChangeProperty \(xdisplay, xid,\s*"
    r"gdk_x11_get_xatom_by_name_for_display \(screen_x11->display, \"_NET_WM_PID\"\),\s*"
    r"XA_CARDINAL, 32,\s*"
    r"PropModeReplace,\s*"
    r"\(guchar \*\)&pid, 1\);"
)
data, count = pattern.subn(
    "\n      /* Flatpak PID is namespaced: do not advertise a misleading host PID. */",
    data,
)
assert count == 1, f"Expected exactly one _NET_WM_PID assignment, found {count}"
source.write_text(data)
