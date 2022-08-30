import pandas as pd
import sys
import re
import json
import copy



# -*- coding: utf-8 -*-


#import plotly.express as px
#import plotly.graph_objects as go







#parse_page([filepath, number_word_separator, substrings, 1])
#	filepath = './Lexique383_140k_fr.it.v4.v9.txt'
#	filepath_fr = './Lexique383_140k_fr.v4.v1.txt'
def parse_page(array_arg):
	
	
	filepath=array_arg[0]
	number_word_separator=array_arg[1]
	current_substring=array_arg[2]
	verbose=array_arg[3]
	
	dir_out='/media/bender/dsk3/workspace_all/small_project_etc/small_projects_current/similarity_german_italian_etc/ger_words_grouped/'
	
	new_matrix=[]
	with open(filepath, 'r', encoding='utf8') as file: file_as_string = file.read()
	file_as_strings_matrix = file_as_string.split('\n')
	file_as_strings_matrix_v2=[]	
	file_result = open(dir_out+current_substring+".txt", "w")
	file_result.write(current_substring)
	file_result.write('\n')

	for j in range(0,len(file_as_strings_matrix)):
		line=file_as_strings_matrix[j]
		if line==None: continue
	
		#print('\n', line, '\n')
		current_line_splitted=line.split(number_word_separator)
		if len(current_line_splitted)<2: continue
	
		current_ger_word=current_line_splitted[0].lower()
		current_ita_word=current_line_splitted[1].lower()
		current_line_splitted[0]=current_ger_word
		current_line_splitted[1]=current_ita_word
		
		
		
		#x = re.search("^The.*Spain$", txt)
		#search_expression='['+current_substring+']'
		search_expression=current_substring
		search_result = re.search(search_expression, current_ger_word)
		if search_result==None: continue 
		'''
		print('\n')
		print('\n')
		print('\n')
		print(search_expression)
		print(search_result)
		print(current_ger_word)
		'''
		
		
		#current_line_splitted.append(current_substring)
		current_line_new=number_word_separator.join(current_line_splitted)			
		file_result.write(current_line_new)
		file_result.write('\n')
		
		
		#print('\n')
		
		#line3=number_word_separator.join(current_line_splitted)	
		#new_matrix.append(line3)
		#print(line3)
		#print(new_line_array)
	file_result.close()
	return None


				


############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################


	

	


#run script	
substrings=['acke','atte','ergi','erke','rtig','huld','beit','isti','fäll','itze','klic','glei','anke','chna','annt','rate','hlag','oche','ekti','eins','einz','erfa','ziel','ünde','chme','spri','mmen','bsch','gebr','gela','ngen','rtra','arbe','zeic','ndel','iefe','prec','ausz','trag','erau','ssen','steh','offe','brau','renn','dreh','anne','laub','erre','eder','inst','gefä','usam','tere','komp','chlu','rspr','ahre','eleg','getr','span','stat','stie','achs','kenn','ngel','scho','star','ante','ment','zahl','ächt','igen','rtei','wand','risc','ntsc','wach','geri','gewi','vere','verz','stei','erse','geme','änge','ndig','nger','anti','rbei','entl','kann','trie','misc','erne','ling','verh','lage','nhei','anis','mein','eise','ühre','rder','ehme','eife','piel','iehe','spre','rauc','frei','eibe','leid','wund','illi','enne','erze','rier','gefa','vier','fall','sehe','arte','hrei','schü','haft','aube','eben','ktio','gend','chwi','enti','miss','abge','gege','aufe','reis','esti','ände','gese','nste','tänd','stän','ucht','uche','leit','chle','weis','olle','mmer','lang','samm','gkei','iert','dige','igke','leic','verk','erwe','zier','ermi','ensc','akti','arti','iebe','iter','erha','ress','orde','weit','verm','vera','vors','zurü','urüc','imme','ione','teri','lege','tter','folg','inne','ache','icke','erwa','dlic','voll','chul','ecke','gesp','igun','echt','bere','blic','egen','mach','htig','lieb','reic','ersp','rein','chau','tion','reit','spie','chen','ufge','chri','schä','erte','erbr','reib','alle','gene','auch','eist','eine','trau','ters','nehm','trei','asch','nisc','nges','aufg','ring','betr','nier','mitt','fahr','such','zieh','nlic','eige','ents','iede','iege','chre','rach','stra','gele','gehe','stan','teil','sier','vert','chwe','durc','erla','verf','führ','setz','erli','amme','erei','hand','inte','chne','ster','stre','eche','best','ette','urch','usch','erun','rlic','auss','eide','chie','verw','cher','verd','raus','isse','chli','schm','lass','nach','verg','gebe','iste','chti','esse','halt','besc','chei','elle','gest','rste','ertr','itte','erle','tige','inde','erge','usge','omme','nsch','asse','tier','rich','sich','unde','chaf','chla','schn','acht','eing','alte','este','atio','verb','tlic','tisc','rück','verl','ausg','schu','ande','komm','tsch','tell','stel','rech','ende','schr','nder','eich','ersc','erst','über','gesc','unge','schi','unte','inge','schw','iere','icht','eite','ange','nter','scha','iche','chte','rsch','esch','vers','lich','isch','schl','sche']





number_word_separator=';;'
filepath = '/media/bender/dsk3/workspace_all/small_project_etc/small_projects_current/similarity_german_italian_etc/000_data_delete/ig_similarity_ger.txt'
verbose=1



def loop_over_substrings(array_arg):
	
	filepath=array_arg[0]
	number_word_separator=array_arg[1]
	substrings=array_arg[2]
	verbose=array_arg[3]
	
	
	for j in range(0,len(substrings)):
		current_substring=substrings[j]
		parse_page([filepath, number_word_separator, current_substring, verbose])






array_arg=[filepath, number_word_separator, substrings, verbose]

loop_over_substrings(array_arg)






