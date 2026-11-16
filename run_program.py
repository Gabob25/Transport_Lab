from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import webbrowser


LAB_DIRECTORY = Path(__file__).resolve().parent
HTML_DIRECTORY = LAB_DIRECTORY / "HTML File"
REFERENCE_VIDEO = LAB_DIRECTORY / "Videos" / "stokes_reference.mp4"


class LabRequestHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path: str) -> str:
        translated_path = Path(super().translate_path(path))
        if translated_path == HTML_DIRECTORY / REFERENCE_VIDEO.name:
            return str(REFERENCE_VIDEO)
        return str(translated_path)


def main() -> None:
    index_file = HTML_DIRECTORY / "index.html"
    if not index_file.is_file():
        raise FileNotFoundError(f"Could not find the app: {index_file}")
    if not REFERENCE_VIDEO.is_file():
        raise FileNotFoundError(f"Could not find the Stokes reference video: {REFERENCE_VIDEO}")

    handler = partial(LabRequestHandler, directory=str(HTML_DIRECTORY))
    with ThreadingHTTPServer(("127.0.0.1", 0), handler) as server:
        url = f"http://127.0.0.1:{server.server_address[1]}/index.html"
        print(f"Opening Bubble Motion at {url}")
        print("Press Ctrl+C to stop the local server.")
        webbrowser.open(url)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nLocal server stopped.")


if __name__ == "__main__":
    main()
