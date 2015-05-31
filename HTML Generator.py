
#This program will take make HTML code for notes that were taken over an entire single stage of the nanodegree

#PLEASE SEE README FILE FOR EXPLANATION OF FUNCTIONALITY

file_contents = open("cleantext.txt")
text = file_contents.read()

def del_ASCII():  #found that the quotes from google doc are "\xe2" and are 3 characters long; wrote this code to replace them with normal quotes
        contents = open("dirtytext.txt")
        txt = contents.read()
        while txt.find("\xe2") != -1:
                location = txt.find("\xe2")
                txt = txt[0:location] + "\"" + txt[location+3:]
        file = open("cleantext.txt", "w")
        file.write(txt)

def get_lesson(txt, number): #pulls a lesson by number
        counter = 1
        end = 0
        while counter <= number:
                start = txt.find("L*", end)
                end = txt.find("L*", start + 1)
                if start == -1: 
                        return -1   #this is the signal I used to let the program know there are no more lessons to pull; same strategy used later
                counter += 1
        return txt[start:end] + "\n"

def get_title(txt): #pulls the title of a lesson
        start = txt.find("L*")
        end = txt.find("\n")
        title = txt[start+2:end]               
        return title

def get_concept(txt, number): #pulls a concept by number from a lesson
        counter = 1
        end = 0
        while counter <= number:
                start = txt.find("C*", end)
                end = txt.find("C*", start + 1)
                if start == -1:
                        return -1
                counter += 1
        return txt[start:end] 


def concept_title (txt): #pulls the title of a concept
        start = txt.find("C*")
        end = txt.find("\n")
        return txt[start+2:end]

def concept_details (txt): #pulls the bulleted details from a concept and stores them them sequentially into a list
        if txt.find("B*") == -1:
                return -1
        details_list = []
        begin = txt.find("B*")
        details = txt[begin+2:]
        firstline = details[0:details.find("\n")]
        details_list.append(firstline)
        details = details[details.find("\n"):]
        while details.find("\n",1) != -1:
                line = details[1:details.find("\n", 1)]
                details_list.append(line)
                details = details[details.find("\n", 1):]
        return details_list

def html_gen(title, details): #generates HTML for a single concept, including its title and details
        text1 ='''
<div class="subtopic">
  <div class="header2">''' + title + '</div>'
        text2 = '''
  <div class = "text">'''
        text3 = ''
        text4 = '''
  </div>
</div>'''
        text5 = '''
</div>'''
        if details == -1:
                return text1 + text5
        for x in details:
                text3 += '''
    <p>
      ''' + x + '''
    </p>'''
        return text1 + text2 + text3 + text4

def code_lesson(txt): # sequentially runs the html_gen function for each concept in a lesson and adds them together to form code for an entire lesson
        counter = 1
        lesson_code = ''
        while get_concept (txt, counter) != -1:
                concept = get_concept(txt, counter)
                title = concept_title(concept)
                details = concept_details(concept)
                lesson_code += html_gen(title, details)
                counter += 1
        return lesson_code

def code_stage(txt): #sequentially runs the code_lesson function for each lesson in a  stage, then adds them together to form code for an entire stage
        counter = 1
        stage_code = ''
        while get_lesson(txt, counter) != -1:
                lesson = get_lesson(txt, counter)
                title = get_title(lesson)
                lesson_html = code_lesson(lesson)
                stage_code += '''
<h1>''' + title + '</h1>'
                stage_code+= lesson_html
                counter += 1
        return stage_code

print code_stage(text) #outputs the HTML code for the entire stage


                





