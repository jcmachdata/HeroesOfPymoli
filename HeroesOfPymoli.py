# Dependencies and Setup
import pandas as pd
import numpy as np

# Load purchasing data 
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)

#display total number of players
purchase_data["SN"].nunique()

#Display total number of players, alternate method
total = purchase_data["SN"].value_counts()
total_final=len(total)
total_final

#calculate number of unique items
unique_items = purchase_data["Item ID"].value_counts()
number_unique_items = len(unique_items)

#calculate average price of items
average_price = purchase_data["Price"].mean()
average_price = round(average_price, 2)
average_price = "${:,.2f}".format(average_price)

#output results to dataframe
purchasing_analysis_df = pd.DataFrame({"Number of items": [number_unique_items], "Average Price": [average_price]})
purchasing_analysis_df

#Group by gender
gender_overview = purchase_data.groupby("Gender")["SN"].nunique()
gender_overview

#find gender numbers
gender_count = gender_overview["Female"]+gender_overview["Male"]+gender_overview["Other / Non-Disclosed"]
gender_count_male = gender_overview["Male"]
gender_count_female = gender_overview["Female"]
gender_count_other = gender_overview["Other / Non-Disclosed"]
gender_count_male = round(gender_count_male)

#calculate gender percentages
male_percent = gender_count_male / gender_count
female_percent = gender_count_female / gender_count
other_percent = gender_count_other / gender_count
male_percent = ("{:.2%}".format(male_percent))
female_percent = ("{:.2%}".format(female_percent))
other_percent = ("{:.2%}".format(other_percent))

#output results to dataframe
gender_df = pd.DataFrame({"": ["Total Number","Percentage"],"Male": [gender_count_male, male_percent],"Female":[gender_count_female, female_percent],"Other / ND": [gender_count_other, other_percent]})
gender_df = gender_df.set_index("")
gender_df

#calculate total purchases per gender
purchase_gender = purchase_data.set_index("Gender")
purchase_gender_male = purchase_gender.loc["Male",:]
purchase_gender_female = purchase_gender.loc["Female",:]
purchase_gender_other = purchase_gender.loc["Other / Non-Disclosed",:]
purchase_count_male = len(purchase_gender_male)
purchase_count_female = len(purchase_gender_female)
purchase_count_other = len(purchase_gender_other)

#calculate average purchase price per gender
avg_purchase_price_male = purchase_gender_male["Price"].mean()
avg_purchase_price_female = purchase_gender_female["Price"].mean()
avg_purchase_price_other = purchase_gender_other["Price"].mean()

avg_purchase_price_male = round(avg_purchase_price_male,2)
avg_purchase_price_female = round(avg_purchase_price_female,2)
avg_purchase_price_other = round(avg_purchase_price_other,2)
avg_purchase_price_male = "${:,.2f}".format(avg_purchase_price_male)
avg_purchase_price_female = "${:,.2f}".format(avg_purchase_price_female)
avg_purchase_price_other = "${:,.2f}".format(avg_purchase_price_other)

#calculate total purchase per person per gender
avg_perperson_male = purchase_gender_male.groupby("SN")["Price"].sum()
avg_perperson_male2 = avg_perperson_male.mean()
avg_perperson_male2 = round(avg_perperson_male2,2)
avg_perperson_male2 = "${:,.2f}".format(avg_perperson_male2)
total_male = avg_perperson_male.sum()
total_male = "${:,.2f}".format(total_male)

avg_perperson_female = purchase_gender_female.groupby("SN")["Price"].sum()
avg_perperson_female2 = avg_perperson_female.mean()
avg_perperson_female2 = round(avg_perperson_female2,2)
avg_perperson_female2 = "${:,.2f}".format(avg_perperson_female2)
total_female = avg_perperson_female.sum()
total_female = "${:,.2f}".format(total_female)

avg_perperson_other = purchase_gender_other.groupby("SN")["Price"].sum()
avg_perperson_other2 = avg_perperson_other.mean()
avg_perperson_other2 = round(avg_perperson_other2,2)
avg_perperson_other2 = "${:,.2f}".format(avg_perperson_other2)
total_other = avg_perperson_other.sum()
total_other = "${:,.2f}".format(total_other)

