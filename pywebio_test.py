from dijkstras import dijkstra
import networkx as nx
import json
from pywebio import start_server, config
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *

# load metro #
graph = nx.read_graphml("tokyometro.graphml")

# implement all translation maps
file_path = "secondary.json"
with open(file_path, "r") as file:
    secondary = json.load(file)
tertiary = dict((v, k) for k, v in secondary.items())
letter_to_line = {
    "A": "Rose",
    "I": "Blue",
    "S": "Leaf",
    "E": "Magenta",
    "G": "Orange",
    "M": "Red",
    "H": "Silver",
    "T": "Sky",
    "C": "Green",
    "Y": "Gold",
    "Z": "Purple",
    "N": "Emerald",
    "F": "Brown",
}


def get_route(start, end) -> str:
    # get route #
    dji = dijkstra(graph, tertiary[start], tertiary[end])

    # get output path #
    output = ""
    for i in range(len(dji[1]) - 1):
        if i == 0:
            output += "Board at " + secondary[dji[1][i]] + " Station. "
        if i == len(dji[1]) - 2:
            output += (
                "Ride on the "
                + letter_to_line[dji[1][i][0]]
                + " line until "
                + secondary[dji[1][i + 1]]
                + " Station. "
            )
        if dji[1][i + 1][0] == dji[1][i][0]:
            continue
        output += (
            "Ride on the "
            + letter_to_line[dji[1][i][0]]
            + " line until "
            + secondary[dji[1][i]]
            + " Station. "
        )
    output += "Total distance traveled: " + str(dji[0]) + " km."

    return output


def go_home():
    clear()
    web_func()


@config(theme="dark")
def web_func():
    # start = input("Input your start station：")
    # end = input("Input your end station：")
    start = select("Departure: ", tertiary.keys())
    end = select("Destination: ", tertiary.keys())

    ROUTE = get_route(start, end)

    put_text(ROUTE)

    put_button(["Find a New Route"], onclick=lambda: go_home())


if __name__ == "__main__":
    start_server(web_func, port=8080, debug=True)
