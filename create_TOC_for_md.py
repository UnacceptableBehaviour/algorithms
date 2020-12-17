#! /usr/bin/env python
# 3.7
# create MD for TOC
# set DEFAULT_DOC_TO_PROCESS to relevant RTF course notes
# DEFAULT_README_NO_EQUATIONS     = Path('./README.md') # < in not using equations
# DEFAULT_README_RENDER_TEX_LOCAL = Path('./README.md') # < tex processed locally to svg pushed to git
                                                        # links inserted in md then also pushed.
# DEFAULT_README_TEXIFY = Path('./README.tex.md')       # < if Texify installed (on GitHub) it will convert
                                                        # tex into equations on git

# passing a .md file as argument will print a TOC for that file

import os
import subprocess
import re
from pprint import pprint
import sys                          # argv
#from pprint import  pprint

from pathlib import Path

# RTF conversion to text
from striprtf.striprtf import rtf_to_text

# Rendering SVG from tex
from render import render           # import from local render
#from readme2tex import render      # import from adapted readme2tex module

# convert RTF to txt
def get_text_content_of_file(rtf_filepath):
    
    with open(rtf_filepath,'r') as f:
        rtf = f.read()
            
    return rtf_to_text(rtf)             # convert to text and return


def create_toc_link_text(title):
    
    # downcase, remove all non alphanumeric, replace space with hyphen
    # leave hyphens in!
    toc_link_text = title.strip().strip("\\").lower()
    toc_link_text = re.sub(r'[^a-z 0-9\-]', '', toc_link_text)
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


#DEFAULT_DOC_TO_PROCESS = Path('context.md')
DEFAULT_DOC_TO_PROCESS = Path('/Users/simon/a_syllabus/_COURSES_00_WIP/ALGO_00_Intro_2_Algorithms_MIT.rtf')
def get_mark_down(filename=DEFAULT_DOC_TO_PROCESS):
    
    print(f"FILE_LOC***\n***\n{filename}\n***\n***\n")
    
    with open(filename) as f:
        content = f.read()

    # incase string passed in
    if Path(filename).suffix == '.rtf':
        content = rtf_to_text(content)
    else:
        print(f"> > > > - - - - - - - - - - < < < < {Path(filename)} {filename} {Path(filename).suffix} > > > >")

    replacement = ''
    # remove anything inside 'comment' delimiters //* this is a comment *//
    content =  re.sub(r'\/\/\*.*?\*\/\/', replacement, content, flags = re.MULTILINE | re.DOTALL)

    # debug verify comment removal
    # for line in iter(content.splitlines()):
    #     print(line)
    # 
    # print("\n\n\n**8**\n\n\n")
    
    return content        
    

DEFAULT_README_RENDER_TEX_LOCAL = Path('./README.md')
DEFAULT_README_TEXIFY = Path('./README.tex.md')    # if Texify installed it will convert the Latex into equations
target_readme_on_git = DEFAULT_README_RENDER_TEX_LOCAL

def save_text_w_toc_to_readme(text, toc_string):
    global target_readme_on_git
    
    replacement = "## Contents  \n" + toc_string + "\n\n## AIM:  \n"
    
    #print(f"***\n***\n{replacement}\n***\n***\n")
    
    text = re.sub(r'^## Contents.*?## AIM:.*?$', replacement, text, flags = re.MULTILINE | re.DOTALL)
        
    print(f"***\n***\n WRITING TO: {target_readme_on_git}\n***\n***\n***\n***\n***\n***\n")
    with open(target_readme_on_git, 'w') as f:
        f.write(text)

    return text


