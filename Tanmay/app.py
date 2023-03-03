import psutil
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def memory_status():
    mem = psutil.virtual_memory()
    mem_utilization = mem.used / mem.total * 100
    result = {
        
        'total_memory': mem.total / (1024 ** 3),
        'used_memory': mem.used / (1024 ** 3),
        'free_memory': mem.available / (1024 ** 3),
        'memory_utilization': mem_utilization,
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)