import subprocess
import atexit
import config

class DetectionManager:
    def __init__(self):
        self.detection_process = subprocess.Popen(['python', config.SCRIPT_PATH], stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=config.ENV)
        atexit.register(self.detection_process.kill)

    def single_pre(self, image_path):
        self._execute_detection("-p1", image_path)

    def batch_pre(self, directory_path):
        self._execute_detection("-d", directory_path)

    def _execute_detection(self, mode_flag, path):
        if path:
            detect_output = f"{mode_flag} {path}\n"
            self.detection_process.stdin.write(detect_output.encode("utf-8"))
            self.detection_process.stdin.flush()

    # Additional methods for handling detection results, configurations, etc.