tex_count = 0
DEFAULT_SVG_LATEX = Path('./scratch/tex')
def process_tex_to_svg(match):#, image_dir=DEFAULT_SVG_LATEX):
    global tex_count
    tex_count += 1
    readme = str(match.group(0))    

    # https://tex.stackexchange.com/questions/255470/compile-tex-directly-into-svg-using-the-command-line
    #
    # line from texify
    # let readme2tex = `python -m readme2tex --nocdn --output ./scratch/tex --project ${this.push.repository.name} --svgdir ./scratch/svg --username ${this.push.repository.owner.name} ${tmpInputPath}`
    #
    # installed reeadmetex - https://pypi.org/project/readme2tex/
    # python -m readme2tex --nocdn --output ${tmpOutputPath} --project ${this.push.repository.name} --svgdir ${svgOutputPath} --username ${this.push.repository.owner.name} ${tmpInputPath}`
    
    # this generates svg file
    # python -m readme2tex --nocdn --output ./scratch/tex/tag.tex   --svgdir ./scratch/svg  --readme ./scratch/tex/fmla.tex
    # reads fmla.tex                --readme
    # puts svg file in directory    --svgdir    < this should be in the repo
    # creates a <p> tag             --output
    # w/ all relevant info!
    # <p align="center"><img src="./scratch/svg/5d6fc5fa4e2ff9cc622d301b8d56c147.svg?invert_in_darkmode" align=middle width=545.4986691pt height=156.4653783pt/></p>
    
    # pip install readme2tex
    # parser = argparse.ArgumentParser(prog='python -m readme2tex', description='Render LaTeX in Github Readmes', epilog=epilog, formatter_class=argparse.RawDescriptionHelpFormatter)
    # parser.add_argument('--readme', nargs='?', type=str, help="The Markdown input file to render.")
    # parser.add_argument('--engine', type=str, default="latex")
    # parser.add_argument('--output', type=str, default="README_GH.md", help="The output file. Defaults to README_GH.md")
    # parser.add_argument('--usepackage', type=str, action='append', default=['amsmath', 'amssymb'], help="Include a LaTeX package. Comes with amsmath and amssymb.")
    # parser.add_argument('--svgdir', type=str, default='svgs', help="Name of the folder to save the output svgs into. Defaults to svgs.")
    # parser.add_argument('--branch', type=str, help="[EXPERIMENTAL] Which branch to save the svgs into. Used by the git-hook system. Defaults to the current branch.")
    # parser.add_argument('--username', type=str, help="Github username. Can be inferred.")
    # parser.add_argument('--project', type=str, help="Github project. Can be inferred.")
    # parser.add_argument('--nocdn', action='store_true', help="Use local relative path rather than rawgit's CDN. Useful for debugging.")
    # parser.add_argument('--htmlize', action='store_true', help="Output a md.html file for you to preview. Useful for debugging.")
    # parser.add_argument('--valign', action='store_true', help="Use the valign attribute instead of the align=middle trick. Only works on Chrome.")
    # parser.add_argument('--rerender', action='store_true', help="Even if equations have already been compiled, recompile them anyways.")
    # parser.add_argument('--bustcache', action='store_true', help="Github has a latency before it will serve up the new asset. This option allows us to circumvent its caching.")
    # parser.add_argument('--add-git-hook', action='store_true', help="Automatically generates a post-commit git hook with the rest of the arguments. In the future, git commit will automatically trigger readme2tex if the input file is changed.")
    # parser.add_argument('input', nargs='?', type=str, help="Same as --readme")
    # 
    # render(               def render(                              args Namespace
    #     readme,                   readme,                               readme='./scratch/tex/fmla.tex',
    #     args.output,              output='README_GH.md',              # output='./scratch/tex/tag.tex',
    #     args.engine,              engine='latex',                     # engine='latex',              
    #     args.usepackage,          packages=('amsmath', 'amssymb'),    # usepackage=['amsmath', 'amssymb'],
    #     args.svgdir,              svgdir='svgs',                      # svgdir='./scratch/svg',
    #     args.branch,              branch=None,                        # branch=None,
    #     args.username,            user=None,                          # username=None,
    #     args.project,             project=None,                       # project=None,
    #     args.nocdn,               nocdn=False,                        # nocdn=True,
    #     args.htmlize,             htmlize=False,                      # htmlize=False,
    #     args.valign,              use_valign=False,                   # valign=False,
    #     args.rerender,            rerender=False,                     # rerender=False,
    #     args.bustcache)           bustcache=False):                   # bustcache=False,
                                                                          
    # readme                                                              add_git_hook=False,
    # './scratch/tex/fmla.tex'                                            input=None,
    # args
    # Namespace(add_git_hook=False, branch=None, bustcache=False, engine='latex', htmlize=False,
    #           input=None, nocdn=True, output='./scratch/tex/tag.tex', project=None,
    #           readme='./scratch/tex/fmla.tex', rerender=False, svgdir='./scratch/svg',
    #           usepackage=['amsmath', 'amssymb'], username=None, valign=False)
    
    args = {  #'readme': './scratch/tex/fmla.tex',
              'output': './scratch/tex/tag.tex',    # <p> tag - retrieved from render directly
              'engine': 'latex',              
              'usepackage': ['amsmath', 'amssymb'],
              'svgdir': './tex',                    # 'svgdir': './scratch/svg',
              'branch': None,
              'username': None,
              'project': None,
              'nocdn': True,
              'htmlize': False,
              'valign': False,
              'rerender': False,
              'bustcache': False }
                                        # instead of writing to file & reading it back 
    #readme = './scratch/tex/fmla.tex'  # readme = str(match.group(0))  above
    #readme = './scratch/tex/fmla.tex'  # requires interface change - uber hack
    
    insert_svg_link = render(            
                        readme,        
                        args['output'],   
                        args['engine'],   
                        args['usepackage'],
                        args['svgdir'],   
                        args['branch'],   
                        args['username'], 
                        args['project'],  
                        args['nocdn'],    
                        args['htmlize'],  
                        args['valign'],   
                        args['rerender'], 
                        args['bustcache'])
    
    #print("SEARCH_TAGC")    
    #print(f"== {tex_count}:\n{readme}\n|\n{insert_svg_link}\n\n")
    return(insert_svg_link)

    # using a remote server service
    # https://stackoverflow.com/questions/9588261/converting-a-latex-code-to-mathml-or-svg-code-in-python
    
    # is there something up with githooks stopping Texify running?
    # is there
    
    
