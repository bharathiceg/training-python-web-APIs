from flask import Flask

app = Flask(__name__)

print("✅ Flask created:", app)
print("📋 Has before_first_request:", hasattr(app, "before_first_request"))
print("📋 Has before_request:", hasattr(app, "before_request"))
    