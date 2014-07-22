import flask


app = flask.Flask(__name__)


@app.route("/")
def main():
    content = flask.request.args.get('content', '')
    mimetype = flask.request.args.get('mimetype', 'application/octet-stream')
    filename = flask.request.args.get('filename', 'file')
    content_disposition = 'attachment; filename="{}"'.format(filename)

    response = flask.Response(
        content,
        mimetype=mimetype
    )
    response.headers.add('Content-Disposition', content_disposition)
    return response
