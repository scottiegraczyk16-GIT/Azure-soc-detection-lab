app = Flask(__name__)

log_file = "/home/azureuser/system_events.log"

events = [
    "INFO nginx service restarted",
    "WARNING CPU usage exceeded 85%",
    "ERROR database connection failed",
    "INFO user updated profile",
    "WARNING disk usage exceeded 90%",
    "ALERT suspicious IP detected",
    "ERROR API returned HTTP 500",
    "INFO backup completed successfully",
    "ALERT multiple failed login attempts",
    "WARNING memory usage high"
]

@app.route("/event")
def generate_event():
    event = random.choice(events)

    timestamp = datetime.datetime.now()

    log_entry = f"{timestamp} {event}\n"

    with open(log_file, "a") as f:
        f.write(log_entry)

    return f"<h2>Generated Event:</h2><p>{event}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
