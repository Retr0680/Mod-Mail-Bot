#     ____       __       ____ 
#    / __ \___  / /______/ __ \
#   / /_/ / _ \/ __/ ___/ / / /
#  / _, _/  __/ /_/ /  / /_/ / 
# /_/ |_|\___/\__/_/   \____/  

from flask import Flask
from threading import Thread

print("     ____       __       ____  ")
print("    / __ \___  / /______/ __ \ ")
print("   / /_/ / _ \/ __/ ___/ / / / ")
print("  / _, _/  __/ /_/ /  / /_/ /  ")
print(" /_/ |_|\___/\__/_/   \____/   ")

app = Flask('')

@app.route('/')
def home():
    return "Infiltration Complete!"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()