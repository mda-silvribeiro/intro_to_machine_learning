import pandas as pd
import numpy as np

df = pd.read_csv('ml-bugs.csv', delimiter = ';')

print(df)
print("#### Mobug ###")
df_mobug = df.loc[df['Species'] == 'Mobug']
print(len(df_mobug))
print(df_mobug)
print("#### Lobug ###")
df_lobug = df.loc[df['Species'] == 'Lobug']
print(len(df_lobug))
print(df_lobug)
print("#### Mobug Color == Brown ###")
df_mobug_brown = df_mobug.loc[df_mobug['Color'] == 'Brown']
print(len(df_mobug_brown))
print(df_mobug_brown)
print("#### Lobug Color == Brown ###")
df_lobug_brown = df_lobug.loc[df_lobug['Color'] == 'Brown']
print(len(df_lobug_brown))
print(df_lobug_brown)
print("#### Mobug Color != Brown ###")
df_mobug_not_brown = df_mobug.loc[df_mobug['Color'] != 'Brown']
print(len(df_mobug_not_brown))
print(df_mobug_not_brown)
print("#### Lobug Color != Brown ###")
df_lobug_not_brown = df_lobug.loc[df_lobug['Color'] != 'Brown']
print(len(df_mobug_not_brown))
print(df_mobug_not_brown)
print("#### Mobug Color == Blue ###")
df_mobug_blue = df_mobug.loc[df_mobug['Color'] == 'Blue']
print(len(df_mobug_blue))
print(df_mobug_blue)
print("#### Lobug Color == Blue ###")
df_lobug_blue = df_lobug.loc[df_lobug['Color'] == 'Blue']
print(len(df_lobug_blue))
print(df_lobug_blue)
print("#### Mobug Color == Green ###")
df_mobug_green = df_mobug.loc[df_mobug['Color'] == 'Green']
print(len(df_mobug_green))
print(df_mobug_green)
print("#### Lobug Color == Green ###")
df_lobug_green = df_lobug.loc[df_lobug['Color'] == 'Green']
print(len(df_lobug_green))
print(df_lobug_green)
print("#### Mobug Length < 17 ###")
df_mobug_length_less_than_17 = df_mobug.loc[df_mobug['Length (mm)'] < 17]
print(len(df_mobug_length_less_than_17))
print(df_mobug_length_less_than_17)
print("#### Lobug Length < 17 ###")
df_lobug_length_less_than_17 = df_lobug.loc[df_lobug['Length (mm)'] < 17]
print(len(df_lobug_length_less_than_17))
print(df_lobug_length_less_than_17)
print("#### Mobug Length < 20 ###")
df_mobug_length_less_than_20 = df_mobug.loc[df_mobug['Length (mm)'] < 20]
print(len(df_mobug_length_less_than_20))
print(df_mobug_length_less_than_20)
print("#### Lobug Length < 20 ###")
df_lobug_length_less_than_20 = df_lobug.loc[df_lobug['Length (mm)'] < 20]
print(len(df_lobug_length_less_than_20))
print(df_lobug_length_less_than_20)


def two_group_ent(first, tot):                        
    return -(first/tot*np.log2(first/tot) +           
             (tot-first)/tot*np.log2((tot-first)/tot))

tot_ent = two_group_ent(10, 24) # Mobug, Total (Mobug+Lobug)
# Mobug Length < 20 + Mobug Length < 17 = 15 / 24 * Lobug Length < 20 + Lobug Length < 17 = 11 / 
# Mobug Length < 20 + Mobug Length < 17 = 15                 
#  + Mobug Length < 17 + Lobug Length < 17  = 9 / total 24 * Mobug Length, Lobug Legth + Mobug Length
g17_ent = 15/24 * two_group_ent(11,15) + 9/24 * two_group_ent(6,9)              
g20_ent = 15/24 * two_group_ent(11,15) + 17/24 * two_group_ent(9,17)
color_green = 16/24 * two_group_ent(20,16) + 8/24 * two_group_ent(2,8)
color_blue = 16/24 * two_group_ent(20,16) + 10/24 * two_group_ent(4,10)
color_brown = 16/24 * two_group_ent(20,16) + 6/24 * two_group_ent(4,10)
answer = tot_ent - g17_ent 
answer2 = tot_ent - g20_ent
answer3 = tot_ent - color_green
answer4 = tot_ent - color_blue
answer5 = tot_ent - color_brown

print(f"g17 {answer} ")
print(f"g20 {answer2} ")
print(f"green {answer3} ")
print(f"blue {answer4} ")
print(f"brown {answer5} ")