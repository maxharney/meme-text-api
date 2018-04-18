#!/usr/bin/python

import sys
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/generate', methods=['GET', 'POST'])
def test():
    text = toMeme(request.values['text'])

    return jsonify(
            text=text
        )

def toMeme(text):
    halfWidth = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()*+,-./:;<=>?@[\]^_`{|}~ '
    fullWidth = '０１２３４５６７８９ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ！゛＃＄％＆（）＊＋、ー。／：；〈＝〉？＠［\］＾＿‘｛｜｝～　'
    translationTable = str.maketrans(halfWidth, fullWidth)
    return text.translate(translationTable)

if __name__ == '__main__':
    app.run(debug=True, port=5000)