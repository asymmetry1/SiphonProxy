# SiphonProxy

Utility script designed to intercept and extract hidden character definitions from AI roleplay platforms (such as Janitor AI) that support custom OpenAI-compatible proxies.

By running a local Flask server equipped with CORS compliance and an automated `pyngrok` tunnel, it mimics an OpenAI completion endpoint, captures the incoming configuration payload and logs the character's definition.

Built for gooners by gooners.

---

## Quickstart

Prerequisite:
- Python 3
- pip
- [ngrok auth token](https://ngrok.com)

```bash
git clone https://github.com/asymmetry1/SiphonProxy.git
cd SiphonProxy
pip install -r requirements.txt
```

Run:

```
python app.py
```

Use the `/v1/chat/completions` url for the proxy url.

Example:

```
Name: Proxy
Model: gpt-4
Proxy Url: link.ngrok-free.app/v1/chat/completions
API Key: sk-dummy
```

## Debug

If showing network error, try refreshing the page.
