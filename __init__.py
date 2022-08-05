import requests
import base64

class Craiyon:

    def generate(prompt: str,image: int, out_path: str):
        try:
            req = requests.post('https://backend.craiyon.com/generate', json={"prompt": str(prompt)})
            with open(f"{out_path}", "wb") as fh:
                fh.write(base64.b64decode(req.json()['images'][image]))
                fh.close()
            return f"Success, your image has been saved at {out_path}"
        except:
            return f"Error while drawing image to {out_path}"
