from flask import Flask, request, render_template, jsonify, abort
from netdecker import decklist_parser, ocr
import netdecker.cardfile_data.formats as formats
from werkzeug import exceptions

app = Flask(__name__)

@app.errorhandler(400)
def handle_bad_request(e):
    return jsonify(error = str(e)), 400

@app.route('/')
def home_route():
    return render_template('index.html', formats=formats.supported_formats)

@app.route('/decklist/', methods=['GET'])
def decklist_route():
    decklist_uri = request.args.get('url')
    decklist_format = request.args.get('format')
    decklist_response = decklist_parser.generate_decklist(decklist_uri, ocr.GoogleOCR(), decklist_format)
    if not decklist_response.success:
        abort(400, description = "Invalid URL.")
    
    return jsonify(decklist=decklist_response.decklist.serialize()), 200
