import pandas as pd

data = pd.read_csv("thanksgiving.csv", encoding="Latin-1")

# print(data.head(3))
# print(data.columns)
# print(data["Do you celebrate Thanksgiving?"].value_counts())

yes_cel_con = data["Do you celebrate Thanksgiving?"] == "Yes"
yes_data = data[yes_cel_con]

# print(yes_data.head(1))

Tofurkey_con = data["What is typically the main dish at your Thanksgiving dinner?"] == "Tofurkey"
Tofurkey_data = data[Tofurkey_con]
# print(Tofurkey_data["Do you typically have gravy?"])

con_app_str = "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"
con_pumpkin_str = "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"
con_pecan_str = "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan"

apple_isnull = data[con_app_str].isnull()
pumpkin_isnull = data[con_pumpkin_str].isnull()
pecan_isnull = data[con_pecan_str].isnull()

ate_pies = data[apple_isnull & pumpkin_isnull & pecan_isnull]

print(ate_pies.head())
