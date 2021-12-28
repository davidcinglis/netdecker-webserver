from flask import Flask, request, render_template, jsonify
from netdecker import decklist, ocr
import netdecker.cardfile_data.formats as formats

app = Flask(__name__)

@app.route('/')
def home_route():
    return render_template('home.html', formats=formats.supported_formats)

@app.route('/decklist/', methods=['GET'])
def decklist_route():
    decklist_uri = request.args.get('url')
    decklist_format = request.args.get('format')
    print("decklist url is %s and format is %s" % (decklist_uri, decklist_format))
    decklist_text = decklist.generate_decklist(decklist_uri, ocr.GoogleOCR(), decklist_format)
    return jsonify(decklist=decklist_text), 200
        

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')