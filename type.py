import time
import keyboard
import pyautogui


pages = [
    ''' Carothean Scripture


    
        
These are the true accounts of our god Carotus. He is the true and only God.
    


    ------Carotism------''',
    '''Chapter 1: In the Beginning
    1.1 In the vast world of Minecraft, where blocks and mobs dwell, there existed a humble vegetable known as the carrot.
    1.2 And lo, the carrot was bestowed with powers beyond compare, for it possessed the ability''',
    '''and nourish those who consumed it.
    1.3 And so it was, from the very beginning, that the carrot reigned supreme, the epitome of all that was good and holy in the Minecraft realm.''',
    '''Chapter 2: The Power of Carrot
    2.1 The people of Minecraft soon realized the wondrous properties of the carrot, for it provided sustenance and healing like no other.
    2.2 Its bright orange hue shone with the radiance of the sun, and its crunchy''',
    '''texture brought joy to the hearts of all who tasted it.
    2.3 The carrot became a symbol of hope and prosperity, a beacon of light in the darkest of caves.''',
    '''Chapter 3: The Quest for Carrot
    3.1 Many brave adventurers set forth on quests to acquire the almighty carrot, for they knew its power would aid them in their journeys.
    3.2 They battled fearsome creatures, delved into treacherous dungeons,''',
    '''and braved the perils of the Nether, all in search of the glorious carrot.
    3.3 For they understood that with carrot by their side, no challenge was too great, no obstacle insurmountable.''',
    '''Chapter 4: Carrot's Divine Wisdom
    4.1 As the people of Minecraft revered the carrot, they sought its divine wisdom, for they believed it held the secrets of the universe.
    4.2 They listened closely to the whispers of the carrot, for it spoke''',
    '''words of truth and guidance, leading them to victory and prosperity.
    4.3 The carrot became their compass, their guiding light, their ultimate source of enlightenment.''',
    '''Chapter 5: The Carrot's Commandments
    5.1 And so, the carrot spoke unto the people, imparting its sacred commandments for all to follow:
    5.2 "Thou shalt cherish the carrot above all other vegetables, for it is the true gift of the Minecraft gods."''',
    '''5.3 "Thou shalt share the carrot's bounty with thy fellow players, for the joy of carrot is meant to be shared."
    5.4 "Thou shalt never underestimate the power of carrot, for it holds the key to victory and sustenance."''',
    '''Chapter 6: The Carrot's Legacy
    6.1 And thus, the word of carrot spread throughout the land, bringing laughter and mirth to all who heard it.
    6.2 The people of Minecraft built grand monuments in honor of the carrot, crafting elaborate carrot statues and''',
    '''carrot-shaped buildings.
    6.3 For they knew that in the realm of Minecraft, the carrot was not just a vegetable but a symbol of unity, joy, and boundless possibilities. 
    ''',
    '''Chapter 7: Advanced Diplomatic Action
    7.1 As the people of Minecraft encountered challenges and conflicts, they sought peaceful resolutions through Advanced Diplomatic Action (ADA).
    7.2 Some encountered a group known as the People of the Carrot, who''',
    '''were known for their unwavering resilience and unyielding attacks.
    7.3 The People of the Carrot, ever steadfast in their ways, refused to surrender and continued their relentless assaults.
    7.4 In the face of such unrelenting adversaries, the people of Minecraft''',
    '''turned to ADA as a means to foster understanding and seek a resolution.''',
    '''Chapter 8: The Carrot Negotiations
    8.1 The brave emissaries of Minecraft embarked on a journey to meet with the People of the Carrot, seeking a peaceful accord.
    8.2 They brought gifts of golden carrots and peaceful intentions, hoping to convey their''',
    '''desire for harmony and cooperation.
    8.3 Through patient dialogue and diplomatic finesse, the emissaries aimed to find common ground amidst the chaos.''',
    ''' Chapter 9: The Power of Carrot Diplomacy
    9.1 The emissaries highlighted the shared appreciation for the power of the carrot, emphasizing its ability to nourish and sustain all.
    9.2 They emphasized the futility of endless conflict, proposing a vision of unity where''',
    '''the People of the Carrot and others coexist in harmony.
    9.3 Through the power of carrot diplomacy, they aimed to forge a path of peace and cooperation in the Minecraft realm.''',
    '''Chapter 10: The Carrot's Wisdom Prevails
    10.1 Slowly but steadily, the People of the Carrot began to listen to the voice of reason and the power of ADA.
    10.2 They recognized the futility of constant attacks, realizing that peace''',
    '''and collaboration could lead to a brighter future.
    10.3 The Carrot's divine wisdom guided them to choose a path of understanding, putting an end to the cycle of aggression.''', '''Carotus' Last Acount I, Carotus, the regal ruler of the carrot domain, speak to you through this message. Listen closely for my instructions, which will be delivered by Makashi, the Earth's only Carrothean Sage. Makashi holds the power to appoint Carrothean Ministers.''',
    '''Stay strong and unwavering in these challenging times. Embrace Carrotism's essence, uniting as one to overcome any obstacle. Makashi, our esteemed Carrothean Sage, appoints Carrothean Ministers who will guide and lead our community with righteousness.
    ''',
    '''Respect and honor Makashi's decisions, for they possess divine wisdom. Follow their instructions, as they are chosen to uphold Carrotism's sacred principles.''',
    '''Stay steadfast, my faithful followers. Through Makashi's wisdom, you will receive the guidance needed for this journey.'''
]


def type_string(string):
    # Adjust the delay between keypresses if needed
    keyboard.write(string, delay=0)


# Locate the image on the screen
print("Starting in 5 seconds...")
time.sleep(5)
print("Starting...")
image_location = pyautogui.locateOnScreen('./image.png')

if image_location is not None:
    # Get the center coordinates of the image
    image_center = pyautogui.center(image_location)

    # Move the mouse to the center of the image
    pyautogui.moveTo(image_center.x, image_center.y, duration=0.2)

    for i in range(len(pages)):
        type_string(pages[i])
        # click the mouse to go to the next page
        pyautogui.click()
        time.sleep(0.5)


else:
    print("Image not found on the screen.")
    print("Move mouse to next page button, you have 5 seconds...")
    time.sleep(1)
    print("4...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Starting...")
    for i in range(len(pages)):
        type_string(pages[i])
        # click the mouse to go to the next page
        pyautogui.click()
        time.sleep(0.5)
