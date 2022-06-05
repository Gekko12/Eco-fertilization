from types import CoroutineType
from flask import Flask, render_template, url_for, request
from BestTimeToFertilizeModule import BestTimeToFertilize
from NPKEstimatorModule import NPKEstimator


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/',methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        crop = request.form.get("crop")
        state = request.form.get("state")
        city = request.form.get("city")

        bttf = BestTimeToFertilize(city_name = city)
        bttf.api_caller()

        if bttf.is_api_call_success():
            category, heading, desc = bttf.best_time_fertilize()

            # today's weather data
            di = bttf.weather_data[0]
            temp = di['Temperature']
            humidity = di['Relative Humidity']
            rainfall = di["Rainfall"]

            est = NPKEstimator()
            est.renameCol()

            npk = {'Label_N':0, 'Label_P':0, 'Label_K':0}
            for y_label in ['Label_N', 'Label_P', 'Label_K']:
                npk[y_label] = est.estimator(crop, temp, humidity, rainfall, y_label)
            print(npk)

            output_data = category +"\n"+ heading +"\n"+ desc +"\n"+ str(npk['Label_N'])  +"\n"+ str(npk['Label_P'])  +"\n"+ str(npk['Label_K'])
            with open("output.txt", "w") as fh:
                fh.write(output_data)
                

        else:
            print("Error occured while calling weather API")
            
        with open("InputData.csv", "w") as fh:
            input_data = "%s,%s,%s" % (crop.strip(), state.strip(), city.strip())
            fh.write(input_data)

    return render_template("index.html")    


if __name__ == "__main__":
    app.run(debug=True)