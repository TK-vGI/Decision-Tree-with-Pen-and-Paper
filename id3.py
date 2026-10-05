import pandas as pd
import numpy as np


def entropy(y):
    probs = y.value_counts(normalize=True)

    return -1*np.sum(probs * np.log2(probs))


def conditional_entropy(df, feature, target):
    total = len(df)
    cond_entropy = 0

    for value in df[feature].unique():
        subset = df[df[feature] == value]

        weight = len(subset) / total

        cond_entropy += weight * entropy(subset[target])

    return cond_entropy


def information_gain(df, feature, target):
    return entropy(df[target]) - conditional_entropy(df, feature, target)


df = pd.DataFrame({
    "bright_colors": [0, 1, 0, 0, 1, 0, 0, 1, 1, 1],
    "spotted": [0, 0, 1, 1, 0, 1, 0, 1, 1, 1],
    "hooded_head": [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    "venomous": [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
})

target_entropy = entropy(df["venomous"])
print(f"Target entropy: {target_entropy:.3f}")

df.head()

target = "venomous"

features = [
    "bright_colors",
    "spotted",
    "hooded_head"
]


for feature in features:
    h_cond = conditional_entropy(df, feature, target)

    ig = information_gain(df, feature, target)

    print(f"{feature:15} | H(Y|X)={h_cond:.3f} | IG={ig:.3f}")


best_feature = max(
    features,
    key=lambda f: information_gain(df, f, target)
)


print("Best split:", best_feature)