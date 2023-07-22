import importlib
import subprocess

# Check if requests module is installed
try:
    importlib.import_module('requests')
except ImportError:
    print("requests module is not installed. Attempting to install...")
    subprocess.check_call(['pip', 'install', 'requests'])

# Check if opencc-python-reimplemented module is installed
try:
    importlib.import_module('opencc')
except ImportError:
    print("opencc-python-reimplemented module is not installed. Attempting to install...")
    subprocess.check_call(['pip', 'install', 'opencc-python-reimplemented'])

# Check if pandas module is installed
try:
    importlib.import_module('pandas')
except ImportError:
    print("pandas module is not installed. Attempting to install...")
    subprocess.check_call(['pip', 'install', 'pandas'])



import requests
import json
import html
import argparse
from opencc import OpenCC

import pandas as pd

from io import StringIO

from data_source.ApiException import ApiException

def get_mtr_stations():
    response = requests.get("https://www.mtr.com.hk/st/data/fcdata_json.php")
    data = response.json()

    stations = data["faresaver"]['facilities']

    for station in stations:
        station["STATION_NAME_TC"] = html.unescape(
            station["STATION_NAME_TC"]) if station["STATION_NAME_TC"] else None
        station["SAVERTWO_TC"] = html.unescape(
            station["SAVERTWO_TC"]) if station["SAVERTWO_TC"] else None
        station["SAVERONE_TC"] = html.unescape(
            station["SAVERONE_TC"]) if station["SAVERONE_TC"] else None
        station["TOILET_TC"] = html.unescape(
            station["TOILET_TC"]) if station["TOILET_TC"] else None
        station["LINE"] = html.unescape(
            station["LINE"]) if station["LINE"] else None

    return stations


mtr_stations = get_mtr_stations()

with open("mtr_stations.json", "w", encoding="utf-8") as f:
    json.dump(mtr_stations, f, ensure_ascii=False, indent=4)

with open("mtr_lines_and_stations.json", "r", encoding="utf-8") as f:
    line_info = json.load(f)

def get_station_id(station_name):
    with open("mtr_stations.json", "r", encoding="utf-8") as f:
        stations = json.load(f)

    simplified_station_name = station_name.replace(" ", "").replace("-", "").lower()

    #读取line_info 循环 检查Station Code是否有匹配的
    for station_dict in line_info:
        if station_dict['Station Code'].lower() == simplified_station_name or station_dict['English Name'].replace(" ", "").replace("-", "").lower() == simplified_station_name or station_dict['Chinese Name'].replace(" ", "").replace("-", "").lower() == simplified_station_name:
            return str(station_dict['Station ID'])

    return None


def get_ticket_price(from_station_id, to_station_id, lang="C"):
    if lang not in ["C", "E"]:
        raise ValueError("Invalid lang parameter. Only 'C' (Chinese) or 'E' (English) are allowed.")
    url = f"https://www.mtr.com.hk/share/customer/jp/api/HRRoutes/?o={from_station_id}&d={to_station_id}&lang={lang}"
    print(url)
    response = requests.get(url)
    data = response.json()

    ticket_prices = []
    station_info = {}

    firstTrainTime = data['firstTrain']
    lastTrainTime = data['lastTrain']

    firstLastTrainRemark = data['firstLastTrainRemark']
    stationOpeningHours = data['stationOpeningHours']

    for route in data['routes']:
        route_name = route['routeName']
        time = route['time']

        for fare in route['fares']:
            fare_title = fare.get('fareTitle')
            fare_info = fare.get('fareInfo', {})

            if fare_title in ['standardClass'] and 'adult' in fare_info:

                adult_price = fare_info['adult']['octopus']
                student_price = fare_info.get('student', {}).get('octopus')

                ticket_prices.append({
                    'fareTitle': fare_title,
                    'routeName': route_name,
                    'fareTitle': fare_title,
                    'adultPrice': adult_price,
                    'studentPrice': student_price,
                    'time': time,
                    'path': route['path']
                })

    station_info['firstTrainTime'] = firstTrainTime
    station_info['lastTrainTime'] = lastTrainTime
    station_info['firstLastTrainRemark'] = firstLastTrainRemark
    station_info['stationOpeningHours'] = stationOpeningHours
    return ticket_prices, station_info



def convert_to_traditional_chinese(station_name):
    cc = OpenCC('s2twp')
    return cc.convert(station_name)


