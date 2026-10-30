import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import plotly.graph_objects as go
x = np.linspace(0, 10, 200); y = np.sin(x) * np.exp(-x / 3)
plt.plot(x, y, label=r"$\sin(x)e^{-x/3}$"); plt.xlabel("x"); plt.legend()
plt.savefig("docs/img/fig_static.png", dpi=150)
fig = go.Figure(go.Scatter(x=x, y=y, mode="lines+markers", name="signal"))
fig.write_html("docs/include/fig_plotly.html", full_html=False, include_plotlyjs=True)
