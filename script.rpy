# The script of the game goes in this file.
define config.top_layers = [ 'waveui' ]
define gui.text_width = 900

# Declare styles used by this game and python initiations.

init python:
    style.n_text = Style(style.default)
    style.n_text.color = "#1E8449"
    
    def hide_wave():
        renpy.hide('wave', layer='waveui')
        return
    
    def change_wave(image_name):
        
        if renpy.showing('wave', layer='waveui'):
            renpy.hide('wave', layer='waveui')
        
        if image_name != 'wave gray':
            renpy.music.set_volume(0.2, delay=0, channel='music')
            renpy.show(image_name, at_list=[right], layer='waveui') 
            renpy.play("Sine2Sec.mp3")
            renpy.music.set_volume(1.0, delay=7, channel='music')
        else:
            renpy.show(image_name, at_list=[right], layer='waveui')
            return
        
        return
    
    def freq_sound(sound_name):
        
        renpy.music.set_pause(True, channel='music')
        
        if sound_name == "green":
            renpy.play("Static1.mp3")
            store.response = "Huh? Dang, just static. I can't seem to connect."
        elif sound_name == "purple_mina":
            renpy.play("Lock2.mp3")
            store.response = "What is this sound? Maybe I could use this?"
        elif sound_name == "red_mina":
            renpy.play("glass.mp3")
            store.response = "What is this sound? Maybe I could use this?"
        
        return
    
    def connection_dragged(drags, drop):
        if not drop:
            return
            
        freq_sound(drags[0].drag_name)
        
        return True
        

# Declare images used by this game.


image bg bar = "Deck's Bar.png"
image bg room = "Office Day Final.png"
image bg roomnight = "Office Night Final.png"
image bg black = "black_bg.png"

image tablet:
    "missing/Missing-Black/Layer 1-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 2-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 3-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 4-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 5-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 6-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 7-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 8-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 9-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 10-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 11-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 12-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 13-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 14-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 15-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 16-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 17-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 18-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 19-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 20-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 21-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 22-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 23-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 24-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 25-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 26-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 27-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 28-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 29-Missing-Black.png"
    pause 0.01
    "missing/Missing-Black/Layer 30-Missing-Black.png"
    pause 0.01
    repeat

image wave green:
    "Layer 1-Green-Oscilliscope.png"
    pause 0.05
    "Layer 2-Green-Oscilliscope.png"
    pause 0.05
    "Layer 3-Green-Oscilliscope.png"
    pause 0.05
    "Layer 4-Green-Oscilliscope.png"
    pause 0.05
    "Layer 5-Green-Oscilliscope.png"
    pause 0.05
    "Layer 6-Green-Oscilliscope.png"
    pause 0.05
    repeat
    
image wave purple:
    "Layer 1-Purple-Oscilliscope-Slow.png"
    pause 0.03
    "Layer 2-Purple-Oscilliscope-Slow.png"
    pause 0.03
    "Layer 3-Purple-Oscilliscope-Slow.png"
    pause 0.03
    "Layer 4-Purple-Oscilliscope-Slow.png"
    pause 0.03
    "Layer 5-Purple-Oscilliscope-Slow.png"
    pause 0.03
    "Layer 6-Purple-Oscilliscope-Slow.png"
    pause 0.03
    "Layer 7-Purple-Oscilliscope-Slow.png"
    pause 0.03
    "Layer 8-Purple-Oscilliscope-Slow.png"
    pause 0.03
    "Layer 9-Purple-Oscilliscope-Slow.png"
    pause 0.03
    "Layer 10-Purple-Oscilliscope-Slow.png"
    pause 0.03
    "Layer 11-Purple-Oscilliscope-Slow.png"
    pause 0.03
    "Layer 12-Purple-Oscilliscope-Slow.png"
    pause 0.03
    "Layer 13-Purple-Oscilliscope-Slow.png"
    pause 0.03
    "Layer 14-Purple-Oscilliscope-Slow.png"
    pause 0.03
    "Layer 15-Purple-Oscilliscope-Slow.png"
    pause 0.03
    repeat

