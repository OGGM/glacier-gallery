from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the .ipynb directory with bokeh server"""
    Popen(["panel", "serve", "explorer.ipynb", "--allow-websocket-origin=*"])