def format_station_info(station_info):
    line = station_info["LINE"]
    station_name_tc = station_info["STATION_NAME_TC"]
    station_name_en = station_info["STATION_NAME_EN"]
    formatted_info = f"[{line}] {station_name_tc} ({station_name_en})"

    return formatted_info


def query_station_info(station_id):
    station_info = get_station_info(station_id)

    if station_info is None:
        raise ApiException("搵唔到指定嘅車站，請檢查輸入嘅車站 ID 是否正確。")
    else:
        formatted_info = format_station_info(station_info)
        return formatted_info


def get_station_info(station_id):
    with open("mtr_stations.json", "r", encoding="utf-8") as f:
        stations = json.load(f)

    for station in stations:
        if station["STATION_ID"] == station_id:
            return station

    return None


line_dict = {
    'AEL': "機場快綫 (Airport Express)",
    'TCL': "東涌綫 (Tung Chung Line)",
    'DRL': "迪士尼綫 (Disneyland Resort Line)",
    'EAL': "東鐵綫 (East Rail Line)",
    'ISL': "港島綫 (Island Line)",
    'KTL': "觀塘綫 (Kwun Tong Line)",
    'SIL': "南港島綫 (South Island Line)",
    'TKL': "將軍澳綫 (Tseung Kwan O Line)",
    'TWL': "荃灣綫 (Tseun Wan Line)",
    'TML': "屯馬綫 (Tuen Ma Line)"
}


def convert_to_json(json_file):
    # 读取CSV内容
    data = pd.read_csv('mtr_lines_and_stations.csv')

    # 转换为JSON格式
    json_data = data.to_json(orient='records')

    # 解析JSON数据
    json_data = json.loads(json_data)

    # 将JSON数据保存到文件
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=4)


def query_specific_line(src,dst,time):
    result = src.split(" ", 1)[1]
    for idx,line in enumerate(time['links']):
        result += f' > {line_dict[line]}'
        if time['interchange'] and idx < len(time['interchange']):
            result += f' > {query_station_info(time["interchange"][idx]).split(" ", 1)[1]}'
    result += f' > {dst.split(" ", 1)[1]}\n'
    return result


def get_station_abbreviation(station_id):
    matches = set()
    for station_dict in line_info:
        if str(station_dict['Station ID']) == str(station_id):
            matches.add((station_dict['Line Code'], station_dict['Station Code']))
    return list(matches)


def get_station_names(abbreviation, lang="EN"):
    matches = []
    for station_dict in line_info:
        if station_dict['Station Code'].lower() == abbreviation.lower():
            if lang.upper() == "TC":
                name = station_dict['Chinese Name']
            else:
                name = station_dict['English Name']
            matches.append((station_dict['Line Code'], name))
    return matches



def get_realtime_arrivals(line, station, lang="EN"):
    url = f"https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php?line={line}&sta={station}&lang={lang}"
    print(url)
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        if "data" in data and f"{line}-{station}" in data["data"]:
            result = ""

            if "UP" in data["data"][f"{line}-{station}"]:
                arrivals_up = data["data"][f"{line}-{station}"]["UP"]
                if arrivals_up:
                    if lang.upper() == "TC":
                        result += "實時到站信息：(上行)\n"
                        for arrival in arrivals_up:
                            time = arrival["time"]
                            destination = arrival["dest"]
                            destination_name = get_station_names(destination, lang)
                            if destination_name:
                                destination = destination_name[0][1]
                            platform = arrival["plat"]
                            result += f"時間：{time}，目的地：{destination}，站台號：{platform}\n"
                    else:
                        result += "Real-time Arrivals (Up):\n"
                        for arrival in arrivals_up:
                            time = arrival["time"]
                            destination = arrival["dest"]
                            destination_name = get_station_names(destination, lang)
                            if destination_name:
                                destination = destination_name[0][1]
                            platform = arrival["plat"]
                            result += f"Time: {time}, Destination: {destination}, Platform: {platform}\n"

                else:
                    if lang.upper() == "TC":
                        result += "沒有找到上行實時到站信息。\n"
                    else:
                        result += "No real-time arrivals found (Up).\n"

            if "DOWN" in data["data"][f"{line}-{station}"]:
                arrivals_down = data["data"][f"{line}-{station}"]["DOWN"]
                if arrivals_down:
                    if lang.upper() == "TC":
                        result += "實時到站信息：(下行)\n"
                        for arrival in arrivals_down:
                            time = arrival["time"]
                            destination = arrival["dest"]
                            destination_name = get_station_names(destination, lang)
                            if destination_name:
                                destination = destination_name[0][1]
                            platform = arrival["plat"]
                            result += f"時間：{time}，目的地：{destination}，站台號：{platform}\n"
                    else:
                        result += "Real-time Arrivals (Down):\n"
                        for arrival in arrivals_down:
                            time = arrival["time"]
                            destination = arrival["dest"]
                            destination_name = get_station_names(destination, lang)
                            if destination_name:
                                destination = destination_name[0][1]
                            platform = arrival["plat"]
                            result += f"Time: {time}, Destination: {destination}, Platform: {platform}\n"

                else:
                    if lang.upper() == "TC":
                        result += "沒有找到下行實時到站信息。\n"
                    else:
                        result += "No real-time arrivals found (Down).\n"

            if result:
                return result.strip()
            else:
                if lang.upper() == "TC":
                    return "沒有找到實時到站信息。"
                else:
                    return "No real-time arrivals found."

        else:
            if lang.upper() == "TC":
                return "該線路和車站沒有可用數據。"
            else:
                return "No data available for the specified line and station."

    else:
        if lang.upper() == "TC":
            return "獲取實時數據時發生錯誤。"
        else:
            return "Error occurred while fetching real-time data."