image wave red:
    "Layer 1-Red-Oscilliscope-Fast.png"
    pause 0.05
    "Layer 2-Red-Oscilliscope-Fast.png"
    pause 0.05
    "Layer 3-Red-Oscilliscope-Fast.png"
    pause 0.05
    "Layer 4-Red-Oscilliscope-Fast.png"
    pause 0.05
    "Layer 5-Red-Oscilliscope-Fast.png"
    pause 0.05
    repeat

image wave blue:
    "Layer 1-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 2-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 3-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 4-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 5-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 6-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 7-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 8-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 9-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 10-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 11-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 12-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 13-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 14-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 15-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 16-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 17-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 18-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 19-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 20-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 21-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 22-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 23-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 24-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 25-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 26-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 27-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 28-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 29-Blue-Oscilliscope-Slower.png"
    pause 0.01
    "Layer 30-Blue-Oscilliscope-Slower.png"
    pause 0.01
    repeat
    
image wave gray = Image("Layer 1-Gray-Oscilliscope-Flatline.png")

image transition purple:
    "wave purple"
    time 2.0
    "wave gray"
    
image transition blue:
    "wave blue"
    time 2.0
    "wave gray"
    
image transition green:
    "wave green"
    time 2.0
    "wave gray"
    
image transition red:
    "wave red"
    time 2.0
    "wave gray"

image mina normal = Image("minaEmotions/mina Normal.png", xalign=0.5, yalign=0.04)
image mina angry = Image("minaEmotions/mina Angry.png", xalign=0.5, yalign=0.04)
image mina happy = Image("minaEmotions/mina Happy.png", xalign=0.5, yalign=0.04)
image mina sad = Image("minaEmotions/mina Sad.png", xalign=0.5, yalign=0.04)

image mina purple = Image("colors/purple-Mina.png", xalign=0.5, yalign=0.04)
image mina green = Image("colors/green-Mina.png", xalign=0.5, yalign=0.04)
image mina red = Image("colors/red-Mina.png", xalign=0.5, yalign=0.04)
image mina blue = Image("colors/blue-Mina.png", xalign=0.5, yalign=0.04)
image mina gray = Image("colors/gray-Mina.png", xalign=0.5, yalign=0.04)

image kai normal = Image("kai/Kai Normal.png", xalign=0.5, yalign=0.04)
image kai angry = Image("kai/Kai Angry.png", xalign=0.5, yalign=0.04)
image kai sad = Image("kai/Kai Normal.png", xalign=0.5, yalign=0.04)


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Mina")
define k = Character("Kai")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # These display lines of dialogue.

    "{=n_text}I woke up at 0600 on the dot again today. Almost like I’d been programmed to, like one of those enhancement junkies. Another night of vivid dreams. Dreams about her. Always about her.{/n_text}"
    
    play sound "TV2.mp3"
    show tablet at truecenter
    window hide
    pause
    
    "{=n_text}Since I took this case, I haven’t been able to get her out of my mind. Where is she? Why’d she run away? What happened to you Kai?{/n_text}"
    
    play sound "TV2.mp3"
    hide tablet
    
    "{=n_text}The questions dart around in my head like a school of fish. Maybe today will be the day I find her and can finally put this obsession to rest.{/n_text}"
    
    stop music fadeout 4.0
    jump the_bar
    
label the_bar:
    $ number_of_flags = 0
    $ purple_seen = False
    $ blue_seen = False
    $ green_seen = False
    $ red_seen = False
    
    $ green_flag_obtained = False
    $ blue_flag_obtained = False
    $ red_flag_obtained = False
    $ blue_flag_obtained = False
    
    play music "Bar_Loop_01.mp3" loop fadein 1.0
    scene bg bar
    with fade
    
    "{=n_text}This bar smells of liquor and melancholy. The half full glasses reflect the faces of the half empty souls holding them.{/n_text}"
    
    "{=n_text}People come here to forget. I’m hoping one of them remembers.{/n_text}"
    
    show mina normal
    
    "{=n_text}There she is. {w}The woman in the picture with Kai. {w}I feel like I’ve seen her before, but I’m not sure where. It doesn’t matter. It’s time to put this empath implant to the test...{/n_text}"
    
    "{=n_text}{b}EMPATH MOD V.07 INITIATED{b}{/n_text}"
    
    play sound "Sine2Sec.mp3"
    $ change_wave('wave gray')
    
    m "What are {i}you{/i} looking at?"
    
    menu:
        "\"Not much.\"":
            show mina happy
            m "\"Classy. You remind me of someone I used to know.\""
            
        "\"Someone who needs a drink?\"":
            show mina happy
            m "\"You’re very observant.\""
            
        "\"A soldier?\"":
            show mina happy
            $ change_wave('transition blue')
            m "\"Ha! I've been called worse.\""
                
    m "\"Buy me a drink?\""
    
    menu:
        "\"Sure. What’s your poison?\"": 
            show mina normal
            m "\"Whiskey, neat.\""
            jump lets_drink
            
        "\"How about some coffee?\"":
            show mina angry
            m "\"You trying to tell me I’ve had enough?\""
            jump backoff
    
