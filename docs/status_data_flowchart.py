# Copyright (C) 2022 Chatpon Chaimongkol <chatponc65@nu.ac.th>

"""



"""

__author__ = "Chatpon Chaimongkol"

# installed Libraries
import schemdraw
from schemdraw import flow

with schemdraw.Drawing() as d:
    d += flow.Start(w=6).label("Data send form HIVEMQ")  # d += 1 -> d=d+1
    d += flow.Arrow().down(d.unit / 2)
    d += flow.Data(w=6).label("receive into the on_message\n"
                              "in comm_mqtt.MQTTConn")
    d += flow.Arrow().down(d.unit / 2)
    d += flow.Data(w=6).label("process input message\n"
                              "into a sensor status state")
    d += flow.Arrow().down(d.unit / 2)
    d += flow.Data(w=7).label("send sensor status to\n"
                              "main_gui2.SensorUI.change_status")
    d += flow.Arrow().down(d.unit / 2)
    # d += (d1 := flow.Decision(w=5, h=5, E="No").label(
    #     "is the name from\nthe data found that in\nthe NAMES list "))
    d1 = d.add(flow.Decision(w=5, h=5, E="No").label(
         "is the name from\nthe data found that in\nthe NAMES list "))
    d += flow.Arrow().right(d.unit/2).at(d1.E)
    d += flow.Terminal(w=5, label= "Exit with no change").anchor('W')
    d += flow.Arrow().down(d.unit / 2).at(d1.S)
    d += flow.Process(w=10).label(
        "call main_gui2.StatusButton.Toggle_color\n"
        "and set the prepare color the indicator ")


