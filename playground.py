

if __name__ == "__main__":
    from core.parser.core_nlp_parser import *
    result = parse(
        "The park is so wonderful when the sun is setting and a cool breeze is blowing")
    from nltk.tree import Tree

    print(Tree.fromstring(str(result)))
    print(result)