label lets_drink:
    
    menu:
        "\"Two whiskeys, neat. The best you got.\"":
            show mina sad
            $ change_wave('transition red')
            m "\"Quick way to drown the memories.\""
            jump questions
            
        "\"One whiskey, neat. One coffee.\"":
            show mina happy
            $ change_wave('transition green')
            m "\"Smart to keep a clear head.\""
            jump questions
            
label backoff:
    
    menu:
        "\"You just looked tired.\"":
            show mina sad
            m "\"I am tired, but coffee won’t fix it.\""
            
        "\"I just assumed at this hour it’d be coffee…\"":
            show mina happy
            m "\"I guess that’s a fair assumption, except we’re in a bar.\""
    
    "\"Point taken.\""
    jump lets_drink
                
label questions:
    menu:
        "Pull out tablet to take notes.":
            show mina angry
            $ change_wave('transition purple')
            m "\"Hey, what do you need that for?\""
            jump notes
            
label notes:
    menu: 
        "\"I’m just keeping track of my thoughts.\"":
            show mina normal
            $ change_wave('transition purple')
            m "\"I’d rather you use a notepad.\""
            jump obsolete
            
        "\"Worried about what you’re telling me?\"":
            m "\"You’re awfully nosy, friend. That can be dangerous.\""
            jump another_drink
            
label obsolete:
    menu:
        "\"Trying not to leave a digital trail?\"":
            show mina angry
            m "\"You’re awfully nosy, friend. That can be dangerous.\""
            jump another_drink
                    
        "\"A notepad? They’re obsolete.\"":
            show mina happy
            $ change_wave('transition purple')
            m "\"Obsolete and expensive. But also extremely hard to hack.\""
            jump hack
            
label hack:
    menu:
        "\"You’re obviously an officer, why are you afraid of hacking?\"":
            $ change_wave('transition purple')
            m "\"Even officers have things they’d rather not have everyone know.\""
            jump secrets
        
        "\"Got something to hide?\"":
            show mina angry
            m "\"You’re awfully nosy, friend. That can be dangerous.\""
            jump another_drink
            
label secrets:
    menu:
        "\"So what are you hiding?\"":
            show mina angry
            m "\"You’re awfully nosy, friend. That can be dangerous.\""
            jump another_drink
        
        "\"Secrets?\"":
            show mina sad
            $ change_wave('transition purple')
            m "\"Everyone has their secrets. Some are just more dangerous than others.\""
            jump purple_secret_unlocked
                
label another_drink:
     
    show mina normal
    show bg bar with fade
    
    m "\"Another round?\""
    
    menu:
        "\"Sure. What's it like being a soldier?\"" if not blue_seen:
            show mina sad
            $ change_wave('transition blue')
            m "\"It used to be different.\" She pauses, looking down."
            jump soldier
        
        "\"How about that weather?\"" if not red_seen:
            show mina angry
            $ red_seen = True
            #$ change_wave('transition red')
            m "\"You can't stop me from drowning my sorrows.\""
            jump another_drink
            
        "\"Aren't you worried about drinking too much?\"" if not green_seen:
            show mina sad
            $ change_wave('transition green')
            m "\"It's the only safe way to alter my state of mind.\""
            jump mind
        
        "\"I think it's your turn to buy...\"":
            jump office_night
        
label soldier:
    $ blue_seen = True
    menu:
        "Wait.":
            show mina happy
            $ change_wave('transition blue')
            m "\"I had a friend back in academy. She liked whisky too.\""
            jump whisky
            
        "\"Things got too real for you?\"":
            show mina sad
            m "\"I guess you could say that.\""
            jump another_drink
            
