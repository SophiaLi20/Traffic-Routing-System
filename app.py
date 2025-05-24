from flask import Flask, request, jsonify
from router_system import TrafficRouterSystem

app = Flask(__name__)
system = TrafficRouterSystem()
system.load_map_data()

@app.route("/")
def index():
    return "Traffic Routing System API"

@app.route("/shortest-path", methods=["GET"])
def shortest_path():
    source = request.args.get("source", type=int)
    if source is None:
        return jsonify({"error": "Missing 'source' query parameter"}), 400

    distances = system.find_shortest_paths(source)
    return jsonify(distances)

if __name__ == "__main__":
    app.run(debug=True)
