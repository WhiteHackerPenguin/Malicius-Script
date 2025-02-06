This script will be launched in the victim's machine. Before that, make sure you have connection to that machine, and in you Kali, use Netcat to be waiting for the port selected in the script.
---
                                                                                        DEFAULT
                                                                                          443
---

*COMMAND*
sudo nc -nlvp 443


This will initialize a process of listening, from you Atackers' Machine. Then, launch the malicius script in the Target 's machine. You will receive a Reverse Shell, with the minimum privileges
