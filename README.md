# IT2005-CallforHelp_SCDFXIBM
A group of year 1 poly students trying to gain some experience in the field.
# Call for Help
## Short Description
### What's the problem?

With the increasingly aging population and a growing segment of vulnerable populations in mind, how might we leverage analytics for better sense-making to be alerted at the onset of incidents which require emergency response and mobilise CFRS for effective early intervention especially to the vulnerable population?

### How can technology help?

With the advancement of technology especially in the AI and machine learning fields, we can make use of computer vision and biosensors to detect if someone or somewhere is suffering from an emergency.

### The Idea

We will be making use of codes to craft an application to reduce response time when it comes to emergency situations by alerting CFRs and professionals.

## Pitch Proposal



## The Architecture

![Solution Architecture](solArch.png)

2 Situations it will mainly be used:

1. When the user is alone at home
    1. The User's heart rate will constantly feedback to the Python Code via the App.
    2. Python Code will return whether it is an abnormal value.
    3. If it is abnormal, App shows alert to user.
    4. This repeats until there are consecutive abnormal values.
    5. If there is, then App will prompt a check to see if user is okay, if no response for 1 minute, other users will receives a ping and dials 995.

2. When someone collapses in public and user is CFR
    1. User will take photo or video of situation via the App.
    2. The data will then be received by IBM Watson and sent to Computer Vision to analyse the data.
    3. If the data is a picture or video of a patient it will get the patient's health conditions from SingHealth which will be sent back to user via App.
    4. Instructions will also be given to user.
    5. If data is a picture or video of a fire the fire will categorized by severity and depending on severity will give instructions to user where possible.

## Long Description
[More details are available here](https://docs.google.com/document/d/1nvfI0ENHBwIohhQT6EjDXGNtcbFp9wNmVMIBolRpPyw/edit)
