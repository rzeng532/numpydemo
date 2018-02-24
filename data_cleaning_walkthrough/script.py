import pandas as pd

DATAFOLDER = 'data/'

data_files = [
    DATAFOLDER + "ap_2010.csv",
    DATAFOLDER + "class_size.csv",
    DATAFOLDER + "demographics.csv",
    DATAFOLDER + "graduation.csv",
    DATAFOLDER + "hs_directory.csv",
    DATAFOLDER + "sat_results.csv"
]

data = {}

for filename in data_files:
    data_frame = pd.read_csv(filename)
    data[filename.replace(DATAFOLDER, "").replace(".csv", "")] = data_frame

#read & parse txt file, then combine 2 dataframe
s_all = pd.read_csv(DATAFOLDER + 'survey_all.txt', delimiter='\t', encoding='utf-8')
shape_info = s_all.shape
print(shape_info[0])
print(shape_info[1])

s_d75 = pd.read_csv(DATAFOLDER + 'survey_d75.txt', delimiter='\t', encoding='utf-8')
shape_info = s_d75.shape
print(shape_info[0])
print(shape_info[1])

survey = pd.concat([s_all, s_d75], axis = 0)

#大小写转换
survey['DBN'] = survey['dbn']

#选择需要的列
what_we_need = ["DBN"
                , "rr_s"
                , "rr_t"
                , "rr_p"
                , "N_s"
                , "N_t"
                , "N_p"
                , "saf_p_11"
                , "com_p_11"
                , "eng_p_11"
                , "aca_p_11"
                , "saf_t_11"
                , "com_t_11"
                , "eng_t_11"
                , "aca_t_11"
                , "saf_s_11"
                , "com_s_11"
                , "eng_s_11"
                , "aca_s_11"
                , "saf_tot_11"
                , "com_tot_11"
                , "eng_tot_11"
                , "aca_tot_11"]

survey = survey.loc[:, what_we_need]

#放入 dict
data['survey'] = survey





