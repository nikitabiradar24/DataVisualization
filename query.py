import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
import subprocess
import json

class QueryProcessor:

    def __init__(self, input_data):
        self.input_data = input_data

    def get_dataframe(self):
        results_raw = self.input_data.get("results")
        df = pd.read_csv(StringIO(results_raw), sep=r"\s+")
        return df

    def convert_to_csv(self):
        df = self.get_dataframe()
        return df.to_csv(index=False)

    def clean_results(self, text):
        return "\n".join(line.strip() for line in text.strip().split("\n"))


    def get_graph_suggestion(self, df):
        prompt = f"""
        You are a data visualization expert.
        Given this dataset:
        {df.head(10).to_string(index=False)}

        Suggest the best graph type (only one word like: bar, line, pie, scatter).
        """

        result = subprocess.run(
            ["ollama", "run", "minimax-m2.5"],
            input=prompt,
            text=True,
            capture_output=True
        )

        return result.stdout.strip().lower()

    #  Plot based on model suggestion
    def plot_graph(self, df, graph_type):
        x = df.columns[0]
        y = df.columns[1]

        if graph_type == "bar":
            plt.bar(df[x], df[y])
        elif graph_type == "line":
            plt.plot(df[x], df[y])
        elif graph_type == "pie":
            plt.pie(df[y], labels=df[x], autopct='%1.1f%%')
        elif graph_type == "scatter":
            plt.scatter(df[x], df[y])
        else:
            print("Unknown graph type, defaulting to bar chart")
            plt.bar(df[x], df[y])

        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(f"{graph_type.capitalize()} Chart")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    input_data = {
        'results': """product_category_name purchase_count
0 cama_mesa_banho 11115
1 beleza_saude 9670
2 esporte_lazer 8641
3 moveis_decoracao 8334
4 informatica_acessorios 7827
5 utilidades_domesticas 6964
6 relogios_presentes 5991
7 telefonia 4545
8 ferramentas_jardim 4347
9 automotivo 4235"""
    }

    qp = QueryProcessor(input_data)
    df = qp.get_dataframe()

    # Get suggestion from Ollama
    graph_type = qp.get_graph_suggestion(df)
    print("Suggested Graph:", graph_type)

    # Plot graph
    qp.plot_graph(df, graph_type)