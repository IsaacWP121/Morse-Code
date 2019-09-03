import pygame
from pygame import Color
from winsound import Beep
from roundrects import aa_round_rect
from random import choice

pygame.init() 
icon = pygame.image.load("")
pygame.display.set_icon(icon)
pygame.display.set_caption("Morse Code")
window_h = 725
window_w = 1300
window = pygame.display.set_mode((window_w, window_h))
morse_keystrokes = [] # this empty list will be used to log and store the short and long beeps
button_text = "Default"
cheatsheettext = ["A ._", ",", "B _...", ",", "C _._.", ",",
                  "D _..", ",", "E .", ",", "F .._.", ",", "G __.",
                  ",", "H ....", ",", "I ..", ",", "J . ___", ",", "K _._", ",",
                  "L ._..", ",", "M __", ",", "N _.", ",",
                  "O ___", ",", "P ._._", ",", "Q __._", ",",
                  "R ._.", ",", "S ...", ",", "T _", ",", "U .._", ",", "V ..._",
                  ",", "W .__", ",", "X _.._", ",", "Y _.__", ",", "Z __..",
                  ",", "", "", "", "", ",", "1 .____", ",", "2 ..___",
                  ",", "3 ...__", ",", "4 ...._", ",", "5 .....", ",", "6 _....", ",",
                  "7 __...", ",", " 8 ___..", ",", "9 ____.", ",", "0 _____"]
checking_dict = {'A': '._', 'B': '_...', 'C': '_._.', 'D': '_..', 'E': '.', 'F': '.._.', 
                'G': '__.', 'H': '....', 'I': '..', 'J': '.', 'K': '_._', 'L': '._..', 'M': '__', 'N': '_.', 
                'O': '___', 'P': '._._', 'Q': '__._', 'R': '._.', 'S': '...', 'T': '_', 'U': '.._', 'V': '..._', 
                'W': '.__', 'X': '_.._', 'Y': '_.__', 'Z': '__..', '1': '.____', '2': '..___', '3': '...__', 
                '4': '...._', '5': '.....', '6': '_....', '7': '__...', '': '8', '9': '____.'}
