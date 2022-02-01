# annotations_path is the path to vizwiz/annotations folder.
from typing import Dict, List
from paths import annotations_path
from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import json, string

splits = {'train', 'val'}


def preprocessing(s: string) -> List:
    # remove stopwords and punctuation.
    stop = set(stopwords.words('english') + list(string.punctuation))
    return [i for i in word_tokenize(s.lower()) if i not in stop]


def collect_words(split: string) -> Dict:
    # Collects all 'useful' tokens (non-stopwords) from the captions of each image.
    # Returns a dict with image ids and the corresponding tokens
    img_tokens = dict()
    
    with open(f'{annotations_path}{split}.json') as json_file:
        data = json.load(json_file)
    
    annotations = data['annotations']
    
    for item in annotations:
        imgid = item['image_id']
        if imgid not in img_tokens:
            img_tokens[imgid] = set()
        useful_tokens = preprocessing(item['caption'])
        for token in useful_tokens:
            img_tokens[imgid].add(token)
    
    return img_tokens


def anotherfunction(tokens: dict) -> Counter:
    c = Counter()
    for subset in tokens.values():
        for token in subset:
            c[token] += 1
    return c


if __name__ == "__main__":
    var = collect_words('val')
    count = anotherfunction(var)
    print(count)
