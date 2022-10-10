# Eco-fertilization

## Abstract
Fertilizer use is typically under the limited control of farmers. For the farmers to achieve higher yields and reduce fertilizer loss, competent guidance is required for the best use of these fertilizers. Additionally, there is a connection between rainfall volume and nutrient loss for various fertilizer applications after each rainfall event. Rainfall that is moderate and falls at the right moment can help nutrients penetrate the soil's rooting zone and dissolve dry fertilizer. However, too much rain can increase the possibility of runoff and the pace at which nutrients like nitrogen (N) which is quintessential, phosphorus (P), and potassium (K) which are crucial, manganese (Mn), and boron (B) that are present in the soil. <br>
&nbsp;&nbsp;&nbsp;&nbsp; This project presents nutrient recommendations using an updated iteration of the random forest algorithm which is based on time-series data to forecast the required quantity of nutrients for various crops by examining rainfall patterns and crop fertility. The method suggested in this study, comes in handy for improving soil fertility by providing nutrients recommendations for optimum conditions for crop growth and reducing leaching and runoff potential.
 
## Required Modules/Tools
1.	Python programming language
2.	Flask web framework
3.	Web Browser
4.	Bash for Windows ([recommended](https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/))

## Version Info
*	Python 3.8.10
*	Matplotlib 3.4.3
*	Flask 2.1.2
*	Category Encoders 2.5.0
*	requests 2.27.1
*	json 2.0.9
*	numpy 1.22.3
*	pandas 1.3.3
*	scikit-learn 1.0.2

## Python modules installation commands
*	pip install flask
*	pip install pandas
*	pip install sklearn
*	pip install category-encoders
*	pip install matplotlib
*	pip install requests
*	pip install numpy

## Instructions
*	Install the required modules and tools listed above.
*	Run the website using below procedure:
	*	Navigate to this path `Eco-Fertilization/Code/app/`
	*	Run the "app.py" using below commands: <br>
      		1.	For Ubuntu & Mac <br>
		        `python3 app.py`  <br>
      		2.	For Windows <br>
		        Double click on `app.py` <br>
			(or use bash and follow Ubuntu's OS procedure) <br>
* Copy the provided URL shown in terminal ie. `http://127.0.0.1:5000` and paste it on the web browser.
* Now input the required fields and submit the details.
* It will show N:P:K content ratio in the soil required for the crop.
* Also message/alert is displayed below the result. Seven days weather forecasts is also displayed along with the result. 

## Reference Video 
[Click to play video](https://drive.google.com/file/d/1lL5mmASWBbWVkvTqSFHfkhVXbXj_YDVn/view?usp=sharing)
