#Javier Castaneda 
#410721322
#Data Science Final Project         Date:6/15/2022
#Created a system for users to check their stats from different games.
#Currently only 3 games are available to check(Valorant, Apex Legends, League of Legends)
#if you do not have an account for any of these games u can use the following usernames for testing
    #Valorant: Shadow0Night0#6666
    #League: Shadow0Night0  
    #Apex: Shadow0Night0
#note that the system sometimes give trouble, this is due to the webpage, so sometimes u just need to sumbit again to get the results.


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
from tkinter import *
import tkinter as tk

#fucntion to get the stats from valorant
def valorant_stats(username):
    #this first part is just using selenium to get to the desired page where all the stats are listsed
    #fuctions are mostly the same for this part
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=PATH)
    html = driver.page_source
    soup = BeautifulSoup(html)

    driver.get("https://tracker.gg/")
    driver.implicitly_wait(5)
    driver.find_element_by_link_text("Valorant").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//*[@id='app']/div[2]/div[2]/div/main/div[3]/div/div[1]/div/div/div[1]/div[2]/div[1]/form/input").send_keys(username, Keys.ENTER)

    

    driver.implicitly_wait(5)
    url = driver.page_source

    stats = []
    stats.append("Valorant")
    #dataframe where i will store the stats, future idea is to be able to combine all stats and save it in a csv file
    df = pd.DataFrame(columns=['Game','Kills', 'HeadShots', 'Deaths', 'Assists','K/D'])
    #df.index = df.index.str.decode('utf_8_sig')
    sleep(5)
    html = driver.page_source
    driver.close()
    #Usinge beautifulsoup on the page that has all the stats listed
    soup = BeautifulSoup(html, 'html.parser')
    sleep(5)
    try:
        div = soup.find("div", {"class": "main"})

        for link in div.findAll("div", {"class": "stat align-left expandable"}):
            temp = link.find("span", {"class": "value"}).text
            stats.append(temp)
        
    except:
        final_df = pd.DataFrame(df)
        return final_df

    try:
        div = soup.find("div", {"class": "trn-profile-highlighted-content__stats"})
        div2 = div.find("div", {"class": "stat"})
        temp2 = div2.find("span", {"class": "stat__value"}).text
    except:
        temp2 = "NA"
    del stats[5:]
    stats.append(temp2)
    #stats.append(temp2)
    df = df.append(pd.Series(stats, index=df.columns[:len(stats)]), ignore_index=True)

    final_df = pd.DataFrame(df)
    return final_df

#fucntion to get the stats from Apex Legends  
def apex_stats(username):
    PATH = "C:\Program Files (x86)\chromedriver.exe"

    driver = webdriver.Chrome(executable_path=PATH)
    html = driver.page_source
    soup = BeautifulSoup(html)

    driver.get("https://tracker.gg/")
    driver.implicitly_wait(5)
    driver.find_element_by_link_text("Apex Legends").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//*[@id='app']/div[2]/div[2]/div/main/div[3]/div/div[1]/div/div/div[1]/div[2]/div[1]/form/input").send_keys(username, Keys.ENTER)

    driver.implicitly_wait(5)
    url = driver.page_source

    stats = []
    stats.append("Apex Legends")
    df = pd.DataFrame(columns=['Game','Level', 'Kills', 'S9 Wins', 'S9 Kills','Favorite Legend'])
    #df.index = df.index.str.decode('utf_8_sig')
    sleep(5)
    html = driver.page_source
    driver.close()
    soup = BeautifulSoup(html, 'html.parser')
    sleep(5)
    #unlike the Valorant funtion, sometime the data is all over the place, so for Apex legends its a little more of a mess
    #the data were in different sub categories
    try: 
        div = soup.find("div", {"class": "giant-stats"})
        for link in div.findAll("div", {"class": "stat align-left giant expandable"}):
            temp = link.find("span", {"class": "value"}).text
            stats.append(temp)
        div = soup.find("div", {"class": "main"})
        for link in div.findAll("div", {"class": "stat align-left expandable feature-hint"}):
            temp = link.find("span", {"class": "value"}).text
            stats.append(temp)
        div = soup.find("div", {"class": "stat align-left expandable"})
        temp = div.find("span", {"class": "value"}).text
        stats.append(temp)

        legend = soup.find("div", {"class": "legend__name"}).text
        stats.append(legend)
    except:
        final_df = pd.DataFrame(df)
        return final_df
        

    df = df.append(pd.Series(stats, index=df.columns[:len(stats)]), ignore_index=True)

    final_df = pd.DataFrame(df)
    return final_df

