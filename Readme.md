# Traffic Routing System (Dijkstra + Flask)

Hey there! 👋  
This is a simple Python project I built to simulate a traffic routing system. Think of it like Google Maps, but super stripped down and totally offline. It uses Dijkstra’s Algorithm under the hood to find the shortest path between locations (nodes), and it’s powered by Flask so you can interact with it through a neat little API.

---

## What This Does

- Lets you load a road network (as a graph)
- Uses Dijkstra’s Algorithm to figure out the shortest route from a given starting point
- Exposes an endpoint so you can test it through your browser or Postman
- Code is modular—easy to read and tweak

I built this mainly to brush up on graphs, algorithms, and for experiencing working with Flask.

---

 📁 Project Structure

- `app.py` – Where the Flask API lives  
- `graph.py` – Just some graph classes  
- `dijkstra.py` – Actual Dijkstra logic (with a Min Heap)  
- `router_system.py` – Core system that connects it all  
- `data.json` – The map (graph) data  
- `venv/` – Python virtual environment (optional)  
- `README.md` – You’re reading it!


---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/traffic-routing-system.git
cd traffic-routing-system
```

### 2. Set Up a Virtual Environment (Optional but Recommended)
```bash
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install Dependencies
```
pip install flask
```
### 4. Run
```
python app.py

# The server will start at
http://127.0.0.1:5000/
```
## API Endpoint
GET /shortest-path?source=<source_id>
Description: Returns the shortest distances from the source node to all other nodes.
```
Example
curl "http://127.0.0.1:5000/shortest-path?source=1"
```
Response
{
  "1": 0,
  "2": 3,
  "3": 7,
  "4": 5
}

## Dependencies
- Python 3.7+
- Flask

## Algorithm Used
The system uses Dijkstra’s Algorithm for shortest path finding. The algorithm implementation uses a Min-Heap (PriorityQueue) for performance optimization on large graphs.

## Future Improvements

- Add real-time traffic data integration
- Visual frontend using React/Map APIs
- User-based route preferences (fastest, shortest, eco-friendly)
