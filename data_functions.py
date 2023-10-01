def min_employee_2_day(day1,day2):
    check1 = day1 in data["date"].values
    check2 = day2 in data["date"].values
    if check1==False or check2==False:
        day2Employee = "invalid input please check the data"
    else:
        id1 = data.loc[data["date"]==day1]["id"].to_string(index=False)
        id2 = data.loc[data["date"]==day2]["id"].to_string(index=False)
        new_data = data.loc[(data['id'] >= int(id1)) & (data['id'] <= int(id2))]
        day2minEmployee = min(new_data["employee"])
        minDayData = new_data.loc[new_data["employee"]==day2minEmployee]
        d = str(minDayData["date"].to_string(index=False))
        day = d.replace("\n"," and ")
        day2Employee = f"After analysing all the data in between {day1} and {day2}, minimum {day2minEmployee} employees worked on {day}"
    return day2Employee

def min_material_2_day(day1,day2):
    check1 = day1 in data["date"].values
    check2 = day2 in data["date"].values
    if check1==False or check2==False:
        day2Mat = "invalid input please check the data"
    else:
        id1 = data.loc[data["date"]==day1]["id"].to_string(index=False)
        id2 = data.loc[data["date"]==day2]["id"].to_string(index=False)
        new_data = data.loc[(data['id'] >= int(id1)) & (data['id'] <= int(id2))]
        day2minMat = min(new_data["material"])
        minDayData = new_data.loc[new_data["material"]==day2minMat]
        d = str(minDayData["date"].to_string(index=False))
        day = d.replace("\n"," and ")
        day2Mat = f"minimum {day2minMat} materials are on {day} in all data between {day1} and {day2}"
    return day2Mat

def min_sr_2_day(day1,day2):
    check1 = day1 in data["date"].values
    check2 = day2 in data["date"].values
    if check1==False or check2==False:
        day2SR = "invalid input please check the data"
    else:
        id1 = data.loc[data["date"]==day1]["id"].to_string(index=False)
        id2 = data.loc[data["date"]==day2]["id"].to_string(index=False)
        new_data = data.loc[(data['id'] >= int(id1)) & (data['id'] <= int(id2))]
        day2minSR = min(new_data["strike_rate"])
        minDayData = new_data.loc[new_data["strike_rate"]==day2minSR]
        d = str(minDayData["date"].to_string(index=False))
        day = d.replace("\n"," and ")
        day2SR = f"In {day1} and {day2} i found the highest strike rate {day2minSR*100}% on {day}"
    return day2SR

def min_shop_2_day(day1,day2):
    check1 = day1 in data["date"].values
    check2 = day2 in data["date"].values
    if check1==False or check2==False:
        day2Shop = "invalid input please check the data"
    else:
        id1 = data.loc[data["date"]==day1]["id"].to_string(index=False)
        id2 = data.loc[data["date"]==day2]["id"].to_string(index=False)
        new_data = data.loc[(data['id'] >= int(id1)) & (data['id'] <= int(id2))]
        day2minShop = min(new_data["shop"])
        minDayData = new_data.loc[new_data["shop"]==day2minShop]
        d = str(minDayData["date"].to_string(index=False))
        day = d.replace("\n"," and ")
        day2Shop = f"On {day},I found the highest number of shops {day2minShop} in between {day1} and {day2}"
    return day2Shop