label whisky:
    
    menu:
        "\"That wouldn't happen to be Kai, would it?\"":
            show mina angry
            m "\"I don't know where you heard that name, friend, but you best forget it.\""
            jump another_drink
                
        "\"I bet you made lots of memories together.\"":
            show mina sad
            $ change_wave('transition blue')
            m "Some memories are bittersweet.\""
            jump bittersweet
            
label bittersweet:
    
    menu:
        "\"Memories of that friend?\"":
            show mina angry
            "\"You're barking up the wrong tree.\""
            jump another_drink
                
        "Wait for her to reminisce.":   
            m "\"We ended up getting partnered up when we graduated. Our first collar was her last.\""
            jump regrets
            
label regrets:
        
    menu:
        "Wait for her to reminisce.":
            m "\"Some regrets just can't be washed away.\""
            jump blue_secret_unlocked
            
#label weather:

label mind:
    $ green_seen = True
    menu:
        "\"You lost me…?\"":
            m "\"Never mind.\""
            jump another_drink
                
        "\"What do you mean altered state of mind?\"":
            show mina normal
            $ change_wave('transition green')
            m "\"I’m not talking about drugs.\""
            jump enhancements

label enhancements:
    menu:
        "\"You mean enhancements?\"":
            show mina angry
            $ change_wave('transition green')
            m "\"Those enhancement junkies are fools. Technology has a place, and it’s not in my head.\""
            jump contradiction
        
        "\"What are you talking about?\"":
            m "\"Nothing important.\""
            jump another_drink
                
label contradiction:
    menu:
        "\"They just take it to the extreme. Tech isn’t inherently dangerous.\"":
            show mina angry
            m "\"You’re a fool too.\""
            jump another_drink
                
        "\"What about your official implant there?\"":
            show mina sad
            $ change_wave('transition green')
            m "\"We don’t all have a choice...\""
            jump green_secret_unlocked
            
label purple_secret_unlocked:
    $ number_of_flags = number_of_flags + 1
    $ purple_flag_obtained = True
    show bg black with fade
    show wave purple at right onlayer waveui
    
    $renpy.pause(1.0)
    
    $ renpy.music.set_pause(True, channel='music')
    $ renpy.play("Paper.mp3")
    show mina purple with dissolve
        
    "Who uses paper anymore? People trying to stay off the grid? What are they {i}hiding{/i}?"
    
    hide wave purple onlayer waveui
    $ renpy.music.set_pause(False, channel='music')
    jump another_drink
    
label blue_secret_unlocked:
    $ number_of_flags = number_of_flags + 1
    $ blue_flag_obtained = True
    show bg black with fade
    show wave blue at right onlayer waveui
    
    $renpy.pause(1.0)
    
    $ renpy.music.set_pause(True, channel='music')
    $ renpy.play("Lock1.mp3")
    show mina blue with dissolve
        
    "Maximum security. Whoever she regrets putting away is definitely not going to see the sun for a while."
    
    hide wave blue onlayer waveui
    $ renpy.music.set_pause(False, channel='music')
    jump another_drink
    
label green_secret_unlocked:
    $ number_of_flags = number_of_flags + 1
    $ green_flag_obtained = True
    show bg black with fade
    show wave green at right onlayer waveui
    
    $renpy.pause(1.0)
    
    $ renpy.music.set_pause(True, channel='music')
    $ renpy.play("WhispersDownloading.mp3")
    show mina green with dissolve
        
    "That’s not a normal download. It feels … almost sentient?"
    
    hide wave green onlayer waveui
    $ renpy.music.set_pause(False, channel='music')
    jump another_drink


label office_night:
    $ transfer_seen = False
    $ papers_seen = False
    $ scientist_seen = False
    show bg black
    hide mina
    
    if number_of_flags > 2:
        "{cps=15}{=n_text}We closed down the bar like two cadets after passing their officers training. Mina’s an alright gal, despite whatever ghosts she's running from.{/n_text}{/cps}"
        "{cps=15}{=n_text} I wonder how all this ties to Kai? I better head home to put the pieces together.{/n_text}{/cps}"
        jump house_call
        return

    elif number_of_flags > 0: 
        "{cps=15}{=n_text}This new empathy chip isn't quite what they promised. Or maybe Mina is just that guarded. Either way I don't have a lot to go on. I wonder how all this ties to Kai? I better head home to put the pieces together.{/n_text}{/cps}"
        jump house_call
        return
    else:
        "{cps=15}{=n_text}This empathy chip was a poor purchase. I can't believe I didn't get anything useful from Mina! My only lead and I blew it. Better go home and sleep it off.{/n_text}{/cps}"
        jump house_call
        return
            
