import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("pokemonv2.csv")

filtered_df = df[df["type1"].isin(["Dark", "Fairy"])]

fig,axes = plt.subplots(1,2,figsize=(18, 10))
axes[0] = sns.countplot(
    ax=axes[0],
    data=filtered_df,
    x="Region",  # Na osi X umieszczamy regiony
    hue="type1",  # Podział słupków wewnątrz regionu na typy 'Dark' i 'Fairy'
    palette={"Dark": "#705746", "Fairy": "#EE99AC"},
)
sns.move_legend(
    axes[0],
    "upper right",
    title="Typ Pokemona"
)
axes[0].set_title(
    "Liczba Pokemonów typu Dark i Fairy w poszczególnych regionach",
    fontsize=14,
    fontweight="bold",
    pad=15,
)
axes[0].set_xlabel("Region", fontsize=12)
axes[0].set_ylabel("Liczba Pokemonów", fontsize=12)



single_type_count = df["type2"].isnull().sum()
dual_type_count = df["type2"].notnull().sum()


labels = ["Jeden typ (Single Type)", "Dwa typy (Dual Type)"]
sizes = [single_type_count, dual_type_count]
explode = (0.05, 0)  # Delikatne "wysunięcie" pierwszego kawałka dla lepszego efektu


axes[1].pie(
    sizes,
    explode=explode,
    labels=labels,
    colors=["#4ff0a1", "#4f97f0"],
    autopct="%1.1f%%",  # Format wyświetlania procentów (jeden znak po przecinku)
    shadow=True,  # Dodanie delikatnego cienia
    startangle=140,  # Kąt obrotu wykresu
    textprops={"fontsize": 12},  # Rozmiar czcionki podpisów
)

axes[1].legend(title="Procentowy udział pokemonów z 1 i z oboma typami")

axes[1].set_title(
    "Procentowy udział Pokemonów jednotypowych i dwutypowych",
    fontsize=14,
    fontweight="bold",
    pad=20,
)
plt.axis("equal")


plt.tight_layout()
plt.savefig("pokemon2.png",dpi=300)
plt.show()