if __name__ == '__main__':
    
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # 
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    
    # title = 'Logarithms - identities & basic manipulation'    # < EG title
    # link_sb = 'logarithms---identities--basic-manipulation'   # < How link should look
    # link = create_toc_link_text(title) 
    # print(link_sb)
    # print(link)
    # print(link == link_sb)
    #     
    # sys.exit(0)
    
    report = f"PWD: {os.getcwd()}"    
    print("sys.argv -- S")
    pprint(sys.argv)
    print("sys.argv -- E")
    
    scan_for_latex = True
    if '-texify' in sys.argv:
        scan_for_latex = False
        target_readme_on_git = DEFAULT_README_TEXIFY        
        sys.argv.remove('-texify')
        report += "\n** -texify: relying gitapp texify to insert SVG equations **"
    else:
        target_readme_on_git = DEFAULT_README_RENDER_TEX_LOCAL
        report += "\n** -localtex: insert tex > SVG equations locally - requires latex installed **"
    
    
    push_to_repo = False
    if '-p' in sys.argv:
        push_to_repo = True        
        sys.argv.remove('-p')
        report += "\n** -p: PUSHING TO REPO **"
    
    # sys.argv[0] is name of this file

    # TODO - FIX THIS LOGIC - add arg processing module or option followed by file
    if len(sys.argv) > 1 and Path(sys.argv[1]).exists():  
        report += f"\nCreating TOC for command line parameter: {sys.argv[1]} <"
        text = get_mark_down(sys.argv[1])
            
    else: 
        report += f"\n* * USING DEFAULT FILE * * - Creating toc FROM {DEFAULT_DOC_TO_PROCESS}"
        text = get_mark_down()
    
    if scan_for_latex:
        text = re.sub(r'^\$\$(.*?)^\$\$', process_tex_to_svg, text, flags = re.MULTILINE | re.DOTALL)
    
    toc = create_TOC_from_text(text)

    toc_string = create_TOC_as_string_from_TOC_nested_list(toc)

    print(save_text_w_toc_to_readme(text, toc_string))
    #save_text_w_toc_to_readme(text, toc_string)
        
    return_code = 'WARNING: No push to git!'
    
    if push_to_repo:
        commit_comment = input("Commit comment:")
                
        if scan_for_latex:            
            return_code = subprocess.call(['git','add','tex/*.svg']) # note command separation inside list! [ ]
            print(f"git add tex/*.svg: {return_code}")                         
        
        return_code = subprocess.call(['git','add',target_readme_on_git]) # note command separation inside list! [ ]
        print(f"git add {DEFAULT_README_TEXIFY}: {return_code}")           # ^----/
            
        return_code = subprocess.call(["git","commit",f"-m autogen {target_readme_on_git}:{commit_comment}"])
        print(f"git commit -m'autogen {target_readme_on_git}: {commit_comment}'")
    
        return_code = subprocess.call(['git','push'])
        print(f"git push: {return_code}")        
    else:
        print(f"\n\n{return_code}\n")
    
    
    #print(f"\n\n{toc_string}\n\n")
    
    print(f"\n\nREPORT / NOTES:\n{report}")