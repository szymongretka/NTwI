from nltk.parse.corenlp import CoreNLPServer, CoreNLPParser
import configparser
import os


def _read_core_nlp_config():
    config = configparser.ConfigParser()
    config.read('config.local.ini')
    default_url = 'http://localhost:9000'

    if 'corenlp' not in config:
        return {
            'url': default_url,
        }

    section = config['corenlp']

    return {
        'url': section.get('url', default_url),
    }


_open_nlp_config = _read_core_nlp_config()


def parse(sentence: str):
    parser = CoreNLPParser(_open_nlp_config['url'])
    return next(parser.parse_text(sentence))
