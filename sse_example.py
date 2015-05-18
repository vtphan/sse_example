from flask import Flask, Response
from flask import render_template
from time import gmtime, strftime, sleep

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/server_time')
def server_time():
   def event_stream():
      while True:
         yield 'event: mesg\ndata: {0}\n\n'.format(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
         sleep(3)

   return Response(event_stream(), mimetype="text/event-stream")


if __name__ == '__main__':
   app.run()