import pandas as pd
from datetime import datetime
import yaml

# Load config
with open("config/settings.yaml", "r") as f:
    config = yaml.safe_load(f)

def log_application(company, role, status):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df = pd.DataFrame([[company, role, status, date]], columns=config["fields"])
    df.to_csv(config["output_file"], mode='a', index=False, header=not pd.io.common.file_exists(config["output_file"]))
