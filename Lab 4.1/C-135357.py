import numpy as np

x = np.random.randint(20, size=(200))
y = np.random.randint(20, size=(200))


m = 0
c = 0

LR = 0.1
itts = 20

MSE = []
SLOPE = []
INTERCEPT = []

for i in range(itts):
    y_pred = m * x + c
    MSE.append(np.mean((y_pred - y) ** 2))

    dcost_dm = np.mean(2 * (y_pred - y) * x)
    dcost_dc = np.mean(2 * (y_pred - y) * x)

    m -= LR * dcost_dm
    SLOPE.append(m)

    c -= LR * dcost_dm
    INTERCEPT.append(c)

sorted_intercept = sorted(INTERCEPT)
index = INTERCEPT.index(sorted_intercept[0])

print(
    f"Slope: {round(SLOPE[index],4)} Bias: { round(INTERCEPT[index],4)} \
      MSE/Cost: {round(MSE[index],4)}"
)
