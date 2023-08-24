import pandas as pd

# CSV 파일 경로 설정
csv_file_path = 'data/twisted_point.csv'

# CSV 파일 읽어와 DataFrame 객체 생성
data_frame = pd.read_csv(csv_file_path)

# DataFrame 객체로부터 데이터 조작 가능
# 예를 들어, 처음 5개 행 출력
print(data_frame.head())

# 특정 열의 데이터 출력
print(data_frame['SWAY_CD'])


# DataFrame의 각 행을 순회하며 작업 수행
for index, row in data_frame.iterrows():
    # if index < 45:
    #     continue
    # if index > 60:
    #     break
    # index는 행의 인덱스, row는 Series 객체로 해당 행의 데이터를@SLNG_YMD 담고 있음
    print(f"-- Index: {index}")
    dptm = str(int(row['SLNG_TM']))
    if(len(dptm) != 4):
        dptm = "0"+dptm if len(dptm) == 3 else "00"+dptm
    
    swayCd = row['SWAY_CD']
    rtCd = "RT" + swayCd[2:]
    
    printData = """
        SET @SLNG_YMD = '""" + str(int(row['SLNG_YMD'])) + """';
        SET @RT_CD = '""" + rtCd + """';
        SET @DPTM = '""" +dptm+ """';
        SET @SHIP_CD = '""" +row['SHIP_CD']+ """';
        SET @CBN_CD = '"""+row['CBN_CD']+"""';


        REG_ID = """+row['REG_ID']+"""
    """
    print(printData)
    print("-----------------------")


# 특정 조건을 만족하는 행 필터링
# filtered_data = data_frame[data_frame['열이름'] > 10]