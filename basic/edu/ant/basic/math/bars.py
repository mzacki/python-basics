from matplotlib import pyplot as plt
from fractions import Fraction


# prints bars to png file in same directory
# from Linux Magazine 210

def fill_tub(per_min, local_xmax):
    local_lx = list(range(1, local_xmax + 1))
    local_ly = [0] * local_xmax
    local_sum = 0
    for i in range(local_xmax):
        local_sum += per_min
        if local_sum > 1:
            break
        local_ly[i] = local_sum

    return local_lx, local_ly


xmax = 15

plt.style.use('ggplot')
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))
fig.suptitle("Filling a bath tub")

lx, ly = fill_tub(Fraction(1, 15), xmax)
ax[0].bar(lx, ly, color='tab:red')
ax[0].set_xlabel("Minutes")
ax[0].set_ylabel("Fill Level")
ax[0].set_title("15min faucet")

lx, ly = fill_tub(Fraction(1, 10), xmax)
ax[1].bar(lx, ly, color='tab:orange')
ax[1].set_xlabel("Minutes")
ax[1].set_ylabel("Fill Level")
ax[1].set_title("10min faucet")

lx, ly = fill_tub(Fraction(1, 10) + Fraction(1 / 15), xmax)
ax[2].bar(lx, ly, color='tab:green')
ax[2].set_xlabel("Minutes")
ax[2].set_ylabel("Fill Level")
ax[2].set_title("Both 15min and 10min faucet")

plt.savefig("bars.png")
