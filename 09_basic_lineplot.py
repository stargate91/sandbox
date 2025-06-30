import matplotlib.pyplot as plt

x = ["2025-01", "2025-02", "2025-03", "2025-04", "2025-05", "2025-06"]
y = [5, 10, 7, 6, 1, 3]

plt.plot(x,y)
plt.title("Monthly sales on Fiverr in 2025")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(False)
plt.savefig("09_basic_lineplot.png")
plt.show()