#fucntion to get the stats from League of Legends
def league_stats(username):
    PATH = "C:\Program Files (x86)\chromedriver.exe"

    driver = webdriver.Chrome(executable_path=PATH)
    html = driver.page_source
    soup = BeautifulSoup(html)

    driver.get("https://tracker.gg/")
    driver.implicitly_wait(5)
    driver.find_element_by_link_text("League of Legends").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//*[@id='app']/div[2]/div[2]/div/main/div[3]/div/div[1]/div/div/div[1]/div[2]/div[1]/form/input").send_keys(username, Keys.ENTER)
    driver.implicitly_wait(5)


    url = driver.page_source

    stats = []
    stats.append("League of Legends")
    df = pd.DataFrame(columns=['Game','Overall KD', 'Average K/D/A', 'CS/Min', 'Vision Score','Win Rate'])
    #df.index = df.index.str.decode('utf_8_sig')
    sleep(5)
    html = driver.page_source
    driver.close()
    soup = BeautifulSoup(html, 'html.parser')
    sleep(5)
    try: 
        div = soup.find("div", {"class": "giant-stats"})
        for link in div.findAll("div", {"class": "stat align-left giant expandable"}):
            temp = link.find("span", {"class": "value"}).text
            stats.append(temp)
    except:
        final_df = pd.DataFrame(df)
        return final_df

    try:
        div = soup.find("div", {"class": "trn-profile-highlighted-content__stats"})
        div2 = div.find("div", {"class": "stat"})
        div2.small.decompose()
        temp2 = div2.find("span", {"class": "stat__value"}).text
        temp2 = temp2.strip().replace("  ","")
    except:
        temp2 = ("NA")

    stats.append(temp2)

    df = df.append(pd.Series(stats, index=df.columns[:len(stats)]), ignore_index=True)

    final_df = pd.DataFrame(df)
    return final_df


def determine(username, Game):
    pass

#function that is called when the submit button is clicked
def click():
    #get the info from the user inputs
    user = user_entry.get()
    g = variable.get()
    #determine what game the user wants
    if (g == "Valorant"):
        df = (valorant_stats(user))
        #displays result from the game and username the user entered 
        if df.empty == True:
            game_name.config(text = "No user found" )
        else:
            header = list(df.columns.values)
            #game_name.config(text=header[0])
            game_stat1_head.config(text = header[1])
            game_stat2_head.config(text = header[2])
            game_stat3_head.config(text = header[3])
            game_stat4_head.config(text = header[4])
            game_stat5_head.config(text = header[5])
            info = df.iloc[0]
            game_name.config(text = info[0])
            game_stat1_data.config(text =info[1])
            game_stat2_data.config(text =info[2])
            game_stat3_data.config(text =info[3])
            game_stat4_data.config(text =info[4])
            game_stat5_data.config(text =info[5])
    elif (g == "Apex Legends"):
        df = (apex_stats(user))
        if df.empty == True:
            game_name.config(text = "No user found" )
        else:
            header = list(df.columns.values)
            #game_name.config(text=header[0])
            game_stat1_head.config(text = header[1])
            game_stat2_head.config(text = header[2])
            game_stat3_head.config(text = header[3])
            game_stat4_head.config(text = header[4])
            game_stat5_head.config(text = header[5])
            info = df.iloc[0]
            game_name.config(text = info[0])
            game_stat1_data.config(text =info[1])
            game_stat2_data.config(text =info[2])
            game_stat3_data.config(text =info[3])
            game_stat4_data.config(text =info[4])
            game_stat5_data.config(text =info[5])
    elif (g == "League of Legends"):
        df = league_stats(user)
        if df.empty == True:
            game_name.config(text = "No user found" )
        else:
            header = list(df.columns.values)
            #game_name.config(text=header[0])
            game_stat1_head.config(text = header[1])
            game_stat2_head.config(text = header[2])
            game_stat3_head.config(text = header[3])
            game_stat4_head.config(text = header[4])
            game_stat5_head.config(text = header[5])
            info = df.iloc[0]
            game_name.config(text = info[0])
            game_stat1_data.config(text =info[1])
            game_stat2_data.config(text =info[2])
            game_stat3_data.config(text =info[3])
            game_stat4_data.config(text =info[4])
            game_stat5_data.config(text =info[5])