characters = [" ", "a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", "I", "j", "J", "k", "K", 
             "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R", "s", "S", "t", "T", "u", "U", "v", "V", "w",
             "W", "x", "X", "y", "Y", "z", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
samplewords = ['Operation', 'Student', 'Believe', 'Station', 'Visit', 'Police', 'Effect', 'Finally', 'Event', 'Player',
               'Imagine', 'Home', 'Already', 'So', 'Question', 'Front', 'South', 'Black', 'Employee', 'Charge', 'Down',
               'Near', 'Window', 'Fine', 'Help', 'Forget', 'Those', 'Management', 'Amount', 'Death', 'Treatment',
               'Rule', 'Full', 'Guess', 'Behind', 'Right', 'Born', 'Street', 'Month', 'Three', 'Protect', 'Land',
               'Character', 'City', 'Technology', 'Song', 'Blue', 'How', 'Safe', 'Range', 'Hang', 'Affect', 'Wind',
               'Write', 'My', 'Violence', 'Final', 'Tonight', 'Child', 'Remove', 'Business', 'Into', 'Because',
               'Contain', 'Meeting', 'Newspaper', 'Smile', 'Two', 'Himself', 'Ability', 'Man', 'Maybe', 'Learn', 'Room',
               'Course', 'Season', 'Possible', 'Career', 'In', 'Someone', 'Their', 'Seek', 'Second', 'Security',
               'Break', 'Community', 'Item', 'But', 'Environment', 'Sense', 'Well', 'Activity', 'Languageverybody',
               'Major', 'Type', 'Coach', 'Beat', 'Compare', 'Cut', 'Few', 'General', 'Probably', 'Commercial',
               'However', 'Address', 'Animal', 'Perhaps', 'Either', 'Realize', 'Once', 'That', 'About', 'Hear', 'Set',
               'Indeed', 'Leg', 'Stay', 'Brother', 'Attention', 'Son', 'Whatever', 'Actually', 'Simply', 'Lie',
               'Toward', 'Without', 'Military', 'Together', 'Him', 'Call', 'Hotel', 'Big', 'Choice', 'Partner',
               'Choose', 'Ok', 'Administration', 'Development', 'Population', 'Value', 'Investment', 'Court', 'Colour',
               'Itself', 'Instead', 'Move', 'Private', 'Spring', 'Open', 'Model', 'Respond', 'Dog', 'This', 'Cold',
               'Become', 'People', 'Edge', 'Nature', 'Bring', 'Worry', 'Billion', 'Use', 'Tough', 'Under', 'Party',
               'Camera', 'Process', 'Whether', 'Record', 'Century', 'Part', 'Sister', 'Develop', 'Notice', 'Difference',
               'Defence', 'Step', 'Of', 'Challenge', 'House', 'Increase', 'Key', 'Get', 'Sure', 'Prevent', 'Run',
               'Never', 'Try', 'Note', 'She', 'Analysis', 'Other', 'The', 'History', 'Buy', 'Shake', 'Save', 'Out',
               'Budget', 'Eye', 'Every', 'Ask', 'Bit', 'Nearly', 'Unit', 'Reduce', 'Heavy', 'Green', 'Risk',
               'Interesting', 'Herself', 'Artist', 'Article', 'Whole', 'Republican', 'Authority', 'Pick', 'Could',
               'See', 'Like', 'Low', 'Peace', 'Give', 'High', 'Represent', 'Minute', 'Consider', 'Eat', 'Stand',
               'These', 'Happen', 'Early', 'Account', 'Arrive', 'Example', 'Method', 'Though', 'Thank', 'Art', 'Accept',
               'Action', 'Some', 'Conference', 'End', 'Source', 'Magazine', 'Expect', 'Seem', 'Position', 'Let', 'Also',
               'Politics', 'Hold', 'Recognize', 'Yourself', 'Pressure', 'Section', 'Even', 'Such', 'Sevendream',
               'Participant', 'East', 'Cancer', 'Nation', 'Feel', 'For', 'Woman', 'Collection', 'Report', 'Firm',
               'Important', 'Candidate', 'Her', 'Pain', 'Quality', 'Involve', 'Say', 'Dead', 'Ahead', 'Heart',
               'Production', 'Check', 'Lawyer', 'Bill', 'Trouble', 'Care', 'Fly', 'Statement', 'Patient', 'Maintain',
               'Then', 'Congress', 'Drug', 'During', 'Network', 'Another', 'Certain', 'Option', 'Wonder', 'Program',
               'Least', 'Project', 'First', 'Truth', 'Through', 'New', 'Subject', 'Sex', 'Produce', 'Red', 'Memory',
               'Wife', 'Up', 'Future', 'Site', 'Despite', 'Appear', 'Factor', 'Order', 'Recent', 'Generation',
               'Individual', 'Information', 'Look', 'Stop', 'Daughter', 'Apply', 'Base', 'Game', 'Expert', 'Chance',
               'Wall', 'Left', 'Think', 'Far', 'Dark', 'Total', 'Usually', 'Evening', 'Speech', 'Where', 'Reveal',
               'Paper', 'Several', 'Manage', 'Rest', 'Force', 'Claim', 'Whose', 'School', 'Drop', 'Response', 'Wrong',
               'Gun', 'Light', 'Necessary', 'Close', 'Lose', 'Sit', 'American', 'Sometimes', 'Health', 'Foreign',
               'Would', 'Push', 'Throw', 'Avoid', 'Cost', 'Word', 'Figure', 'Return', 'Public', 'Mrs', 'Shoot', 'Hair',
               'Around', 'Job', 'Better', 'Have', 'A', 'Want', 'Market', 'Almost', 'Fear', 'Detail', 'Anything', 'Do',
               'Your', 'Ready', 'Piece', 'No', 'Love', 'Ground', 'Cultural', 'Way', 'Something', 'Material', 'Per',
               'Hour', 'Practice', 'Again', 'Friend', 'Study', 'Series', 'Later', 'Number', 'Crime', 'Continue', 'By',
               'Short', 'Show', 'Issue', 'Huge', 'Walk', 'Else', 'Company', 'Tell', 'Food', 'Movement', 'Skin',
               'System', 'Glass', 'Although', 'Phone', 'Condition', 'Owner', 'Suddenly', 'Industry', 'Turn',
               'Knowledge', 'Media', 'Family', 'Strong', 'Federal', 'Somebody', 'Field', 'Doctor', 'Make', 'Couple',
               'Measure', 'Benefit', 'Quite', 'Myself', 'Scientist', 'Oh', 'Scene', 'Impact', 'Five', 'Sport',
               'Understand', 'Draw', 'Card', 'Many', 'Determine', 'Goal', 'Recently', 'Change', 'Describe', 'Adult',
               'Wide', 'Majority', 'Die', 'Listen', 'Nice', 'Guy', 'Seat', 'Car', 'President', 'You', 'While', 'Trip',
               'Certainly', 'To', 'Sell', 'Modern', 'Each', 'Religious', 'Bar', 'Interview', 'Clearly', 'Hope',
               'Victim', 'Effort', 'Indicate', 'There', 'Stock', 'Finger', 'Staff', 'Tree', 'Executive', 'Available',
               'Lead', 'Agreement', 'Explain', 'Evidence', 'Present', 'Quickly', 'Culture', 'Strategy', 'Here',
               'Capital', 'All', 'Thus', 'Large', 'Pretty', 'Civil', 'Former', 'Cover', 'Prove', 'Church', 'Image',
               'Good', 'Sound', 'Attack', 'Cell', 'Onto', 'Reflect', 'Decide', 'Relate', 'Various', 'Able', 'Follow',
               'Space', 'Own', 'Remain', 'Mean', 'Property', 'Stage', 'Region', 'Year', 'Less', 'Assume', 'Us', 'Week',
               'Easy', 'Board', 'At', 'Prepare', 'Best', 'Add', 'Result', 'Inside', 'Outside', 'Ball', 'Service',
               'Writer', 'Talk', 'Hard', 'Girl', 'Legal', 'Place', 'Design', 'Within', 'TV', 'Allow', 'Situation',
               'Spend', 'Late', 'Treat', 'Four', 'Only', 'Suffer', 'Debate', 'Trade', 'Physical', 'Garden', 'Member',
               'Test', 'Door', 'Serious', 'Off', 'Lot', 'Enough', 'Its', 'From', 'Anyone', 'Ever', 'Thousand',
               'Soldier', 'Middle', 'More', 'Fight', 'Threat', 'Fund', 'Moment', 'Different', 'Remember', 'Happy',
               'Kill', 'On', 'Discussion', 'Thought', 'Road', 'Include', 'Between', 'Person', 'Weight', 'Floor',
               'Medical', 'Me', 'Standard', 'Yes', 'Similar', 'Film', 'Come', 'World', 'Eight', 'Hundred', 'Main',
               'Line', 'Thing', 'Admit', 'Professor', 'Why', 'Too', 'Popular', 'Institution', 'Just', 'State', 'View',
               'Mouth', 'Form', 'Shot', 'Data', 'Require', 'Sign', 'Personal', 'Degree', 'Send', 'Along', 'Western',
               'Focus', 'Support', 'Senior', 'Cause', 'Over', 'Raise', 'One', 'PM', 'Kid', 'Concern', 'Painting',
               'Throughout', 'Music', 'Sexual', 'Problem', 'Join', 'Tax', 'They', 'Interest', 'War', 'Energy', 'Until',
               'Kind', 'Deal', 'Structure', 'Free', 'Attorney', 'Young', 'Away', 'Loss', 'Human', 'Social', 'Same',
               'Bag', 'Beyond', 'Central', 'What', 'News', 'Third', 'Half', 'Wait', 'True', 'Power', 'Product', 'Know',
               'Story', 'Foot', 'Hospital', 'Performance', 'Next', 'Teach', 'Than', 'Director', 'Water', 'Exist',
               'Table', 'Laugh', 'Customer', 'Not', 'Arm', 'Much', 'Difficult', 'Above', 'Responsibility', 'Bed',
               'Upon', 'Real', 'White', 'Purpose', 'Body', 'Office', 'Agree', 'Provide', 'Official', 'Really', 'Matter',
               'We', 'Movie', 'Mention', 'Both', 'Top', 'Citizen', 'Research', 'When', 'Positive', 'Law', 'Meet',
               'Dinner', 'Enter', 'Specific', 'Mr', 'Control', 'May', 'Decision', 'Sort', 'Resource', 'Exactly',
               'Since', 'Hit', 'Current', 'Perform', 'Offer', 'Relationship', 'Whom', 'Shoulder', 'Campaign', 'Role',
               'Point', 'National', 'Deep', 'Day', 'Case', 'Rise', 'Direction', 'Trial', 'Size', 'Class', 'Democrat',
               'Box', 'Special', 'Simple', 'Plan', 'Including', 'Should', 'Clear', 'Wear', 'Cup', 'Nothing', 'Catch',
               'Reality', 'North', 'Fill', 'Agent', 'Particular', 'Head', 'Rather', 'Reason', 'College', 'Can', 'Yet',
               'Play', 'Natural', 'Sea', 'Which', 'Speak', 'Money', 'Put', 'Life', 'Occur', 'Score', 'Or', 'Pull',
               'Television', 'Morning', 'Father', 'Air', 'Everyone', 'Disease', 'Period', 'Entire', 'Drive', 'Mother',
               'Six', 'Single', 'Picture', 'Weapon', 'Win', 'Mission', 'Name', 'Create', 'Need', 'Chair', 'Rock',
               'Read', 'Term', 'Heat', 'Forward', 'Old', 'Miss', 'Decade', 'Live', 'Before', 'Finish', 'Against',
               'Hand', 'Soon', 'Area', 'Store', 'Find', 'Price', 'Plant', 'Page', 'Bank', 'Opportunity',
               'International', 'Centre', 'Keep', 'Fire', 'Message', 'Leave', 'Great', 'Southern', 'Machine',
               'Training', 'Nor', 'And', 'Likely', 'Book', 'Growth', 'After', 'Gas', 'Our', 'Small', 'Feeling', 'Now',
               'Share', 'According', 'Face', 'Side', 'Common', 'Especially', 'Among', 'Be', 'Author', 'Suggest',
               'Might', 'Environmental', 'Skill', 'Theory', 'Surface', 'Still', 'Carry', 'Pattern', 'None',
               'Professional', 'Reach', 'Pay', 'Manager', 'Little', 'Establish', 'Start', 'Take', 'Voice', 'Million',
               'Husband', 'Summer', 'Receive', 'If', 'Star', 'Grow', 'Who', 'Serve', 'Answer', 'Boy', 'Task', 'His',
               'Work', 'Go', 'Democratic', 'Them', 'Travel', 'Approach', 'Back', 'Worker', 'Build', 'Today', 'Stuff',
               'Discuss', 'Always', 'Enjoy', 'Race', 'Fact', 'Oil', 'Country', 'Leader', 'Ten', 'Agency', 'Ago', 'Mind',
               'Radio', 'Political', 'I', 'Fish', 'Sing', 'Rate', 'Fast', 'Fall', 'Themselves', 'Tend', 'Blood',
               'Everything', 'Pass', 'He', 'Others', 'Particularly', 'Successful', 'Policy', 'With', 'List', 'Letter',
               'Begin', 'Government', 'Watch', 'Any', 'Long', 'Behaviour', 'Yard', 'Kitchen', 'Yeah', 'Will',
               'Organization', 'Success', 'Level', 'Bad', 'Teacher', 'Night', 'Very', 'Team', 'Officer', 'Computer',
               'Financial', 'Society', 'Lay', 'Idea', 'Past', 'Last', 'Baby', 'Not', 'Identify', 'Time', 'Must',
               'Education', 'Age', 'Most', 'Election', 'Across', 'Style', 'Marriage', 'Rich', 'Often', 'West', 'Hot',
               'Building', 'As', 'Traditional', 'Economic', 'Town', 'Wish', 'Poor', 'Fail', 'Science', 'Consumer',
               'Discover', 'Parent', 'Experience', 'Economy', 'Group', 'Local', 'Improve', 'Argue', 'Beautiful', 'Act',
               'Significant', 'Alone', 'Audience', 'It', 'Right', 'Born', 'Street', 'Month', 'Three', 'Protect', 'Land',
               'Character', 'City', 'Technology', 'Song', 'Blue', 'How', 'Safe', 'Range', 'Hang', 'Affect', 'Wind',
               'Write', 'My', 'Violence', 'Final', 'Tonight', 'Child', 'Remove', 'Business', 'Into', 'Because',
               'Contain', 'Meeting', 'Newspaper', 'Smile', 'Two', 'Himself', 'Ability', 'Man', 'Maybe', 'Learn', 'Room',
               'Course', 'Season', 'Possible', 'Career', 'In', 'Someone', 'Their', 'Seek', 'Second', 'Security',
               'Break', 'Community', 'Item', 'But', 'Environment', 'Sense', 'Well', 'Activity', 'Language']

def play_beep(Type, box):
    if Type == 1:
        morse_keystrokes.append(".")
        box.update()
        Beep(700, 200)
    elif Type == 2:
        morse_keystrokes.append("_")
        box.update()
        Beep(700, 400)

def custom_font(size, systemfont=True, font="Aileron"):  # this returns a font with a customizable size and well font in as little as 14 charectors in comparison to at least 23
    if systemfont:
        return pygame.font.SysFont(font, size)
    else:
        return pygame.font.Font(font, size)

def changing_font(msg, max_width=350, font_color=Color("black")): # this is to return an appropriete text size value depending on the largest text fitting in a certain area
    def render(m, fc, f):
        textsurface = f.render(msg, True, fc)
        return textsurface.get_rect()
    textrect = render(msg, font_color, custom_font(60))[2]
    textrect2 = render(msg, font_color, custom_font(40))[2]
    if textrect >= max_width and textrect2 <= max_width:
        return 40
    elif textrect >= max_width and textrect2 >= max_width:
        return 20
    else:
        return 60

def check_word(text, string):
    word = list(text)
    broken_morse_word = []
    if " " in string:
        for i in range(string.count(" ")):
                string.remove(" ")
    else:
        print("Next time try using a space.")

    for i in range(len(word)):
        word[i] = word[i].capitalize()
    for i in range(len(word)):
        broken_morse_word.append(checking_dict.get(word[i]))

    if "".join(string) == "".join((broken_morse_word)):
        return True
    else:
        return False


class Button: # this class will be used to draw and interact with a Button.
    def __init__(self, x, y, w, h, color, border=0, round=False, text=None, Font=custom_font(60), Font_Color=Color("black")):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.border = border
        self.round = round
        self.text = text
        self.Font = Font
        self.Font_Color = Font_Color
        self.draw()

    def draw(self):
        if self.round == False:
            if self.border != 0:
                pygame.draw.rect(window, self.color, (self.x, self.y, self.w, self.h))
                pygame.draw.rect(window, Color("black"), (self.x, self.y, self.w, self.h), self.border)
                pygame.display.update()
            else:
                pygame.draw.rect(window, self.color, (self.x, self.y, self.w, self.h))
                pygame.display.update()
        elif self.round == True:
            if self.border != 0:
                aa_round_rect(window, (self.x, self.y, self.w, self.h), Color("black"), 30, self.border, self.color)
                pygame.display.update()
            else:
                aa_round_rect(window, (self.x, self.y, self.w, self.h), self.color, 30)
                pygame.display.update()
        if self.text != None:
            self.draw_text()

    def clicked(self):
        mouse = pygame.mouse.get_pos()
        if self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
            return True
        else:
            return False

    def draw_text(self):
        Label(self.text, self.x, self.y, self.w, self.h, self.Font, self.Font_Color)
        # Thanks for your time if your reading this


class Morse_Box:# this class is used to draw an updatable box which syncs with each morse code "key-stroke" and has a interactable delete button
    def __init__(self, x, y, w, h, color, dbc, border=0, font=custom_font(30), typing_font=custom_font(60), font_color=Color("black")):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.dbc = dbc  # acronym for delete button color
        self.border = border
        self.font = font
        self.typing_font = typing_font
        self.font_color = font_color
        self.draw()

    def draw(self):
        if self.border != 0:
            pygame.draw.rect(window, self.color, (self.x, self.y, self.w, self.h))
            pygame.draw.rect(window, Color("black"), (self.x, self.y, self.w, self.h), self.border)
            pygame.draw.rect(window, self.dbc, ((window_w - self.x) - (self.w / 15), self.y, self.w / 15, self.h))
            pygame.draw.rect(window, Color("black"), ((window_w - self.x) - (self.w / 15), self.y, self.w / 15, self.h),
                             self.border)
        else:
            pygame.draw.rect(window, self.color, (self.x, self.y, self.w, self.h))
            pygame.draw.rect(window, self.dbc, ((window_w - self.x) - (self.w / 15), self.y, self.w / 15, self.h))
        Label("DEL", self.x, self.y, self.w, self.h, self.font, self.font_color,
              (((window_w - self.x) - (self.w / 15) + ((self.w / 15) / 2)), (self.y + (self.h / 2))))
        Label("".join(morse_keystrokes), self.x, self.y, self.w, self.h, self.typing_font, self.font_color,
              ((self.x + ((self.w / 2) - (self.w / 15) + 35)), (self.y + (self.h / 2) - 10)))

    def update(self):
        if self.border != 0:
            pygame.draw.rect(window, self.color, (self.x, self.y, self.w, self.h))
            pygame.draw.rect(window, Color("black"), (self.x, self.y, self.w, self.h), self.border)
            pygame.draw.rect(window, self.dbc, ((window_w - self.x) - (self.w / 15), self.y, self.w / 15, self.h))
            pygame.draw.rect(window, Color("black"), ((window_w - self.x) - (self.w / 15), self.y, self.w / 15, self.h),
                             self.border)
        else:
            pygame.draw.rect(window, self.color, (self.x, self.y, self.w, self.h))
            pygame.draw.rect(window, self.dbc, ((window_w - self.x) - (self.w / 15), self.y, self.w / 15, self.h))
        Label("DEL", self.x, self.y, self.w, self.h, self.font, self.font_color,
              (((window_w - self.x) - (self.w / 15) + ((self.w / 15) / 2)), (self.y + (self.h / 2))))
        Label("".join(morse_keystrokes), self.x, self.y, self.w, self.h, self.typing_font, self.font_color,
              ((self.x + ((self.w / 2) - (self.w / 15) + 35)), (self.y + (self.h / 2) - 10)))

    def clicked(self):
        mouse = pygame.mouse.get_pos()
        if ((window_w - self.x) - (self.w / 15)) + self.w > mouse[0] > ((window_w - self.x) - (self.w / 15)) and self.y + self.h > mouse[1] > self.y:
            return True
        else:
            return False


class Typing_Box:
    def __init__(self, x, y, w, h, inactive_colour, active_colour):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.iac = inactive_colour
        self.ac = active_colour
        self.text = ""
        self.num = 0
        self.active = False
        self.draw()

    def draw(self):
        if self.active:
            colour = self.ac
        else:
            colour = self.iac
        pygame.draw.rect(window, colour, (self.x, self.y, self.w, self.h), 2)

    def update(self):
        if self.active:
            colour = self.ac
        else:
            colour = self.iac

        window.fill(Color("grey97"), (self.x, self.y, self.w, self.h))
        pygame.draw.rect(window, colour, (self.x, self.y, self.w, self.h), 2)
        self.text_label = Label(self.text, self.x, self.y, self.w, self.h, custom_font(changing_font(self.text)), alternate_center=((self.x + (self.w / 2) - 3), (self.y + (self.h / 2)-3)))
        pygame.display.update()

    def clicked(self):
        mouse = pygame.mouse.get_pos()
        if self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
            pygame.draw.rect(window, self.ac, (self.x, self.y, self.w, self.h), 2)
            pygame.display.update()
            return True
        else:
            pygame.draw.rect(window, self.iac, (self.x, self.y, self.w, self.h), 2)
            pygame.display.update()
            return False


class Label: # this class is quite simple it renders, centers and draws any given text on the screen including the ability to use alternate centering equations
    def __init__(self, msg, x, y, w, h, font, font_color=Color("black"), alternate_center=None):
        self.msg = msg
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.font = font
        self.font_color = font_color
        self.alternate_center = alternate_center
        self.draw()

    def render(self):
        textsurface = self.font.render(self.msg, True, self.font_color)
        return textsurface, textsurface.get_rect()

    def draw(self):
        self.textsurf, self.textrect = self.render()
        if self.alternate_center == None:
            self.textrect.center = ((self.x + (self.w / 2) - 3), (self.y + (self.h / 2)))

        elif self.alternate_center == 1:
            self.textrect.center = ((self.x + (self.textrect[2] / 2) - 3), (self.y + (self.textrect[3] / 2)))

        else:
            self.textrect.center = self.alternate_center
        window.blit(self.textsurf, self.textrect)
        pygame.display.update()


def main_screen(Word, Mode=None):
    window.fill(Color("grey97"))
    if button_text != "Default":
        b1_text, b_font_size = ".", custom_font(90)
        b2_text = "_"
    else:
        b1_text, b_font_size = "Dit", custom_font(70)
        b2_text= "Da"
    b1 = Button(20, 40, 450, 250, Color("grey80"), 2, True, b1_text, b_font_size)
    b2 = Button(20, 370, 450, 250, Color("grey80"), 2, True, b2_text, b_font_size)
    space = Button(180, 305, 130, 50, Color("grey80"), 2, False, "Space", custom_font(30))
    first_box = Morse_Box(150, 670, 1000, 55, Color("grey80"), Color("grey73"), 2)
    Your_Word = Label("Your word is:", 675, 310, 0, 0, custom_font(60))
    Word_Label = Label(Word, 675, 375, 0, 0, custom_font(changing_font(Word)))
    back = Button(-2, 677, 80, 50, Color("grey80"), 2, False, "Back", custom_font(30))
    tab = Button(1261, 20, 40, 645, (190, 190, 190), 1, False, "-", custom_font(40))
    run = True

    def tab_open(Word, Mode=Mode):
        window.fill(Color("grey97"))
        if button_text != "Default":
            b1_text, b_font_size = ".", custom_font(90)
            b2_text = "_"
        else:
            b1_text, b_font_size = "Dit", custom_font(70)
            b2_text= "Da"
        b1 = Button(20, 40, 450, 250, Color("grey80"), 2, True, b1_text, b_font_size)
        b2 = Button(20, 370, 450, 250, Color("grey80"), 2, True, b2_text, b_font_size)
        space = Button(180, 305, 130, 50, Color("grey80"), 2, False, "Space", custom_font(30))
        first_box = Morse_Box(150, 670, 1000, 55, Color("grey80"), Color("grey73"), 2)
        Your_Word = Label("Your word is:", 675, 310, 0, 0, custom_font(60))
        Word_Label = Label(Word, 675, 375, 0, 0, custom_font(changing_font(Word)))
        back = Button(-2, 677, 80, 50, Color("grey80"), 2, False, "Back", custom_font(30))
        cheatsheet = Button(861, 20, 440, 645, (210, 210, 210), 1, False)
        tab = Button(861, 20, 40, 645, (190, 190, 190), 1, False, "-", custom_font(40))
        num = 0
        for i in range(len(cheatsheettext)):
            num += 1
            if cheatsheettext[i] != ",":
                if i == 40:
                    num = 1
                if i >= 40:
                    cheatsheettextlabel = Label(cheatsheettext[i], 1100, (10 + (num * 30)), 0, 0, custom_font(25), Color("black"), 1)
                else:
                    cheatsheettextlabel = Label(cheatsheettext[i], 950, (10 + (num * 30)), 0, 0, custom_font(25), Color("black"), 1)
            else:
                num -= 1

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b1.clicked():
                        play_beep(1, first_box)
                    elif b2.clicked():
                        play_beep(2, first_box)
                    elif first_box.clicked():
                        global morse_keystrokes
                        morse_keystrokes = morse_keystrokes[:-1]
                        first_box.update()
                    elif tab.clicked():
                        run = not run
                        main_screen(Word)
                    elif back.clicked():
                        morse_keystrokes = []
                        first_menu()
                    elif space.clicked():
                        morse_keystrokes.append(" ")
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        morse_keystrokes = morse_keystrokes[:-1]
                        first_box.update()
                    elif event.key == pygame.K_RETURN:
                        if check_word(Word, morse_keystrokes):
                            print("Correct")
                        else:
                            print("False")
                        run = not run
                        morse_keystrokes = []
                        if Mode != None:
                            choose_word("")
                        else:
                            main_screen(choice(samplewords))
                    elif event.unicode == ".":
                        play_beep(1, first_box)
                    elif event.unicode == ",":
                        play_beep(1, first_box)
                    elif event.unicode == "_":
                        play_beep(2, first_box)
                    elif event.unicode == "-":
                        play_beep(2, first_box)
                    elif event.unicode == " ":
                        morse_keystrokes.append(" ")

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.clicked():
                    play_beep(1, first_box)
                elif b2.clicked():
                    play_beep(2, first_box)
                elif first_box.clicked():
                    global morse_keystrokes
                    morse_keystrokes = morse_keystrokes[:-1]
                    first_box.update()
                elif tab.clicked():
                    run = not run
                    tab_open(Word)
                elif back.clicked():
                    morse_keystrokes = []
                    first_menu()
                elif space.clicked():
                    morse_keystrokes.append(" ")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    morse_keystrokes = morse_keystrokes[:-1]
                    first_box.update()
                elif event.key == pygame.K_RETURN:
                    if check_word(Word, morse_keystrokes):
                        print("Correct")
                    else:
                        print("False")
                    run = not run
                    morse_keystrokes = []
                    if Mode != None:
                        choose_word("")
                    else:
                        main_screen(choice(samplewords))
                elif event.unicode == ".":
                    play_beep(1, first_box)
                elif event.unicode == ",":
                    play_beep(1, first_box)
                elif event.unicode == "_":
                    play_beep(2, first_box)
                elif event.unicode == "-":
                    play_beep(2, first_box)
                elif event.unicode == "=":
                    play_beep(2, first_box)
                elif event.unicode == "+":
                    play_beep(2, first_box)
                elif event.unicode == " ":
                    morse_keystrokes.append(" ")

def choose_word(Typing_Strokes):
    window.fill(Color("grey97"))
    if button_text != "Default":
        b1_text, b_font_size = ".", custom_font(90)
        b2_text = "_"
    else:
        b1_text, b_font_size = "Dit", custom_font(70)
        b2_text= "Da"

    b1 = Button(20, 40, 450, 250, Color("grey80"), 2, True, b1_text, b_font_size)
    b2 = Button(20, 370, 450, 250, Color("grey80"), 2, True, b2_text, b_font_size)
    Your_Word = Label("Your word is:", 675, 310, 0, 0, custom_font(60))
    input_box = Typing_Box(500, 350, 350, 50, Color("black"), Color("blue"))
    back = Button(-2, 677, 80, 50, Color("grey80"), 2, False, "Back", custom_font(30))
    tab = Button(1261, 20, 40, 645, (190, 190, 190), 1, False, "-", custom_font(40))
    run = True

    def tab_open(Typing_Strokes):
        window.fill(Color("grey97"))
        if button_text != "Default":
            b1_text, b_font_size = ".", custom_font(90)
            b2_text = "_"
        else:
            b1_text, b_font_size = "Dit", custom_font(70)
            b2_text= "Da"

        b1 = Button(20, 40, 450, 250, Color("grey80"), 2, True, b1_text, b_font_size)
        b2 = Button(20, 370, 450, 250, Color("grey80"), 2, True, b2_text, b_font_size)
        Your_Word = Label("Your word is:", 675, 310, 0, 0, custom_font(60))
        input_box = Typing_Box(525, 350, 300, 50, Color("black"), Color("blue"))
        back = Button(-2, 677, 80, 50, Color("grey80"), 2, False, "Back", custom_font(30))
        cheatsheet = Button(861, 20, 440, 645, (210, 210, 210), 1, False)
        tab = Button(861, 20, 40, 645, (190, 190, 190), 1, False, "-", custom_font(40))
        num = 0
        for i in range(len(cheatsheettext)):
            num += 1
            if cheatsheettext[i] != ",":
                if i == 40:
                    num = 1
                if i >= 40:
                    cheatsheettextlabel = Label(cheatsheettext[i], 1100, (10 + (num * 30)), 0, 0, custom_font(25), Color("black"), 1)
                else:
                    cheatsheettextlabel = Label(cheatsheettext[i], 950, (10 + (num * 30)), 0, 0, custom_font(25), Color("black"), 1)
            else:
                num -= 1
        active = False
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if tab.clicked():
                        run = not run
                        choose_word(Typing_Strokes)

                    elif back.clicked():
                        run = not run
                        morse_keystrokes = []
                        first_menu()
                if event.type == pygame.KEYDOWN and input_box.active:
                    if event.key == pygame.K_RETURN:
                        main_screen(input_box.text, 1)

                    elif event.key == pygame.K_BACKSPACE:
                        input_box.text = input_box.text[:-1]
                        input_box.update()

                    else:
                        if event.unicode in characters:
                            input_box.text += event.unicode
                        input_box.update()
    active = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tab.clicked():
                    run = not run
                    tab_open(Typing_Strokes)
                elif input_box.clicked():
                    input_box.active = not input_box.active

                elif back.clicked():
                      run = not run
                      input_box.text = ""
                      first_menu()
                else:
                    input_box.active = False
            if event.type == pygame.KEYDOWN and input_box.active:
                    if event.key == pygame.K_RETURN:
                        main_screen(input_box.text, 1)

                    elif event.key == pygame.K_BACKSPACE:
                        input_box.text = input_box.text[:-1]
                        input_box.update()

                    else:
                        if event.unicode in characters:
                            input_box.text += event.unicode
                        input_box.update()


def first_menu():
    window.fill(Color("grey97"))
    prompt = Label("Would you like a word generated for you?", window_w/2, 150, 0, 0, custom_font(50))
    yes = Button(150, 300, 400, 225, Color("grey80"), 1, True, "Yes")
    no = Button(750, 300, 400, 225, Color("grey80"), 1, True, "No")
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if yes.clicked():
                    run = not run
                    chose_own = False
                    main_screen(choice(samplewords))
                elif no.clicked():
                    run = not run
                    chose_own = True
                    choose_word("")
                

if __name__ == "__main__":
    first_menu()
