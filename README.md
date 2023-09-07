# Car Purchase Prediction Amount
Project made for the specialization on Machine Learning and Deep Learning.

# Follow the instructions

 ![Screenshot](Instructions.gif)

 1 - According to the Gif run the 'Car Purchase Model Building.ipynb'. You need to download it first and use Google Colab for running it.
 2 - You'll see the choose file button waiting for been hit. Hit it and choose the file 'Car_Purchasing_Data.csv', you have downloaded as well.
 3 - After run everything the Car Purchase Model Building.ipynb will force download 'keras_cifar10_trained_model.h5'. Get it and use into your API if you don't want use the one I made.
 4 - Inside Python project folder terminal, run 'pip install requirementes.txt'
 5 - After that, run 'uvicorn mlapi:app --reload'. You'll see a message like this: "Application startup complete."
 6 - Using a cURL, postman or any tool you want, run this cURL command:
  ```
  curl  --location 'http://127.0.0.1:8000' \
        --header 'Content-Type: application/json' \
        --data '{
            "Gender": 1,
            "Age": 50,
            "AnnualSalary": 45000,
            "CreditCardDebt": 30000,
            "NetWorth": 6000
        }'
  ```
7 - You should see the result.
<img width="1136" alt="Screen Shot 2023-09-07 at 13 47 44" src="https://github.com/renatomateusx/Car_Purchase_Prediction_Amount/assets/4579323/44fb00e5-da3c-4435-b619-743ad76802d2">

