from flask import Flask, jsonify, request, send_file
import weasyprint
import io

app = Flask(__name__)

@app.route('/convert', methods=['GET'])
def convert():
    try:
        args = request.args
        url = str(args.get("url"))
        pdf = weasyprint.HTML(url).write_pdf()
        return send_file(io.BytesIO(pdf), download_name="result.pdf")
    except:
        return jsonify({"success" : False})

app.run(host='0.0.0.0', port=8080, debug=True)
