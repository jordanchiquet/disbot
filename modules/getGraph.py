import matplotlib.pyplot as plt 

def getGraph(xArray: list, yArray: list, type: str):
    if type == "bar":
        plt.bar(xArray, yArray)
    plt.show()






x = ['thatbadrussian', 'slomojoe', 'Tlacotl', 'TGRAS', 'IMC', 'Jordan', 'Ganjalf', 'Valrite', 'Set', 'The Cuckinator', 'Thotiana', 'hackablebot', 'deezhugz']
y = [1, 43, 9, 1, 10, 69, 237, 10, 271, 188, 4, 9, 2]

getGraph(x, y, "bar")