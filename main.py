from flask import Flask
from flask import url_for, request, redirect, abort
from flask import render_template, request, Response, Blueprint
from markupsafe import escape
from pytube import YouTube
from pytube import Search
from io import BytesIO
from pytube.innertube import _default_clients
from pytube.exceptions import AgeRestrictedError, LiveStreamError

_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]

app = Flask(__name__)

def filter_streams(results):
    page_results=[]
    for result in results:
        try:
            if result.streams:
                if result not in page_results:
                    page_results.append(result)
        except AgeRestrictedError:
            pass
        except LiveStreamError:
            pass
    return page_results

def get_stream(id, itag):
    url = f"https://youtube.com/watch?v={id}"
    data = YouTube(url)
    stream = data.streams.get_by_itag(itag)
    symbols=["!","@","#","$","%","&","*","=","|","{","}",":","'",'"',"\\","/","?","<",">"]
    filename=data.title
    for symbol in symbols:
        filename=filename.replace(symbol,"")
    filename=filename.replace(" ","_")
    filename=filename+f'.{stream.mime_type.split("/")[1]}'
    buffer = BytesIO()
    stream.stream_to_buffer(buffer)
    buffer.seek(0)
    def generate():
        chunk = buffer.read(1024)
        while chunk:
            yield chunk
            chunk = buffer.read(1024)
    return Response(generate(), mimetype=stream.mime_type, headers={'Content-Disposition': f'attachment; filename="{filename}"'})

@app.route('/')
@app.route('/index.html')
def home():
    return render_template("index.html")

@app.route('/search.html', methods=["GET","POST"])
def search():
    if request.method == "POST":
        query_string = escape(request.form['query'])
        search = Search(query_string)
        page_results = filter_streams(results=search.results)
        return render_template("search.html",query=query_string, results=page_results)
    else:
        return render_template("search.html")

@app.route('/download', methods=["GET","POST"])
def download():
    id = request.args.get('id')
    itag = request.args.get('itag')
    data_stream = get_stream(id, itag)
    return data_stream