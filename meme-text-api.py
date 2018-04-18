#!/usr/bin/python

import sys
from flask import Flask, request

app = Flask(__name__)

@app.route('/generate', methods=['GET', 'POST'])
def test():
    return toMeme(request.values['text'])

def toMeme(text):
    halfWidth = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'
    fullWidth = '０１２３４５６７８９ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ！゛＃＄％＆（）＊＋、ー。／：；〈＝〉？＠［\］＾＿‘｛｜｝～'
    translationTable = str.maketrans(halfWidth, fullWidth)
    return text.translate(translationTable)

if __name__ == '__main__':
    app.run(debug=True, port=5000)