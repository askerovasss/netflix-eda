import pandas as pd
import matplotlib.pyplot as plt

def load_df(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def bar_top(df, col, n=10, title=None, ax=None):
    ax = ax or plt.gca()
    cnt = df[col].value_counts().head(n)
    cnt.plot(kind="bar", ax=ax)
    ax.set_title(title or f"Top {n} of {col}")
    ax.set_ylabel("count")
    plt.tight_layout()
