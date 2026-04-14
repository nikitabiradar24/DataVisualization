from flask import Flask, jsonify, send_file, request
from flask_cors import CORS
import matplotlib.pyplot as plt
import io

from query import QueryProcessor

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    print("Home endpoint hit")
    return "Hello World"

@app.route('/test')
def test():
    print("Test endpoint hit")
    return "Working"

@app.route('/visualize', methods=['POST'])
def visualize():
    try:
        print("\n--- /visualize endpoint hit ---")

        input_data = request.json
        print("Step 1: Received input_data:", input_data)
        print("Type of input_data:", type(input_data))

        if input_data is None:
            print("No JSON received in request")
            return "No JSON received", 400

        qp = QueryProcessor(input_data)
        print("Step 2: QueryProcessor initialized:", qp)


        df = qp.get_dataframe()
        print("Step 3: DataFrame created")
        print("DataFrame head:\n", df.head())
        print("DataFrame types:\n", df.dtypes)

        
        df['purchase_count'] = df['purchase_count'].astype(int)
        print("Step 4: purchase_count converted to int")
        print(df['purchase_count'])


        plt.figure(figsize=(10,6))
        print("Step 5: Plotting bar chart")
        plt.bar(df['product_category_name'], df['purchase_count'], color='skyblue')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        print("Step 5: Plot created")

        
        img = io.BytesIO()
        plt.savefig(img, format='png', bbox_inches='tight')
        img.seek(0)
        plt.close()
        print("Step 6: Image saved to BytesIO")

       
        print("Step 7: Sending image back")
        return send_file(img, mimetype='image/png')

    except Exception as e:
        print("Error caught in /visualize:", e)
        return f"Internal Server Error: {e}", 500

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True, use_reloader=False)  # use_reloader=False to avoid Windows console crash