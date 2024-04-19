

from networkState import SingleRouterNetworkState, Flow
import matplotlib.pyplot as plt

def main():
    router = SingleRouterNetworkState()
    # print(dir(router))
    gens = 5000
    for i in range(30):
        newFlow = Flow()
        router.addFlow(newFlow)

    for i in range(gens):
        router.evolve(i)

    plt.plot(router.q_history)
    averageWindow = router.flows[0].W
    for f in router.flows:
        hist = f.W
        for j in range(len(hist)):
            averageWindow[j] += f.W[j]

    for i in range(len(averageWindow)):
        averageWindow[i] = averageWindow[i] / len(router.flows)
    plt.plot(averageWindow)
    plt.plot(router.x_hist)
    plt.title("Queue size, predicted size, and window size")
    plt.xlabel("Time")
    plt.ylabel("Packets")
    plt.show()
    

    plt.plot(router.q_history, averageWindow)
    plt.title("Queue size versus window size")
    plt.xlabel("Queue size")
    plt.ylabel("Window Size")
    plt.show()

main()

