### Setup

##### *nix
    python3 -m venv ./venv
    source ./venv/bin/activate
    pip install -r requirements.txt

    python3 install.py
    
### Usage
##### Windows
    Get-Content .\text_to_summarize.txt | py.exe main.py

##### *nix
    cat ./text_to_summarize.txt | python3 main.py
