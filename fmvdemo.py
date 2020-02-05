bashcommand = "ffplay -autoexit -window_title FMV-demo fish.ogv"
import subprocess
process = subprocess.Popen(bashcommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
