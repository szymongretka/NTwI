### Setup

To use core_nlp_parser module you need to download models from https://stanfordnlp.github.io/CoreNLP/ and run the server with command:

    java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000

Parser by default uses localhost and port 9000. To tweak this settings set up a config.local.ini file with content:

    [corenlp]
    url=<YOUR_URL>


##### *nix
    python3 -m venv ./venv
    source ./venv/bin/activate
    pip install -r requirements.txt

    python3 install.py
    
### Usage
##### Windows
    Get-Content .\text_to_summarize.txt | py.exe 

##### *nix
    cat ./text_to_summarize.txt | python3 main.py
