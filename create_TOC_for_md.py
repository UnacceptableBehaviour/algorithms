#! /usr/bin/env python
# 3.7
# create MD for TOC


import os
import subprocess
import re
from pprint import pprint
import sys                          # argv
#from pprint import  pprint

from pathlib import Path

# RTF conversion to text
from striprtf.striprtf import rtf_to_text

# convert RTF to txt
def get_text_content_of_file(rtf_filepath):
    
    with open(rtf_filepath,'r') as f:
        rtf = f.read()
            
    return rtf_to_text(rtf)             # convert to text and return


def create_toc_link_text(title):
    
    # downcase, remove all non alphanumeric, replace space with hyphen
    toc_link_text = title.strip().strip("\\").lower()
    toc_link_text = re.sub(r'[^a-z 0-9]', '', toc_link_text)
    toc_link_text = re.sub(r' ', '-', toc_link_text)
    
    return toc_link_text


MAX_NO_CONTENT_ITEMS_PER_INDENT = 100   
MAX_INDENT_DEPTH = 12
FRONT_OF_QUEUE = 0
INDENT_DEPTH = 0
LINK_LINE = 1

def create_indented_md_link_lines(link_tuples, indent=1):    
    if indent > MAX_INDENT_DEPTH: return
    
    toc_lines = []    
    bullet = 1

    while(len(link_tuples) > 0):
        #print(f"INDENT:{indent} - len(link_tuples):{len(link_tuples)}")
        
        if( link_tuples[FRONT_OF_QUEUE][INDENT_DEPTH] == indent ):
            # pop it
            line = link_tuples.pop(FRONT_OF_QUEUE)
            
            # create toc line            
            tabs ="\t" * (indent - 1)
            print(f"{tabs}{bullet}. {line[LINK_LINE]}")
            toc_lines.append(f"{tabs}{bullet}. {line[LINK_LINE]}")            
            
            bullet += 1
            
            
        elif( link_tuples[FRONT_OF_QUEUE][INDENT_DEPTH] > indent ):
            # call this function to go to next level
            toc_lines.append( create_indented_md_link_lines(link_tuples, indent+1) )
        else:
            # return to go to down a level
            return toc_lines

        
    return toc_lines
    


def create_TOC_from_text(text):

    replacement = ''
    links_with_no_of_indents = []
    
    # how to enumerate - replacement with a tag? for later returning snippet?
    # remove code snippets
    text_lite = re.sub(r'^```.*?```', replacement, text, flags = re.MULTILINE | re.DOTALL)
    
                                    # match for one or more # and title
    collect_toc_lines = re.findall(r'^(#+)(.*?)$', text_lite, flags = re.MULTILINE | re.DOTALL)
    
    #print('\n\n> found - - - - S\n')
    for m in collect_toc_lines:
        #print(f"[{m[1].strip()}](#{create_toc_link_text(m[1])})\\")
        #print(m)
        
        md_href = f"[{m[1].strip()}](#{create_toc_link_text(m[1])})"
        
        links_with_no_of_indents.append( (len(m[0]) - 1,md_href) )
    
    links_with_no_of_indents.pop(0) # remove headline    
    
    indented_md_hrefs = create_indented_md_link_lines(links_with_no_of_indents)
       
    return indented_md_hrefs 
    
# Look at how to do this with functools.reduce()
# https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
#
def create_TOC_as_string_from_TOC_nested_list(toc_list):
    lines = ""
    
    for l in toc_list:
        if type(l).__name__ == 'str':
            lines += f"{l}  \n"
        elif type(l).__name__ == 'list':
            lines += create_TOC_as_string_from_TOC_nested_list(l)

    return lines


#DEFAULT_FILE = Path('context.md')
DEFAULT_FILE = Path('/Users/simon/a_syllabus/_COURSES_00_WIP/ALGO_00_Intro_2_Algorithms_MIT.rtf')
def get_mark_down(filename=DEFAULT_FILE):
        
    with open(filename) as f:
        content = f.read()

    # incase string passed in
    if Path(filename).suffix == '.rtf':
        content = rtf_to_text(content)
    else:
        print(f"> > > > - - - - - - - - - - < < < < {Path(filename).suffix} > > > >")

    replacement = ''
    # remove anything inside 'comment' delimiters //* this is a comment *//
    content =  re.sub(r'\/\/\*.*?\*\/\/', replacement, content, flags = re.MULTILINE | re.DOTALL)

    for line in iter(content.splitlines()):
        print(line)
    
    print("\n\n\n\n\n\n")
    
    return content        
    

#DEFAULT_README = Path('./README.md')
DEFAULT_README = Path('./README.tex.md')    # if Texify installed it will convert the Latex into equations
def save_text_w_toc_to_readme(text, toc_string):
    
    replacement = "## Contents  \n" + toc_string + "\n\n## AIM:  \n"
    
    print(f"***\n***\n{replacement}\n***\n***\n")
    
    text = re.sub(r'^## Contents.*?## AIM:.*?$', replacement, text, flags = re.MULTILINE | re.DOTALL)

    with open(DEFAULT_README, 'w') as f:
        f.write(text)

    return text
    
    
    
if __name__ == '__main__':
    
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # 
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    report = f"PWD: {os.getcwd()}"
    
    # sys.argv[0] is name of this file

    if len(sys.argv) > 1 and Path(sys.argv[1]).exists():  
        report += f"\nCreating TOC for {sys.argv[1]}"
        text = get_mark_down(sys.argv[1])
            
    else: 
        report += f"\n* * USING DEFAULT FILE * * - Creating TOC for {DEFAULT_FILE}"
        text = get_mark_down()
    

    toc = create_TOC_from_text(text)

    toc_string = create_TOC_as_string_from_TOC_nested_list(toc)

    print(save_text_w_toc_to_readme(text, toc_string))
        
    return_code = 'WARNING: No push to git!'
    if '-p' in sys.argv:
        return_code = subprocess.call(['git','add',DEFAULT_README]) # note command separation inside list! [ ]
        print(f"git add {DEFAULT_README}: {return_code}")          # ^----/
    
        return_code = subprocess.call(["git","commit","-m'added autogenerated {DEFAULT_README}'"])
        print(f"git commit -m'added autogenerated {DEFAULT_README}': {return_code}")
    
        return_code = subprocess.call(['git','push'])
        print(f"git push: {return_code}")        
    else:
        print(f"\n\n{return_code}\n")
    
    print(f"\n\n{report}")