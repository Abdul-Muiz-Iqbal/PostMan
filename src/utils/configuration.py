from dataclasses import dataclass
from typing import Optional

@dataclass
class Configuration:
    drive_path: Optional[str]
    local_save_location: Optional[str]
    store_msgs: bool = False

    def save(self):
        with open("Config", "w") as f:
            f.writelines([self.drive_path, self.local_save_location, self.store_msgs])