
# RoboGram
[![MIT license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/lbgrand/RoboGram/LICENSE)
[![built with Selenium](https://img.shields.io/badge/built%20with-Selenium-yellow.svg)](https://github.com/SeleniumHQ/selenium)
[![built with Python3](https://img.shields.io/badge/built%20with-Python3-red.svg)](https://www.python.org/)

### Script that automates the promotion of your Intagram account (make Likes, Comments and Followers)

**This is originally the project of Tim Grossmann**
I made some changes and add new functions, so it meets my needs. You can use my project freely for your purposes as well as original one (in this case head over to https://github.com/timgrossmann/InstaPy/ ). I appreciate the amazing work made by Tim!

**If you have some issues**
Write me on lbgrand@rambler.ru or drop me a direct message on Instagram @gordeevandrei. You can also check out https://github.com/timgrossmann/InstaPy/ if you want to know how it works in all details.

**Disclaimer**: Please Note that this is a research project. I am by no means responsible for any usage of this tool. Use on your own behalf. I’m also not responsible if your accounts get banned due to extensive use of this tool.

### Social

#### [VK](https://vk.com/andrewgordeev) | [Twitter](https://twitter.com/andregordeev) | [Instagram](https://www.instagram.com/gordeevandrei/) 

[![paypal](https://img.shields.io/badge/-PayPal-blue.svg)](https://www.paypal.me/lbgrand)

Table of Contents
=================

* [What can you do with this program?](#what-can-you-do-with-this-program?)
* [Installation on Windows and Mac](#installation-on-windows-and-mac)
* [Installation on Linux](#installation-on-linux)
* [Setup and start](#setup-and-start)

## What can you do with this program?
This is an automation script that will log in with your Instagram account and do some promotion work for you. What does it exactly do? It takes hashtags that you give it, seaches for pictures marked with one of those hashtags and likes, comments them or follows their owners. You can set the number of likes, comments and follows your bot should do. You also must choose some hashtags, so that bot can seach posts with them. I would suggest you to take hashtags which describes your own interests and what your account is about. 

## Installation on Windows and Mac

At this point of time I didn't find an efficient way to install this programm on Windows/Mac. That's why we will simulate Linux on your computer and then install it. But don't be afraid, it won't be too hard and you will become new interesting experience and some cool benefits as well. If I see positive feedbacks and interest I will give my best to make the installation user friendlier and simpler.

1. First step is to download VirtualBox from https://www.virtualbox.org/wiki/Downloads 
Just choose the right version for your operating system and download it. This software makes it possible for you to simulate another operating systems like Linux, so it's just overall helpful tool on your PC.

2. Now download operating system Ubuntu to install it on VirtualBox. You can find it here: https://www.ubuntu.com/download/desktop

3. Ok, that was easy. The third step is a bit trickier, but it's sometimes cool to feel yourself like a hacker =)
So to install Ubuntu we must enable virtualization on your computer. To make it happen first find out which key you need to press in order to access the BIOS. It's often one of  F1, F2, or F3 keys, Esc key or Delete key, but you can google and find the right key for your computer brand.
When you find it restart you computer and press that key many times during loading process. Then you should see BIOS window and can navigate arrow keys. Here you schould search for option Virtualization or Virtualization Technology. I find it to be in System Configurations, but that could be different for you.
After that press Enter and enable it. You're done. Last but not least press Esc and save changes.

4. Now your computer should start Windows/MacOS and we can install Linux. This step won't be difficult at all. So just start VirtualBox, click Create, type in Ubuntu as name, choose Linux as Type and Ubuntu (64-bit) as Version.
Click next. Choose 2048 MB memory size and click next again. Then just click though (with Next or Create) all next windows.

5. Good, we're almost done. Start your brand new virtual machine (you will see it on the left of the window). Here click directory symbol and find Ubuntu that you downloaded in step 2. Wait a bit and then click Install Ubuntu. In the next window tick both checkboxes.
Then the intallation should be pretty intuitive, just proceed with all standars setting and answer some simple requests. If you stall and need some help look at the page https://tutorials.ubuntu.com/tutorial/tutorial-install-ubuntu-desktop#4 .
Please note your password, you will need it later on.

Congratulation! Now you have Ubuntu (Linux) installed and can proceed with the next section ```Installation on Linux```. Only few step are left for my program to start working for you!

## Installation on Linux 

The installation of this programm on Linux will take little time and effort from you. So go ahead and get it!

1. Now you will become a real programmer for a bit and use Command Line! Just kidding =) I just want you to open Terminal and type in some commads that I will give you later.
So click on Dash (the Ubuntu icon in the upper-left corner), type "terminal", and select the Terminal application from the results that appear. 

2. Let's start coding! Type in (or copy-paste) following lines, pressing Enter in the end of each line (type in your password when you get the request):
```bash
sudo apt-get install git
git clone https://github.com/lbgrand/RoboGram
cd RoboGram/scripts/
sudo chmod u+x unix.sh
./unix.sh
```
Now you see how the installation run. When you get grey windows with language setting just push Enter two times, and it will proceed.
In the end you will see the lines:
```bash
Setup is completed.
Press any key to continue...
```
Press Enter, close the Terminal and it's all you need to do! Congratulation! The installation is over, so we can configure and start the programm. Proceed to read about it in the next section.

## Setup and start

Okey, you made it so far! Let's get to the last steps before you can enjoy this program. We need to configure it to work with your Instagram account and then start it.

1. Configuration: Under the Dash (the Ubuntu icon in the upper-left corner) you will find Files icon, click it. 
In the opened window go in the RoboGram folder and open quickstart.py. There find following lines:
```python
######################################
insta_username = 'your login'
insta_password = 'your password'
number_of_likes = 1200
number_of_follows = 0
number_of_comments = 250 
tags = ['student', 'nature', 'river', 'forest', 'tree', 'lake', 'sea', 'ocean', 'sky', 'travel', 'cloud', 'stone', 'water', 'city', 'country', 'mountain']
######################################
```
Here replace ```your login``` in quotation marks with your Instagram login and ```your password``` in quotation marks with your Instagram password.
Then edit the number of likes, comments and number of people the bot schould follow in one session (the next session it will unfollow those people and follow the next number_of_follows people).
I don't promote to use following function because I don't like people being upset about it, and I also hate to see unwanted accounts in my feed.
But if you want then use it. Just don't go over 100 follows a day. For likes 1200 a day is the upper limit (as well as 250 comments) that you can safely use every day. 
Don't go over it since you will be banned. If you new to Instagram then reduce all numbers in two times (i.e. 600/50/125). Now edit tags. 
You can add and/or remove tags. Just make sure you use the seme form as I do in example above. I suggest to take the tags which describes your interests and account best.
And that's it. Close the editor window saving changes and configuration is done. You don't need to do this step ever again.    

2. Start: Now we're ready to start the program! You should be in the RoboGram folder (as we made in first step).
Make right click over white empty spacea and select ```Open in Termimal```. You will see Terminal window you're already familiar with. Here type in: 
```bash
sudo python quickstart.py
```
or if it doesn't work:
```bash
sudo python3 quickstart.py
```

If the program starts, loads Instagram page, but doesn't go anywhere further please check out you Google Chrome language setup. 
If the default language of browser isn't English then follow this guide https://www.lifewire.com/change-default-languages-in-google-chrome-4103615 
to change it to English.

Now the program will be started and you can enjoy its work and of course benefits. Fill free to send me a message if you like my work or have an issue!

