"""Screen Schedule
"""

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.factory import Factory
import datetime
from kivy.properties import ObjectProperty, ListProperty
from uix.tabbedcarousel import TabbedCarousel

app = App.get_running_app()


class TalkInfo(Factory.TouchRippleBehavior, Factory.ButtonBehavior, Factory.BoxLayout):
    talk = ObjectProperty(None)

    Builder.load_string('''
<TalkInfo>
    canvas.before:
        Color:
            rgba: app.gray[:3]+[.2] 
        Rectangle:
            size: self.size
            pos: self.pos
    size_hint_y: None
    height: max(lblinfo.texture_size[1] + dp(4), dp(40))
    spacing: dp(5)
    on_release: 
        scr = app.load_screen('ScreenTalks', manager=app.navigation_manager)
        scr.talkid = self.talk['talk_id']
    LeftAlignedLabel:
        size_hint: None, 1
        font_size: dp(14)
        valign: 'middle'
        width: dp(45)
        text: "{}\\n{}".format(root.talk['start_time'], root.talk['end_time'])
    Label:
        id: lblinfo
        font_size: dp(14)
        valign: 'middle'
        size_hint: 1, 1
        text_size: self.width, None
        text: root.talk['title']
''')




class ScreenSchedule(Screen):
    """
    Screen to display the schedule as per schedule.json. A default
    schedule is provided.
    """

    Builder.load_string('''
<Topic@Label>
    canvas.before:
        Color
            rgba: app.base_active_color
        Rectangle
            size: self.width, self.height
            pos: self.right - self.width  , self.y + dp(3)
        Color
            rgba: app.base_active_color[:3]+[.5]
        Rectangle
            size: self.width, self.height
            pos: self.right - self.width - dp(3), self.y
        Color
            rgba: app.black[:3]+[.5]
        Rectangle
            texture: self.texture
            size: self.width - dp(50), self.height
            pos: self.x + dp(28), self.y - dp(3)
    font_size: dp(18)
    text_size: self.width - dp(50), self.height
    size_hint: None, None
    width: dp(300)
    height: dp(45)
    halign: 'center'
    valign: 'middle'
    pos_hint: {'left': 1}

<AccordionItemTitle>
    text_size: self.width - dp(10), self.height
    halign: 'left'
    valign: 'middle'
    color: app.base_color

<AccordionItem>
    canvas.before:
        Rectangle
            size: dp(270), dp(32)
            pos: self.x, self.top - dp(40)

<Header@LeftAlignedLabel>
    size_hint_y: None
    height: dp(27)
    width: dp(40)
    size_hint: None, 1
    background_color: app.base_active_color[:3] + [.3]
    canvas.before:
        Color
            rgba: root.background_color if root.background_color else app.white
        Rectangle
            size: self.size
            pos: self.pos
    
   
<ScreenSchedule>
    name: 'ScreenSchedule'
    BoxLayout
        spacing: dp(10)
        orientation: 'vertical'
        # padding: dp(4)
        Topic
            text: app.event_name
        Accordion
            id: accordian_days
            orientation: 'vertical'

<TalkTitle@BoxLayout>
    spacing: dp(9)   
    height: dp(30)
    size_hint_y: None
    Header
        size_hint: None,None
        text: 'Time'
    Header
        text: 'Title'

<TabbedCarousel>
    background_color: app.white[:3]+[0]

<TabbedPanelHeader>
    background_color: app.white if self.state == 'down' else app.base_active_color
    background_normal: 'atlas://data/default/but_overlay'
    background_down: 'atlas://data/default/but_overlay'
    font_size: dp(12)

<Track@Screen>
    ScrollView
        ScrollGrid
            id: container
 ''')

    def on_pre_enter(self):
        container = self.ids.accordian_days
        container.opacity = 0

    def on_enter(self, onsuccess=False):
        """Series of actions to be performed when Schedule screen is entered
        """
        container = self.ids.accordian_days
        # make sure the corresponding navigation is depressed
        app.navigationscreen.ids.left_panel.ids.bt_sched.state = 'down'
        # if the screen loads by pressing back, do nothing.
        if self.from_back:
            Factory.Animation(d=.5, opacity=1).start(container)
            return
        self.ids.accordian_days.clear_widgets()
        from network import get_data

        events = get_data('event', onsuccess=onsuccess)
        if not events:
            return

        schedule = get_data('schedule', onsuccess=onsuccess)
        if not schedule:
            return

        events = events.get('0.0.1')
        schedule = schedule.get('0.0.1')[0]

        # take first event as the one to display schedule for.
        self.event = event = events[0]
        app.event_name = event['name']
        app.venue_name = event['venue']
        start_date = event['start_date']
        end_date = event['end_date']
        
        dates = list(schedule.keys())[1:]
        # each day could have multiple tracks
        tracks = schedule['tracks']
        dates = sorted(
            dates,
            key=lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))

        # perf optims, minimize dot lookups
        acordion_add = self.ids.accordian_days.add_widget
        AccordionItem = Factory.AccordionItem
        Track = Factory.Track

        # criar tabbed carrousel apenas para os locais que tenham programação na data
        list_tracks = ["[LAB] GAROTAS\nDO ENIAC", "[LAB] ADA\nLOVELACE", "[LAB] GRACE\nHOPPER",
                       "[SALA] HIPACIA\nDE ALEXANDRIA", "[SALA] KAREN\nSPARK JONES",
                       "[LAB] JEAN\nSAMMET", "[LAB] RADIA\nPERLMAN", "[LAB] CAROL\nSHAW",
                       "[SALA] ROBERTA\nWILLIAMS", "[SALA] FRANCES\nALLEN", "TEATRO\nPYTHONICO",
                       "FREETIME" ]

        locals_to_date = {
            '2018-05-24': [1, 2, 3, 4, 5, 11, 12],
            '2018-05-25': [6, 7, 8, 9, 10, 12],
            '2018-05-26': [11, 12]
        }

        first = None
        today = datetime.datetime.now()
        
        for date in dates:
            # add current day as accordion widget
            ccday = datetime.datetime.strptime(date,"%Y-%m-%d")
            cday = AccordionItem(title=ccday.strftime("%d/%m/%Y"))

            if ccday.date() >= today.date():
                if not first: first = cday
            acordion_add(cday)
            day_sched = schedule[date]
            # create a carousel for each track
            tcarousel = TabbedCarousel()
            
            # this carousel would show each track as new tab
            trackscreens = []
            tsa = trackscreens.append
            tca = tcarousel.add_widget
            for track in tracks:
                new_trk = Track(name=track)
                tsa(new_trk)
                # add track to carousel if date it is ok
                if list_tracks.index(new_trk.name)+1 in locals_to_date[date]:
                    tca(new_trk)

            for talk in day_sched:
                try:
                    stime  = "%s -- %s"%(date, talk['start_time'])
                    etime  = "%s -- %s"%(date, talk['end_time'])
                    stime = datetime.datetime.strptime(stime,"%Y-%m-%d -- %H:%M")
                    etime = datetime.datetime.strptime(etime,"%Y-%m-%d -- %H:%M")
                    talk['current'] = today > stime and today < etime
                except:
                    pass
                tid = talk['track']
                if tid.lower() == 'all':
                    for tlk in trackscreens:
                        tc = tlk.ids.container
                        ti = TalkInfo(talk=talk)
                        ti.color = app.gray[:3]+[2] if len(tc.children)%2 == 0 else (.3, .3, .3, .2)
                        if talk['current']: ti.color = ti.color[:3] + [.8]
                        tc.add_widget(ti)
                    continue
                ti = TalkInfo(talk=talk)
                trackscreens[int(tid)-1].ids.container.add_widget(ti)

            cday.add_widget(tcarousel)
        if first: container.select(first)
        Factory.Animation(d=.5, opacity=1).start(container)
