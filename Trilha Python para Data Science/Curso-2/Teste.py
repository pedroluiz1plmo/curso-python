import matplotlib.pyplot as plt

# 1. Create the data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 2. Create the plot
plt.plot(x, y, label='Growth Trace')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('VS Code Test Plot')
plt.legend()

# 3. Force the window to stay open
print("Plotting... Please check your taskbar for a new window.")
plt.show(block=True) 

# 4. Optional: Add an input so the terminal doesn't close instantly
input("Press Enter to close the script...")