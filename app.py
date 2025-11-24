from email.mime import message
from flask import Flask, render_template, request, redirect
from db import get_db

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")



# VIEW EVENTS
@app.route("/events")
def events():
    db = get_db()
    cur = db.cursor(dictionary=True)
    cur.execute("SELECT * FROM Event ORDER BY start_time ASC")
    events = cur.fetchall()
    return render_template("events.html", events=events)

# ADD EVENT

@app.route("/add_event", methods=["GET", "POST"])
def add_event():
    if request.method == "POST":
        title = request.form["title"]
        start = request.form["start_time"]
        end = request.form["end_time"]
        desc = request.form["description"]

        db = get_db()
        cur = db.cursor()
        cur.execute("""
            INSERT INTO Event (title, start_time, end_time, description)
            VALUES (%s, %s, %s, %s)
        """, (title, start, end, desc))
        db.commit()

        return redirect("/events")

    return render_template("add_event.html")



# UPDATE EVENT

@app.route("/update_event/<int:event_id>", methods=["GET", "POST"])
def update_event(event_id):
    db = get_db()
    cur = db.cursor(dictionary=True)

    if request.method == "POST":
        title = request.form["title"]
        start = request.form["start_time"]
        end = request.form["end_time"]
        desc = request.form["description"]

        cur.execute("""
            UPDATE Event SET title=%s, start_time=%s, end_time=%s, description=%s
            WHERE event_id=%s
        """, (title, start, end, desc, event_id))
        db.commit()

        return redirect("/events")

    cur.execute("SELECT * FROM Event WHERE event_id=%s", (event_id,))
    event = cur.fetchone()

    return render_template("update_event.html", event=event)



# DELETE EVENT

@app.route("/delete_event/<int:event_id>")
def delete_event(event_id):
    db = get_db()
    cur = db.cursor()

    cur.execute("DELETE FROM EventResourceAllocation WHERE event_id=%s", (event_id,))
    cur.execute("DELETE FROM Event WHERE event_id=%s", (event_id,))
    db.commit()

    return redirect("/events")

# VIEW RESOURCES

@app.route("/resources")
def resources():
    db = get_db()
    cur = db.cursor(dictionary=True)
    cur.execute("SELECT * FROM Resource")
    resources = cur.fetchall()
    return render_template("resources.html", resources=resources)
# ADD RESOURCE

@app.route("/add_resource", methods=["GET", "POST"])
def add_resource():
    if request.method == "POST":
        name = request.form["name"]
        rtype = request.form["type"]

        db = get_db()
        cur = db.cursor()
        cur.execute("""
            INSERT INTO Resource (resource_name, resource_type)
            VALUES (%s, %s)
        """, (name, rtype))
        db.commit()

        return redirect("/resources")

    return render_template("add_resource.html")

# UPDATE RESOURCE

@app.route("/update_resource/<int:resource_id>", methods=["GET", "POST"])
def update_resource(resource_id):
    db = get_db()
    cur = db.cursor(dictionary=True)

    if request.method == "POST":
        name = request.form["name"]
        rtype = request.form["type"]

        cur.execute("""
            UPDATE Resource SET resource_name=%s, resource_type=%s
            WHERE resource_id=%s
        """, (name, rtype, resource_id))
        db.commit()

        return redirect("/resources")

    cur.execute("SELECT * FROM Resource WHERE resource_id=%s", (resource_id,))
    resource = cur.fetchone()

    return render_template("update_resource.html", resource=resource)


# DELETE RESOURCE

@app.route("/delete_resource/<int:resource_id>")
def delete_resource(resource_id):
    db = get_db()
    cur = db.cursor()

    cur.execute("DELETE FROM EventResourceAllocation WHERE resource_id=%s", (resource_id,))
    cur.execute("DELETE FROM Resource WHERE resource_id=%s", (resource_id,))
    db.commit()

    return redirect("/resources")



@app.route("/allocate", methods=["GET", "POST"])
def allocate():
    db = get_db()
    cur = db.cursor(dictionary=True)

    
    cur.execute("SELECT * FROM Event")
    events = cur.fetchall()

    cur.execute("SELECT * FROM Resource")
    resources = cur.fetchall()

    if request.method == "POST":
        event_id = request.form["event_id"]
        resource_id = request.form["resource_id"]

        cur.execute("SELECT start_time, end_time FROM Event WHERE event_id = %s", (event_id,))
        event_time = cur.fetchone()
        start_time = event_time["start_time"]
        end_time = event_time["end_time"]

       
        cur.execute("""
            SELECT * FROM EventResourceAllocation AS A
            JOIN Event AS E ON A.event_id = E.event_id
            WHERE A.resource_id = %s
            AND (
                (E.start_time <= %s AND E.end_time >= %s)
                OR (E.start_time <= %s AND E.end_time >= %s)
                OR (%s <= E.start_time AND %s >= E.end_time)
            )
        """, (resource_id, start_time, start_time, end_time, end_time, start_time, end_time))

        conflict = cur.fetchone()

        if conflict:
            message = "⚠ This resource is already allocated for this time slot!"
            return render_template("allocate.html", events=events, resources=resources, message=message)
        

       
        cur.execute("""
            INSERT INTO EventResourceAllocation (event_id, resource_id)
            VALUES (%s, %s)
        """, (event_id, resource_id))
        db.commit()

        return redirect("/allocate")

   
    cur.execute("""
        SELECT 
            e.event_id,
            e.title,
            e.start_time,
            e.end_time,
            r.resource_name,
            r.resource_type
        FROM EventResourceAllocation a
        JOIN Event e ON a.event_id = e.event_id
        JOIN Resource r ON a.resource_id = r.resource_id
        ORDER BY e.start_time ASC
    """)
    reports = cur.fetchall()

    return render_template("allocate.html", events=events, resources=resources, reports=reports)


@app.route("/resource_report", methods=["GET", "POST"])
def resource_report():
    db = get_db()
    cur = db.cursor(dictionary=True)

    utilisation = []
    bookings = []

    if request.method == "POST":
        start = request.form["start"]
        end = request.form["end"]

        # 1. Total Hours 
        cur.execute("""
            SELECT
                r.resource_id,
                r.resource_name,
                SUM(
                    TIMESTAMPDIFF(
                        HOUR,
                        GREATEST(e.start_time, %s),
                        LEAST(e.end_time, %s)
                    )
                ) AS total_hours
            FROM EventResourceAllocation a
            JOIN Event e ON a.event_id = e.event_id
            JOIN Resource r ON a.resource_id = r.resource_id
            WHERE e.start_time <= %s AND e.end_time >= %s
            GROUP BY r.resource_id, r.resource_name
            ORDER BY total_hours DESC;
        """, (start, end, end, start))
        utilisation = cur.fetchall()

        # 2. Bookings Inside The Date Range
        cur.execute("""
            SELECT 
                r.resource_name,
                e.title,
                e.start_time,
                e.end_time
            FROM EventResourceAllocation a
            JOIN Event e ON a.event_id = e.event_id
            JOIN Resource r ON a.resource_id = r.resource_id
            WHERE e.start_time >= %s AND e.end_time <= %s
            ORDER BY e.start_time ASC;
        """, (start, end))
        bookings = cur.fetchall()

    # ALWAYS RETURN SOMETHING
    return render_template(
        "resource_report.html",
        utilisation=utilisation,
        bookings=bookings
    )



        
if __name__ == "__main__":
    app.run(debug=True)





app.run(debug=True)
