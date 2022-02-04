from jbi100_app.data import get_coordinates

# Here you can add any global configuations

color_list1 = ["green", "blue"]
color_list2 = ["red", "purple"]
final_old = ['Day_of_Week', 'Hour', 'Road_Type',
             'Speed_limit', 'Pedestrian_Crossing-Physical_Facilities', 'Light_Conditions',
             'Weather_Conditions', 'Road_Surface_Conditions', 'Special_Conditions_at_Site',
             'Carriageway_Hazards', 'Age_Band_of_Casualty', 'Bus_or_Coach_Passenger',
             'Pedestrian_Road_Maintenance_Worker',
             'Casualty_IMD_Decile', 'Towing_and_Articulation', 'Vehicle_Manoeuvre',
             'Vehicle_Location-Restricted_Lane', 'Junction_Location', 'Hit_Object_in_Carriageway',
             'Vehicle_Leaving_Carriageway', 'Hit_Object_off_Carriageway', '1st_Point_of_Impact',
             'Was_Vehicle_Left_Hand_Drive?', 'Journey_Purpose_of_Driver', 'Age_Band_of_Driver', 'Propulsion_Code',
             'Accident_Severity', 'Pedestrian_Crossing-Human_Control', 'Urban_or_Rural_Area',
             'Did_Police_Officer_Attend_Scene_of_Accident', 'Casualty_Class', 'Sex_of_Casualty',
             'Casualty_Severity', 'Car_Passenger', 'Casualty_Home_Area_Type', 'Driver_Home_Area_Type']

final = ['Day_of_Week', 'Hour', 'Road_Type', 'Speed_limit', 'Pedestrian_Crossing-Physical_Facilities',
         'Light_Conditions', 'Pedestrian_Location', 'Pedestrian_Movement', 'Weather_Conditions', 'Accident_Severity',
         'Pedestrian_Crossing-Human_Control', 'Casualty_Severity', 'Casualty_Class', 'Urban_or_Rural_Area',
         'Junction_Location', 'Sex_of_Casualty', 'Road_Surface_Conditions']

attributes_heat = ['Speed_limit', 'Accident_Severity', 'Hour', 'Junction_Detail', 'Casualty_Class']

months_list = ['All', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
               'November', 'December']

cities_df = get_coordinates().sort_values('city')
# pip install requirements.txt
