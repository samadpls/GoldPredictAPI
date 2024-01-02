# GoldPredictAPI 📈🤖

This project implements a gold price prediction system using machine learning. The system is trained on historical gold price data and provides a `FastAPI`-based API for making predictions.

## Files 📂

- **gld_predication.py**: FastAPI app with a pre-trained model, offering an API endpoint for gold price predictions.

- **Gold Price Prediction.ipynb**: Jupyter Notebook for initial gold price data exploration, preprocessing, and training of the RandomForestRegressor model.

## Dependencies 🛠️

- FastAPI
- Scikit-learn
- NumPy
- Pandas
- Matplotlib
- Seaborn

## How to Use 🚀

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the FastAPI application:

    ```bash
    uvicorn gld_predication:app --reload
    ```

    This will start the FastAPI server locally.

3. Make predictions using Swagger:

    Open your web browser and go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the Swagger UI.

    - Click on the `/predict` endpoint.
    - Click on the "Try it out" button.
    - Input the sample request data:

        ```json
        {
          "SPX": 2671.91992,
          "USO": 14.0600,
          "SLV": 15.5100,
          "EUR_USD": 1.186789
        }
        ```

    - Click on the "Execute" button to make a prediction.
      ![demo](https://github.com/samadpls/GoldPredictAPI/assets/94792103/0876bea2-aa30-4a63-a0a7-0e75badc699f)


4. Make predictions using curl:

    Alternatively, you can use `curl` to make predictions:

    ```bash
    curl -X 'POST' \
      'http://127.0.0.1:8000/predict' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "SPX": 2671.91992,
      "USO": 14.0600,
      "SLV": 15.5100,
      "EUR_USD": 1.186789
    }'
    ```

## Additional Information ℹ️

- **Colab Notebook**: The `Gold Price Prediction.ipynb` file in Google Colab contains the initial exploration and model training.

- **Model Saving**: The trained model is saved as `gld_data.pkl` using the `pickle` library and loaded by the FastAPI application for predictions.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
