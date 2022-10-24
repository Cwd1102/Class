# creates a list of students in this particular class
# input: none
# output: list of students in a class: lastname, firstnam
def fill_roster():
    newRoster = list()
    newRoster.append("Hamilton, Eric") #early, signed in, signed out
    newRoster.append("Lupoli, Shawn") #early, signed in, signed out
    newRoster.append("Allgood, Nick") #late, signed in
    newRoster.append("Arsenault, Al") #no show
    newRoster.append("Aja, Richard") #early, signed in, signed out
    newRoster.append("Asad, Hamza") #late, signed in
    newRoster.append("Barot, Bharg") #early, signed in, signed out
    newRoster.append("Cajudoy, Janeiyah") #late, signed in, signed out
    newRoster.append("Chen, Kevin") #early, signed in, signed out
    newRoster.append("Cleary, Miranda") #late, signed in, signed out
    newRoster.append("Diaz, Sergio") #early, signed in, signed out
    newRoster.append("Dove, Ellie") #late, signed in
    newRoster.append("Dulce, Alexander John") #early, signed in, signed out
    newRoster.append("Gaither, Oliver") #early, signed in, signed out
    newRoster.append("Gunaseelan, Adith") #late, signed in, signed out
    newRoster.append("Hambrecht, Matt") #early, signed in, signed out
    newRoster.append("Hassanein, Magdi") #early, signed in, signed out
    newRoster.append("Henderson, Sean") #early, signed in, signed out
    newRoster.append("Ilamni, Jazlyn") #late, signed in, signed out
    newRoster.append("Jacob, Ify") #late, signed in
    newRoster.append("Lare, George") #early, signed in, signed out
    newRoster.append("Mammel, Sammie") #no show
    newRoster.append("Odeseye, Ayodele")  #early, signed in, signed out
    newRoster.append("Ortiz, Joseph") #early, signed in, signed out
    newRoster.append("Othman, Youssef") #early, signed in, signed out
    newRoster.append("Pham, Matthew") #late, signed in, signed out
    newRoster.append("Premkumar, David") #early, signed in, signed out
    newRoster.append("Robinson, Edward") #early, signed in, signed out
    newRoster.append("Tang, Hieu") #late, signed in
    newRoster.append("Turner, Jessica") #early, signed in, signed out
    newRoster.append("Vantran, Luke")  #late, signed in, signed out
    newRoster.append("Vedasendur Senthilvel, Pranav") #late, signed in, signed out
    newRoster.append("Yahaya, Idris") #early, signed in, signed out
    newRoster.append("Zheng, Kelvin") #early, signed in, signed out
    newRoster.append("Zhuang, Michael") #late, signed in
    newRoster.append("Sheldon, Simon") #no show

    return newRoster