def query_ticket_price(from_station_name, to_station_name, tg_inline_mode=False, lang="C"):
    output_text = ""
    title_msg = ""
    from_station_id = get_station_id(from_station_name)
    to_station_id = get_station_id(to_station_name)

    if from_station_id is None or to_station_id is None:
        traditional_from_station_name = convert_to_traditional_chinese(
            from_station_name)
        traditional_to_station_name = convert_to_traditional_chinese(
            to_station_name)

        if traditional_from_station_name != from_station_name:
            from_station_id = get_station_id(traditional_from_station_name)

        if traditional_to_station_name != to_station_name:
            to_station_id = get_station_id(traditional_to_station_name)

    if from_station_id is None or to_station_id is None:
        if lang == "C":
            raise ApiException("無法找到指定嘅車站，請檢查輸入嘅車站名稱是否正確。")
        elif lang == "E":
            raise ApiException("Unable to find the specified stations. Please check if the station names are correct.")
    else:
        ticket_prices, station_info = get_ticket_price(
            from_station_id, to_station_id, lang)
        if not ticket_prices:
            if lang == "C":
                raise ApiException("冇搵到適用嘅車票價錢。")
            elif lang == "E":
                raise ApiException("No applicable ticket prices found.")

        if lang == "C":
            output_text += '[Hong Kong MTR車票價格]\n'
        elif lang == "E":
            output_text += '[Hong Kong MTR Ticket Prices]\n'

        from_station_info = format_station_info(
            get_station_info(from_station_id))

        to_station_info = format_station_info(get_station_info(to_station_id))


        if lang == "C":
            output_text += f"由 {from_station_info} 去 {to_station_info} 嘅車票價格：\n"
            title_msg += f"由 {from_station_info} 去 {to_station_info} 嘅車票價格"
            output_text += '\n請留意，該車票價格僅計算使用八達通拍卡或使用乘車二維碼入閘嘅價格，唔包括購買單程票嘅價格。\n\n'
            output_text += f'首班車時間：{station_info["firstTrainTime"]["time"]}\n'
            output_text += '首班車路綫: '
            output_text += query_specific_line(from_station_info, to_station_info, station_info["firstTrainTime"])
            output_text += f'末班車時間：{station_info["lastTrainTime"]["time"]}\n'
            output_text += '尾班車路綫: '
            output_text += query_specific_line(from_station_info, to_station_info, station_info["lastTrainTime"])
            output_text += f'{station_info["firstLastTrainRemark"]}\n'
            output_text += f'車站開放時間：{station_info["stationOpeningHours"]}\n'
            output_text += "乘搭首/尾班車的乘客必須使用本頁列明的轉乘路綫，因有關的轉乘路綫可能與行程指南所建議的路綫不同。\n\n"

        elif lang == "E":
            output_text += f"Ticket prices from {from_station_info} to {to_station_info}:\n"
            title_msg += f"Ticket prices from {from_station_info} to {to_station_info}"
            output_text += '\nPlease note that the ticket prices only apply to Octopus card or QR code entry, and do not include the price of single journey tickets.\n\n'
            output_text += f'First Train Time: {station_info["firstTrainTime"]["time"]}\n'
            output_text += 'First Train Route: '
            output_text += query_specific_line(from_station_info, to_station_info, station_info["firstTrainTime"])
            output_text += f'Last Train Time: {station_info["lastTrainTime"]["time"]}\n'
            output_text += 'Last Train Route: '
            output_text += query_specific_line(from_station_info, to_station_info, station_info["lastTrainTime"])
            output_text += f'{station_info["firstLastTrainRemark"]}\n'
            output_text += f'Station Opening Hours: {station_info["stationOpeningHours"]}\n'
            output_text += "Passengers taking the first/last train must use the transfer routes listed on this page, as the recommended routes in the travel guide may differ.\n\n"

        departure_station_abbreviations = get_station_abbreviation(from_station_id)
        if departure_station_abbreviations:
            if lang == "C":
                output_text += f"{from_station_info} 嘅實時發車時間：\n"
            elif lang == "E":
                output_text += f"Real-time departure times from {from_station_info}:\n"

            for line, abbreviation in departure_station_abbreviations:
                if lang == "C":
                    arrivals_lang = "TC"
                elif lang == "E":
                    arrivals_lang = "EN"
                realtime_departure = get_realtime_arrivals(line, abbreviation, arrivals_lang)
                if realtime_departure:
                    if lang == "C":
                        output_text += f"線路：{line_dict[line]}\n"
                        output_text += f"{realtime_departure}\n\n"
                    elif lang == "E":
                        output_text += f"Line: {line_dict[line]}\n"
                        output_text += f"{realtime_departure}\n\n"
        else:
            if lang == "C":
                output_text += f"無法獲取 {from_station_info} 的實時發車時間。\n\n"
            elif lang == "E":
                output_text += f"Unable to retrieve real-time departure times for {from_station_info}.\n\n"

        for price in ticket_prices:
            route_name = price['routeName']
            adult_price = price['adultPrice']
            student_price = price['studentPrice']
            fareTitle = price['fareTitle']
            time = price['time']
            path = price['path']

            if lang == "C":
                if fareTitle == 'standardClass':
                    output_text += f"\n車廂類型：普通等\n"
                elif fareTitle == 'firstClass':
                    output_text += f"\n車廂類型：头等\n"
                output_text += f"路線名稱：{route_name}\n"
                output_text += f"成人票價：{adult_price}\n"
                output_text += f"學生票價：{student_price}\n"
                output_text += f"行車時間：{time}分鐘\n"
                output_text += f"路線：\n"
                for segment in path:
                    link_text = segment.get('linkText')
                    if link_text is not None:
                        output_text += f"{link_text}\n"
            elif lang == "E":
                if fareTitle == 'standardClass':
                    output_text += f"\nCar Type: Standard\n"
                elif fareTitle == 'firstClass':
                    output_text += f"\nCar Type: First Class\n"
                output_text += f"Route Name: {route_name}\n"
                output_text += f"Adult Price: {adult_price}\n"
                output_text += f"Student Price: {student_price}\n"
                output_text += f"Travel Time: {time} minutes\n"
                output_text += f"Route:\n"
                for segment in path:
                    link_text = segment.get('linkText')
                    if link_text is not None:
                        output_text += f"{link_text}\n"

        if tg_inline_mode:
            return output_text, title_msg
        else:
            return output_text


# 如果直接调用这个文件，就会执行下面的代码
if __name__ == "__main__":

    # 创建命令行解析器
    parser = argparse.ArgumentParser(description='查询车票价格')

    # 添加命令行参数
    parser.add_argument('from_station', help='出发站')
    parser.add_argument('to_station', help='到达站')

    # 解析命令行参数
    args = parser.parse_args()

    # 获取出发站和到达站
    from_station_name = args.from_station
    to_station_name = args.to_station

    #更新车站信息
    url = 'https://opendata.mtr.com.hk/data/mtr_lines_and_stations.csv'
    json_file = 'mtr_lines_and_stations.json'
    convert_to_json(json_file)
    # 查询车票价格
    output_text = query_ticket_price(from_station_name, to_station_name)
    print(output_text)

    #print(get_station_abbreviation("上水"))
    #print(get_realtime_arrivals("EAL", "SHS", "TC"))