label house_call:
    
    play music "Neon Noir Reveal.mp3"
    
    k "\"I hope you don't mind. I let myself in.\""
    
    scene bg roomnight
    show kai normal
    
    show kai angry
    k "\"I heard you’ve been looking for me.\""
    
    $ renpy.music.set_volume(0.4, delay=0, channel='music')

    menu:
        "\"You just made my job easier, Kai.\"":
            show kai sad
            k "\"No one has called me that in a while. I thought I'd escaped that life.\""
            jump escape

        "\"You look exactly like your photo.\"":
            show kai sad
            k "\"But I'm not the same woman. That was a different life. You're not taking me back.\""
            jump excuses

label escape:

    menu:
        "\"I'm taking you in.\"":
            show kai angry
            k "\"I'm afraid that's just not going to happen.\""
            jump excuses

label excuses:
    
    menu:
        "\"You can't say anything to change my mind.\"":
            show kai angry
            k "\"You don't understand!\""
            jump answers

        
        "\"Please don't make this difficult.\"":
            show kai sad
            k "\"So there's some humanity that survives the transfer.\""
            jump transfer
            
label transfer:
    $ transfer_seen = True
    
    menu:
        "\"Transfer? ...\"" if green_flag_obtained:
            show kai sad
            k "\"Yes, when they copied my memories and gave them to you.\""
            $ renpy.play("WhispersDownloading.mp3")
            "That sound... could it be a consciousness? My consciousness?\""
            jump answers
        
        "\"Don't try to confuse me!\"":
            "She's obviously trying to trick me!"
            jump bad
    
        "\"What do you mean?\"":
            k "\"There's more to this than you realize.\""               
            jump answers
            
label answers:
    
    menu:
        "\"Help me understand.\"" if not transfer_seen:
            k "\"So there's some humanity that survives the transfer.\""
            jump transfer
        
        "\"Why did you come here?\"" if not papers_seen:
            k "\"To show you these documents.\""
            jump papers
        
        "\"Are you working alone?\"" if not scientist_seen:
            k "\"I'm the only one who knows now, yes.\""
            jump scientist
            
        "\"I believe you. Get out of here.\"" if scientist_seen or transfer_seen or scientist_seen:
            jump good
            
label papers:
    $ papers_seen = True
    
    menu:
        "\"Only criminals keep paper documents.\"":
            k "\"You're right about that. The things they're doing are criminal!\""
            jump bad
        
       
        "\"What are you hiding using paper?\"" if purple_flag_obtained:
            k "\"See for yourself.\""
            $ renpy.play("Paper.mp3")
            "The papers from Mina's memory... Are these those documents?"
            jump answers
        
        "\"I don't want any part of those.\"":
            jump answers

label scientist:
    $ scientist_seen = True
    
    menu:
        "\"What do you mean now?\"" if blue_flag_obtained:
            k "\"He was a government scientist. But he had a conscience. He knew what they were doing. He showed us proof. We locked him up anyways."
            $ renpy.play("Lock1.mp3")
            "Their first collar... Was he innocent?"               
            jump answers
                    
        "\"Good, then it ends here. Let's go.\"":
            show kai angry
            k "\"I told you I'm not going back!\""
            jump bad
        
        "\"Seems like you know something dangerous.\"":             
            jump answers

label bad:
    
    "{cps=15}{=n_text}It all happened so quickly. Did she draw first or did I? I'd better contact the authorities...{/n_text}{/cps}"
    
    hide kai
    
    show mina normal
    m "\"I guess you sniffing around brought her out of hiding.\""
    show mina sad
    m "\"And you wondered why I drink...\""
    
    return

label good:
    
    "{cps=15}{=n_text}If she's right, I can't take her in. And if anyone knows she paid me a visit, I'm not safe either. I'll have to figure things out on the road.{/n_text}{/cps}"
    
    return
            