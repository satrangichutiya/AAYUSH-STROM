#MIT License
#Copyright (c) 2024 ᴋᴜɴᴀʟ [AFK]

import sys
import glob
import asyncio
import logging
import importlib
import urllib3
from pathlib import Path
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

# Dummy Flask server for Render Web Service
import os
import threading
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Storm Bot is running on Render!"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

threading.Thread(target=run_web).start()

# Logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Plugin loader
def load_plugins(plugin_name):
    path = Path(f"STORM/modules/{plugin_name}.py")
    spec = importlib.util.spec_from_file_location(f"STORM.modules.{plugin_name}", path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["STORM.modules." + plugin_name] = load
    print("✅ STORM imported:", plugin_name)

# Load all plugins from STORM/modules/
files = glob.glob("STORM/modules/*.py")
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("\n✅ STORM BOT IS DEPLOYED SUCCESSFULLY")

# Async run all clients
async def main():
    await asyncio.gather(
        X1.run_until_disconnected(),
        X2.run_until_disconnected(),
        X3.run_until_disconnected(),
        X4.run_until_disconnected(),
        X5.run_until_disconnected(),
        X6.run_until_disconnected(),
        X7.run_until_disconnected(),
        X8.run_until_disconnected(),
        X9.run_until_disconnected(),
        X10.run_until_disconnected(),
    )

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
