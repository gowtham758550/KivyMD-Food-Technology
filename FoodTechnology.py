from kivy.lang.builder import Builder
from kivymd.app import MDApp
from webbrowser import open

kv = """
BoxLayout:
    orientation:'vertical'
    
    MDToolbar:
        title: 'Food Technology'
        md_bg_color: .2,.2,.2,1
        specific_text_color: 1,1,1,1
        
    MDBottomNavigation:
        panel_color:.2,.2,.2,1
        
        MDBottomNavigationItem:
            name:'screen1'
            text:'Free'
            ScrollView:
                MDList:
                    TwoLineListItem:
                        text: 'Food Allergy Training'
                        secondary_text: 'Provider: Allergy Training'
                        on_press: app.open_link("https://allergytraining.food.gov.uk/english/")
                        	
                    TwoLineListItem:
                        text: 'Food Labelling'
                        secondary_text: 'Labelling Training'
                        on_press: app.open_link("https://labellingtraining.food.gov.uk/")
                            
                    TwoLineListItem:
                        text: 'Root Cause Analysis'
                        secondary_text: 'RCA Training'
                        on_press: app.open_link("https://rcatraining.food.gov.uk/#module-menu-fbo")
                        
                    TwoLineListItem:
                        text: 'Food Safety and Quality Management'
                        secondary_text: 'Provider: OpenLearning'
                        on_press: app.open_link("https://www.openlearning.com/courses/food-safety-and-quality-management/")
                        
                    TwoLineListItem:
                        text: 'Food Defence'
                        secondary_text: 'Provider: IFSH IIT' 
                        on_press: app.open_link("https://www.ifsh.iit.edu/fspca/courses/intentional-adulteration")
                        
                    TwoLineListItem:
                        text: 'Six Sigma White Belt Certification in Food Service'
                        secondary_text: 'Six Sigma Online'
                        on_press: app.open_link("https://www.sixsigmaonline.org/six-sigma-white-belt-certification-in-food-service/")
               
        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Paid'
            ScrollView:
                MDList:
                    TwoLineListItem:
                        text: 'Elements of Food Safety Management: ISO'
                        secondary_text: 'Provider: Alison'
                        on_press: app.open_link("https://alison.com/course/iso-22000-2018-elements-of-food-safety-management-system-fsms")
                        
                    TwoLineListItem:
                        text: "Intelluctual Property in Food and Drink"
                        secondary_text: "Provider: Future learn"
                        on_press: app.open_link("https://www.futurelearn.com/courses/intellectual-property-management-food")
                        
                    TwoLineListItem:
                        text: "Trust in Our Food"
                        secondary_text: "Provider: Future learn"
                        on_press: app.open_link("https://www.futurelearn.com/courses/food-supply-systems")
                        
                    TwoLineListItem:
                        text: "Sustainable Food Production & Agriculture"
                        secondary_text: "Provider: Future learn"
                        on_press: app.open_link("https://www.futurelearn.com/courses/sustainable-agriculture-in-a-changing-environment")
                    
                    TwoLineListItem:
                        text: "Improving Food Productions"
                        secondary_text: "Provider: Future learn"
                        on_press: app.open_link("https://www.futurelearn.com/courses/food-production-agricultural-technology-plant-biotechnology")
                        
                    TwoLineListItem:
                        text: "Understanding Food Processing Technologies"
                        secondary_text: "Provider: Future learn"
                        on_press: app.open_link("https://www.futurelearn.com/courses/how-is-my-food-made")
                        
                    TwoLineListItem:
                        text: "Identifying Food Fraud"
                        secondary_text: "Provider: Future learn"
                        on_press: app.open_link("https://www.futurelearn.com/courses/food-fraud")
                        
                    TwoLineListItem:
                        text: "Understanding Sustainable Farming"
                        secondary_text: "Provider: Future learn"
                        on_press: app.open_link("https://www.futurelearn.com/courses/explore-how-farmers-produce-food-sustainably")
        
        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'About'
            MDLabel:
                halign:'center'
                pos_hint: {"center_x": 0.5, "center_y": 0.9}
                text: 'An android application developed using python specially for students who are interesting in Food Technology.'
            
            MDLabel:
            	text: 'Developed by Gowtham S'
                pos_hint: {'center_y': .7}
                halign:'center'
                
            MDRaisedButton:
            	text: "Github"
            	on_press: app.open_link("https://www.github.com/gowtham758550/")
            	pos_hint:{"center_x": 0.3, "center_y": 0.6}
            	
            MDRaisedButton:
                pos_hint:{"center_x": 0.7, "center_y": 0.6}
            	text: "LinkedIn"
            	on_press: app.open_link("https://www.linkedin.com/in/gowtham-s-516433182")
            	
            MDLabel:
            	text: 'With the help of Monish Rithvi'
            	halign: 'center'
            	
            MDRaisedButton:
                pos_hint: {"center_x": 0.5, "center_y": 0.4}
            	text: "Linkedin"
            	on_press: app.open_link("https://www.linkedin.com/in/monish-rithvi-850b23193")
            	
            MDRaisedButton:
                pos_hint:{"center_x": 0.5, "center_y": 0.2}
            	text: "Click to view source code"
            	on_press: app.open_link("https://github.com/gowtham758550/KivyMD-Food-Technology")
            	

                                    
            
"""


class FoodTechnology(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Red'
        self.icon = ''
        return Builder.load_string(kv)

    def open_link(self, url):
        open(url)


FoodTechnology().run()