# creates a list of attendance data in this particular class. 
# Notice, students SHOULD be listed twice, signing in, and signing out
# input: none
# output: list of students in a class: lastname, firstname
def fill_attendance_data():
    newData = list()

    #early people
    newData.append("Chen, Kevin, 08:55:34, 10/20/2022") 
    newData.append("Diaz, Sergio, 08:55:44, 10/20/2022") 
    newData.append("Dulce, Alexander John, 08:55:54, 10/20/2022") 
    newData.append("Gaither, Oliver, 08:56:10, 10/20/2022") 
    newData.append("Hambrecht, Matt, 08:56:11, 10/20/2022") 
    newData.append("Hassanein, Magdi, 08:56:12, 10/20/2022") 
    newData.append("Henderson, Sean, 08:56:13, 10/20/2022") 
    newData.append("Lare, George, 08:56:14, 10/20/2022") 
    newData.append("Hamilton, Eric, 08:50:34, 10/20/2022") 
    newData.append("Lupoli, Shawn, 08:55:14, 10/20/2022") 
    newData.append("Aja, Richard, 08:55:14, 10/20/2022") 
    newData.append("Barot, Bharg, 08:55:24, 10/20/2022")
    newData.append("Odeseye, Ayodele, 08:57:14, 10/20/2022")  
    newData.append("Ortiz, Joseph, 08:57:15, 10/20/2022") 
    newData.append("Othman, Youssef, 08:57:16, 10/20/2022") 
    newData.append("Premkumar, David, 08:57:17, 10/20/2022") 
    newData.append("Robinson, Edward, 08:57:18, 10/20/2022") 
    newData.append("Turner, Jessica, 08:57:19, 10/20/2022")
    newData.append("Yahaya, Idris, 08:57:20, 10/20/2022") 
    newData.append("Zheng, Kelvin, 08:57:21, 10/20/2022") 

    #late people
    newData.append("Allgood, Nick, 09:02:14, 10/20/2022")  
    newData.append("Asad, Hamza, 09:03:14, 10/20/2022")
    newData.append("Cajudoy, Janeiyah, 09:04:14, 10/20/2022")
    newData.append("Cleary, Miranda, 09:05:14, 10/20/2022") 
    newData.append("Dove, Ellie, 09:06:14, 10/20/2022")
    newData.append("Gunaseelan, Adith, 09:07:14, 10/20/2022") 
    newData.append("Ilamni, Jazlyn, 09:02:15, 10/20/2022")
    newData.append("Jacob, Ify, 09:02:16, 10/20/2022")
    newData.append("Pham, Matthew, 09:02:17, 10/20/2022")
    newData.append("Tang, Hieu, 09:02:18, 10/20/2022")
    newData.append("Vantran, Luke, 09:02:21, 10/20/2022")
    newData.append("Vedasendur Senthilvel, Pranav, 09:02:22, 10/20/2022")
    newData.append("Zhuang, Michael, 09:02:23, 10/20/2022")

    #signed out
    newData.append("Aja, Richard, 09:15:34, 10/20/2022")
    newData.append("Barot, Bharg, 09:16:34, 10/20/2022")  
    newData.append("Cajudoy, Janeiyah, 09:17:34, 10/20/2022") 
    newData.append("Chen, Kevin, 09:18:34, 10/20/2022") 
    newData.append("Cleary, Miranda, 09:19:34, 10/20/2022") 
    newData.append("Diaz, Sergio, 09:15:35, 10/20/2022")
    newData.append("Dulce, Alexander John, 09:15:36, 10/20/2022") 
    newData.append("Gaither, Oliver, 09:15:37, 10/20/2022") 
    newData.append("Gunaseelan, Adith, 09:15:38, 10/20/2022") 
    newData.append("Hambrecht, Matt, 09:15:39, 10/20/2022") 
    newData.append("Hassanein, Magdi, 09:01:34, 10/20/2022") 
    newData.append("Henderson, Sean, 09:02:34, 10/20/2022") 
    newData.append("Ilamni, Jazlyn, 09:03:34, 10/20/2022") 
    newData.append("Lare, George, 09:04:34, 10/20/2022") 
    newData.append("Odeseye, Ayodele, 09:05:34, 10/20/2022") 
    newData.append("Ortiz, Joseph, 09:06:34, 10/20/2022") 
    newData.append("Othman, Youssef, 09:07:34, 10/20/2022")
    newData.append("Pham, Matthew, 09:08:34, 10/20/2022") 
    newData.append("Premkumar, David, 09:09:34, 10/20/2022") 
    newData.append("Robinson, Edward, 09:10:34, 10/20/2022") 
    newData.append("Turner, Jessica, 09:11:34, 10/20/2022") 
    newData.append("Vantran, Luke, 09:12:34, 10/20/2022") 
    newData.append("Vedasendur Senthilvel, Pranav, 09:13:34, 10/20/2022") 
    newData.append("Yahaya, Idris, 09:14:34, 10/20/2022") 
    newData.append("Zheng, Kelvin, 09:16:34, 10/20/2022") 
    newData.append("Hamilton, Eric, 09:08:24, 10/20/2022")
    newData.append("Lupoli, Shawn, 09:20:14, 10/20/2022")
    
    # Nick never signed out
    # newData.append("Allgood, Nick, 09:10:14, 10/20/2022")     
    #notice, no Al
    
    return newData