#output results to dataframe
purchasing_analysis_gender = pd.DataFrame({"Gender":["Male","Female","Other / ND"],"Purchase Count": [purchase_count_male, purchase_count_female, purchase_count_other],
                                           "Total Purchase Value": [total_male, total_female,total_other], "Average Purchase Price": [avg_purchase_price_male, avg_purchase_price_female, avg_purchase_price_other],
                                          "Avg. Total Purchase Per Person": [avg_perperson_male2, avg_perperson_female2, avg_perperson_other2]})

purchasing_analysis_gender = purchasing_analysis_gender.set_index("Gender")
purchasing_analysis_gender

#configure age bins
age_bins = [0,9,14,19,24,29,34,39,120]
age_labels = ["<10","10-14","15-19","20-24","25-29","30-34","35-39","40+"]
purchase_data["Age Bin"] = pd.cut(purchase_data["Age"], age_bins, labels=age_labels)
age_grouped = purchase_data.groupby("Age Bin")

#calculate number and percentages by age group
count_age = age_grouped["SN"].nunique()
percentage_age = count_age/total_final

#output results to dataframe
age_demographic = pd.DataFrame({"Total Count": count_age, "Percentage of Players": percentage_age})
age_demographic["Percentage of Players"]=age_demographic["Percentage of Players"].map("{:.2%}".format)
age_demographic.index.name = None
age_demographic

#calculate purchase count, avg. purchase price, avg. purchase total per person
purchase_count = age_grouped["Item Name"].count()
avg_price = age_grouped["Price"].mean()
purchase_total = age_grouped["Price"].sum()
avg_perperson_price = purchase_total/count_age

#output results to dataframe
purchase_analysis_df = pd.DataFrame({"Purchase Count": purchase_count, "Average Price": avg_price,"Purchase Total": purchase_total, "Avg. Per Person": avg_perperson_price})
purchase_analysis_df["Average Price"] = purchase_analysis_df["Average Price"].map("${:.2f}".format)
purchase_analysis_df["Purchase Total"] = purchase_analysis_df["Purchase Total"].map("${:.2f}".format)
purchase_analysis_df["Avg. Per Person"] = purchase_analysis_df["Avg. Per Person"].map("${:.2f}".format)
purchase_analysis_df

#calculate top spenders
sn_group = purchase_data.groupby(["SN"])
sn_total_purchase = sn_group["Price"].sum()
sn_avg_purchase = sn_group["Price"].mean()

#sort by total purchase
sn_df = pd.DataFrame({"Avg. Purchase": sn_avg_purchase, "Total Purchase": sn_total_purchase})
sn_df_sort = sn_df.sort_values("Total Purchase", ascending=False)
sn_df_sort["Total Purchase"] = sn_df_sort["Total Purchase"].map("${:.2f}".format)
sn_df_sort["Avg. Purchase"] = sn_df_sort["Avg. Purchase"].map("${:.2f}".format)
sn_df_sort.head()

purchase_data.head()

#calculate purchase count, item price, and total purchase value
popular_df = purchase_data[["Item ID","Item Name","Price"]]
popular_grp = popular_df.groupby(["Item ID", "Item Name"])
pop_purchase = popular_grp["Item ID"].count()
pop_total = popular_grp["Price"].sum()
item_price = pop_total / pop_purchase

#output results to dataframe
pop_df = pd.DataFrame({"Purchase Count": pop_purchase, "Item Price": item_price,"Total Purchase Value": pop_total})
pop_df_sort = pop_df.sort_values("Purchase Count", ascending=False)
pop_df_sort["Total Purchase Value"] = pop_df_sort["Total Purchase Value"].map("${:.2f}".format)
pop_df_sort["Item Price"] = pop_df_sort["Item Price"].map("${:.2f}".format)
pop_df_sort.head()

#resort by most popular items
pop_df_sort = pop_df.sort_values("Total Purchase Value", ascending=False)
pop_df_sort["Total Purchase Value"] = pop_df_sort["Total Purchase Value"].map("${:.2f}".format)
pop_df_sort["Item Price"] = pop_df_sort["Item Price"].map("${:.2f}".format)

pop_df_sort.head()

