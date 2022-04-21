import numpy as np
import matplotlib.pyplot as plt

plt.ion()
fig, (ax1, ax2) = plt.subplots(2)

def simuation(x_act, p, N):
    v_k = np.random.choice([1, -1], p=[p, 1 - p])
    x_act = (x_act + v_k) % N
    return x_act


def discrete_filter(bel, p, N):
    bel_prime = np.zeros_like(bel)
    for x in range(bel.shape[0]):
        bel_prime[x] = p * bel[x - 1] + (1 - p) * bel[(x + 1) % N]
    return bel_prime


def plot_historgram(x_act, bel):
    ax1.cla()
    ax1.scatter(x_act,0)
    ax1.axis([0, bel.shape[0] - 1, -1, 1])
    ax1.set_ylabel('Actual Position')
    ax2.cla()
    ax2.bar(range(0, bel.shape[0]), bel, width=1.0)
    y_min = np.minimum(np.amax(bel) * 1.2, 1)
    ax2.axis([0, bel.shape[0] - 1, 0, y_min])
    ax2.set_ylabel('Estimated Position')

    plt.draw()
    plt.pause(0.000001)

def z_k(x, L, N):
    theta = np.pi * 2 * x / N
    return np.sqrt((L - np.cos(theta)) ** 2 + np.sin(theta) ** 2)

def resample(bel, L, e, N, x):
    z = z_k(x, L, N)
    for count in range(bel.shape[0]):
        if not z - e < z_k(count, L, N) < z + e:
            bel[count] = 0
        else:
            bel[count] = bel[count] / (2*e)

    bel_sum = sum(bel)

    return np.true_divide(bel, bel_sum)
    #return bel

def main():
    #initial position
    N = 100
    x_act = int(N / 4)
    e = 0.5
    L = 2
    p = 0.55

    e_pri = 0.45
    p_pri = 0.55

    bel = np.array(N * [1/N])
    #bel = np.zeros(N)
    #bel[N//4] = 1

    plt.ion()
    plt.show()

    for i in range(0, 500):
        x_act = simuation(x_act, p, N)
        bel = discrete_filter(bel, p_pri, N)
        bel = resample(bel, L, e_pri, N, x_act)
        plot_historgram(x_act, bel)
        print(np.sum(bel))


    plt.ioff()
    plt.show()


if __name__ == "__main__":
    main()
