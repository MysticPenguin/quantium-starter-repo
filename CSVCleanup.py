import pandas as pd
data_list = []

def clean(sr):
    global data_list
    array = sr.array
    if(array[0] == "pink morsel"):
        cost = array[1]
        quant = array[2]
        cost_str = cost.replace("$", "").replace(",", "")
        # Convert the clean string to a float
        cost_float = float(cost_str)
        total = cost_float * quant
        clean_row = [f"${total:,.2f}",array[3],array[4]]
        data_list.append(clean_row)



df = pd.read_csv('C:\\Users\\Benja\\Documents\\CSE 495 Project\\quantium-starter-repo\\data\\daily_sales_data_2.csv')


df.apply(clean, axis=1, raw = False)


clean_data = pd.DataFrame(columns=["sold","date","region"],data=data_list)
print(clean_data)
clean_data.to_csv("daily_sales_data_clean_2.csv")
# for i in df.index:
#         test = df.loc[i]
#         print(test)
#
# print(df)
