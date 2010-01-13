import plot, xml.dom.minidom

def get_statusimage(db):
    plot_list = get_plot_list(db, xml_to_mapping())
    resources = {
        "background": "dikulan/resources/background.png",
        "reserved": "dikulan/resources/reserved.png",
        "free": "dikulan/resources/free.png"
    }
    plotter = plot.Plot(plot_list, "background", resources)
    return plotter.get_image()

def xml_to_mapping():
    doc = xml.dom.minidom.parse("dikulan/resources/coordinates.xml")
    out = dict()
    for seat in doc.getElementsByTagName("seat"):
        seat_id = seat.getAttribute("id")
        x = int(seat.getAttribute("x"))
        y = int(seat.getAttribute("y"))
        out[seat_id] = x,y
    return out
    
def get_plot_list(db, mapping):
    plot_list = list()
    mapping = mapping.copy()
    
    # Cross-reference with reserved seats
    reserved_seats = get_reserved_seats(db)
    for seat_id in reserved_seats:
        seat = mapping.pop(str(seat_id[0]))
        seat = seat, "reserved"
        plot_list.append(seat)
    
    # The rest of the seats are free
    for seat_id in mapping:
        seat = mapping[seat_id], "free"
        plot_list.append(seat)
    
    return plot_list
    
    

def get_reserved_seats(db):
    cursor = db.cursor()
    cursor.execute("select id from reserved_seats")
    return cursor


