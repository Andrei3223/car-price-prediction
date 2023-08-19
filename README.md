# Streamlit project to predict the price of used cars

In this project linear regression is used to predict the price of vehicle on the secondary marked. The price is evaluated by 
such characteristics as car's year of manufacture, car mileage, fuel type and so on.


## Files

- `app.py`: streamlit app file
- `EDA_cars_hw.ipynb`: jupyter project to prepare and analyze data, to make a model (linear regression). The model is
saved into `model.pickle` file  
- `model.pickle`: file with prediction model
- `requirements.txt`: package requirements files
- `Drive.jpg`: awesome Ryan Gosling picture

## Run Demo Locally 

### Shell

For directly run streamlit locally in the repo root folder as follows:

```shell
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ streamlit run app.py
