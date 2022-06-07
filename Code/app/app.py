from flask import Flask, render_template, request, url_for
from BestTimeToFertilizeModule import BestTimeToFertilize
from NPKEstimatorModule import NPKEstimator


app = Flask(__name__)


@app.route('/processing/', methods=['GET', 'POST'])
def processing():
    # print('Processing......')
    if request.method == "GET":
        print("The URL /processing is accessed directly.")
        return url_for('index.html')

    if request.method == "POST":
        form_data = request.form
        call_success = []
        npk_list_dict = []
        popup_data = []
        seven_days = []

        crop = form_data['crop']
        state = form_data['state']
        city = form_data['city']

        with open("InputData.csv", "w") as fh:
            input_data = "%s,%s,%s" % (crop.strip(), state.strip(), city.strip())
            fh.write(input_data)
        
        bttf = BestTimeToFertilize(city_name = city, state_name = state)
        bttf.api_caller()

        if bttf.is_api_call_success():
            category, heading, desc = bttf.best_time_fertilize()

            call_success.append(1)
            popup_data.append([category, heading, desc])
            seven_days = bttf.weather_data[:]
            # print(seven_days)
            
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
            # print(npk)

            npk_list_dict.append(npk)

            output_data = category +"\n"+ heading +"\n"+ desc +"\n"+ str(npk['Label_N'])  +"\n"+ str(npk['Label_P'])  +"\n"+ str(npk['Label_K'])
            with open("output.txt", "w") as fh:
                fh.write(output_data)
        else:
            print("Error Occured")
        #print(call_success, npk_list_dict, form_data, popup_data)
        return render_template('update.html', CALL_SUCCESS = call_success, NPK = npk_list_dict, FORM_DATA = form_data, POPUP_DATA = popup_data, SEVEN_DAYS = seven_days)
    

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)