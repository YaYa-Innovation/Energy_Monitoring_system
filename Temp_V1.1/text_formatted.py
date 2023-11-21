import time
while True:
	with open('/home/pi/Temp_V1.1/data_files/hmi_output_file.txt', 'r') as new_result_data_file:
	    new_result_data_lines = new_result_data_file.readlines()

	with open('/home/pi/Temp_V1.1/data_files/box.txt', 'r') as box_file:
	    box_lines = box_file.readlines()

	with open('/home/pi/Temp_V1.1/data_files/normal_color_range.txt', 'r') as normal_color_range_file:
	    normal_color_range_lines = normal_color_range_file.readlines()
	    
	with open('/home/pi/Temp_V1.1/data_files/warning_color_range.txt', 'r') as warning_color_range_file:
	    warning_color_range_lines = warning_color_range_file.readlines()
	    
	with open('/home/pi/Temp_V1.1/data_files/danger_color_range.txt', 'r') as danger_color_range_file:
	    danger_color_range_lines = danger_color_range_file.readlines()
	    
	with open('/home/pi/Temp_V1.1/data_files/label.txt', 'r') as label_file:
	    label_lines = label_file.readlines()
	    
	with open('/home/pi/Temp_V1.1/data_files/original_file.txt', 'w') as original_file:
	    for box_line, result_line, normal_line ,warning_line ,danger_line ,label_line in zip(box_lines, new_result_data_lines, normal_color_range_lines,warning_color_range_lines,danger_color_range_lines,label_lines):
	        original_file.write(f"temperature {box_line.strip()} = {result_line.strip()}, normal_color={normal_line.strip()}, warning_color={warning_line.strip()}, danger_color={danger_line.strip()}, label={label_line.strip()}\n")
	        
	with open('/home/pi/Temp_V1.1/data_files/original_file.txt', 'r') as original1_file:
	    original1 = original1_file.readlines()
	    print(original1)

	print("Data replaced and saved to 'original_file.txt'")
	time.sleep(1)
