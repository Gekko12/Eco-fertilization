var crop_arr = new Array("rice","maize","chickpea","kidneybeans","pigeonpeas","mothbeans","mungbean","blackgram","lentil","pomegranate","banana","mango","grapes","watermelon","muskmelon","apple","orange","papaya","coconut","cotton","jute","coffee");


function print_crop(crop_id){
	// given the id of the <select> tag as function argument, it inserts <option> tags
	var option_str = document.getElementById(crop_id);
	option_str.length=0;
	option_str.options[0] = new Option('Select Crop','');
	option_str.selectedIndex = 0;
	for (var i=0; i<crop_arr.length; i++) {
		option_str.options[option_str.length] = new Option(crop_arr[i],crop_arr[i]);
	}
}
