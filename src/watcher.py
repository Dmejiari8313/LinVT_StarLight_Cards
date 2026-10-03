import argparse
import subprocess
import sys
import time
from pathlib import Path

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

class ChangeHandler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script
        self.process = None
        self.restart_script()

    def restart_script(self):
        if self.process:
            self.process.terminate()
            self.process.wait()
        self.process = subprocess.Popen([sys.executable, str(self.script)])

    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            print(f'{event.src_path} has been modified, restarting script...')
            self.restart_script()

def main():
    parser = argparse.ArgumentParser(description="Reinicia el juego cuando cambia el código.")
    parser.add_argument(
        "--script",
        type=Path,
        default=Path(__file__).with_name("main.py"),
        help="Script que se debe reiniciar (por defecto: src/main.py).",
    )
    args = parser.parse_args()

    source_dir = args.script.resolve().parent
    event_handler = ChangeHandler(args.script.resolve())
    observer = Observer()
    observer.schedule(event_handler, path=str(source_dir), recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        if event_handler.process:
            event_handler.process.terminate()
    observer.join()


if __name__ == "__main__":
    main()