OPTIONS = [
"Valorant",
"Apex Legends",
"League of Legends"
]
REGION = [
"North America",
"EU West",
"EU East/Nordic",
"Latin America (North)",
"Latin America (South)",
"Oceania",
"Korea",
"Japan",
"Russia"
]
#this is the GUI using tkinter
#note that this is the first time ive used a GUI in python so it was a learning experience 

#defining window, giving a title and bg
window = tk.Tk()
window.configure(background="Gray")
window.title("Stats Checker")

window.geometry("500x500+10+10")

#defining the label and the input 
username = tk.Label(window, text="Username", background="Gray", fg="White",font=('Times New Roman',14,'bold'))
user_entry = tk.Entry(background="Gray",fg="White")
username.place(x=75, y=50)
user_entry.place(x=200, y=55)

#creating a drop down, for users to select game
game = tk.Label(window, text="Select Game", background="Gray",fg="White",font=('Times New Roman',14,'bold'))
variable = StringVar(window)
variable.set(OPTIONS[0]) # default value
game_entry = OptionMenu(window, variable, *OPTIONS)
game_entry.config(background="Gray",fg="White",font=('Times New Roman',14,'bold'))
game.place(x=75, y=100)
game_entry.place(x=200, y=100)

#Display data headers 
#out_label= tk.Label(window,text ="Out",background="Gray",fg="White",font=('Times New Roman',14,'bold'))
#out_label.place(x=50, y=200)
game_name = tk.Label(window,background="Gray",fg="White",font=('Times New Roman',14,'bold'))
game_stat1_head = tk.Label(window,background="Gray",fg="Black",font=('Times New Roman',14,'bold'))
game_stat2_head = tk.Label(window,background="Gray",fg="Black",font=('Times New Roman',14,'bold'))
game_stat3_head = tk.Label(window,background="Gray",fg="Black",font=('Times New Roman',14,'bold'))
game_stat4_head = tk.Label(window,background="Gray",fg="Black",font=('Times New Roman',14,'bold'))
game_stat5_head= tk.Label(window,background="Gray",fg="Black",font=('Times New Roman',14,'bold'))
game_name.place(x=50, y=200)
game_stat1_head.place(x=50, y=250)
game_stat2_head.place(x=50, y=325)
game_stat3_head.place(x=200, y=250)
game_stat4_head.place(x=200, y=325)
game_stat5_head.place(x=350, y=250)

#display user stats
game_stat1_data = tk.Label(window,background="Gray",fg="cyan",font=('Times New Roman',14,'bold'))
game_stat2_data = tk.Label(window,background="Gray",fg="cyan",font=('Times New Roman',14,'bold'))
game_stat3_data = tk.Label(window,background="Gray",fg="cyan",font=('Times New Roman',14,'bold'))
game_stat4_data = tk.Label(window,background="Gray",fg="cyan",font=('Times New Roman',14,'bold'))
game_stat5_data= tk.Label(window,background="Gray",fg="cyan",font=('Times New Roman',14,'bold'))
game_stat1_data.place(x=50, y=275)
game_stat2_data.place(x=50, y=350)
game_stat3_data.place(x=200, y=275)
game_stat4_data.place(x=200, y=350)
game_stat5_data.place(x=350, y=275)


#submit button
sub = tk.Button(window, text="Submit", command=click,background="Gray",fg="White",font=('Times New Roman',14,'bold'))
sub.place(x=200, y=150)


window.mainloop()