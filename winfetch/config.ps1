# ===== WINFETCH CONFIGURATION =====

# Opossum image (put winfetch.png in this folder)
$image = "~/.config/winfetch/winfetch.png"

# Show the image as colored ASCII characters (set to $false or remove for pixel blocks)
$ascii = $false

# Width of the image in characters (lower it if it's too big for your terminal)
$imgwidth = 25

# Pixels with alpha below this are treated as transparent
$alphathreshold = 50

# Info lines to show, in order
@(
    "title"
    "dashes"
    "os"
    "computer"
    "kernel"
    "motherboard"
    "uptime"
    "pkgs"
    "pwsh"
    "terminal"
    "cpu"
    "gpu"
    "memory"
    "disk"
    "battery"
    "blank"
    "colorbar"
)