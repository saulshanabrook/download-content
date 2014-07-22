import flask
import markdown2

app = flask.Flask(__name__)


@app.route("/")
def main():
    content = flask.request.args.get('content', '')
    if not content:
        return markdown2.markdown(open("README.md").read(), extras=["fenced-code-blocks"]) + open('fork_me_on_github.html').read()
    mimetype = flask.request.args.get('mimetype', 'application/octet-stream')
    filename = flask.request.args.get('filename', 'file')
    content_disposition = 'attachment; filename="{}"'.format(filename)

    response = flask.Response(
        content,
        mimetype=mimetype
    )
    response.headers.add('Content-Disposition', content_disposition)
    return response
