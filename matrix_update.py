#!/usr/bin/python

import subprocess
import os
import re

import gdcc_conf

TEMPLATE_DIR=os.path.join(gdcc_conf.WWW_ROOT, "matrix_template")
TEMPLATE_FILE=os.path.join(TEMPLATE_DIR, "matrix.pdf")
MATRIX_TABLE_FILE=os.path.join(TEMPLATE_DIR, "autogeneratedtable.tex")

PDFLATEX_CMD = ["pdflatex", "matrix"]

print("Updating Game Documentation Matrix..." + TEMPLATE_FILE)

def find_tex_files():
	texfiles = []
	for root, dirs, files in os.walk(gdcc_conf.GDD_DIR):
    		for filename in files:
        		if filename.endswith(".tex"):
             			texfiles.append(os.path.join(root, filename))
	return texfiles

def find_features_in_tex_file(filename):
	found_features = []
	f = open(filename, 'r')
	for line in f.xreadlines():
		match = line.find("\\newcommand{\\feature")
		if match > -1:
			continue

		match = line.find("\\feature")
		if match > -1:
			feature_name = extract_feature_name(line[match:])
			found_features.append(feature_name)
	f.close()
	return found_features

def extract_feature_name(string):
	feature_name = ""
	found_start_curly_brace = False
	for char in string:
		if char == "{":
			found_start_curly_brace = True
			continue
		if char == "}":
			if feature_name == "":
				raise Exception("Failed to parse \\feature{X} - " +
					"Missing starting curly brace?")
			return feature_name
		if found_start_curly_brace:
			feature_name += char
	raise Exception("Failed to parse \\feature{X} - Missing ending curly brace?")

def find_source_files(source_dir, valid_ext):
	source_files = []
	for root, dirs, files in os.walk(source_dir):
    		for filename in files:
			if filename.find(".git") != -1:
				continue
			if filename_has_ext(filename, valid_ext):
             			source_files.append(os.path.join(root, filename))
	return source_files

def find_features_in_source_file(comment, filename):
	found_features = []
	f = open(filename, 'r')
	for line in f.xreadlines():
		match = line.find(comment + "@ImplementsFeature")
		if match > -1:
			feature_name = extract_feature_name(line[match:])
			found_features.append(feature_name)
	f.close()
	return found_features

def filename_has_ext(filename, valid_ext):
	ext = os.path.splitext(filename)[-1]
	return ext in valid_ext

def build_matrix(all_features, implemented_client_features):
	f = open(MATRIX_TABLE_FILE, 'w')
	write_matrix_table_header(f)
	count = 0
	for feature in all_features:
		write_matrix_table_feature(f, feature, implemented_client_features, count)
		count += 1
	write_matrix_table_footer(f)
	f.close()

def write_matrix_table_header(f):
	header = "\\begin{tabular}{|l|l|l|l|}\n"
	header += "\\hline\n"
	header += "Feature & Implemented in Client & Implemented in Server & Tested \\\\ \n"
	header += "\\hline\n"
	f.write(header)
	
def write_matrix_table_footer(f):
	f.write("\\end{tabular}\n")

def write_matrix_table_feature(f, feature, implemented_client_features, count):
	line = ""

	feature_color = "White"
	if count % 2 == 1:
		feature_color = "FeatureOdd"

	yes_color = "FeatureYes"
	no_color= "FeatureNo"	

	line += "\\cellcolor{" + feature_color + "}" + feature + " &"

	if feature in implemented_client_features:
		line += "\\cellcolor{" + yes_color + "}Yes &"
	else:
		line += "\\cellcolor{" + no_color + "}No &"

	# No support for server features yet
	line += "\\cellcolor{" + no_color + "}No &"

	# No support for tests yet
	line += "\\cellcolor{" + no_color + "}No \\\\"

	line += "\\hline"

	f.write(line + "\n")

if __name__ == '__main__':
	texfiles = find_tex_files()
	all_features = []
	implemented_client_features = []
	implemented_server_features = []

	for filename in texfiles:
		features = find_features_in_tex_file(filename)
		all_features = list(set(all_features + features))

	client_source_files = find_source_files(
		gdcc_conf.CLIENT_SOURCE_DIR,
		gdcc_conf.CLIENT_SOURCE_EXT)

	for source_file in client_source_files:
		features = find_features_in_source_file(gdcc_conf.CLIENT_COMMENT, source_file)
		implemented_client_features = list(set(
			implemented_client_features + features))
	
	build_matrix(all_features, implemented_client_features)

	subprocess.call(PDFLATEX_CMD, cwd=TEMPLATE_DIR)
	subprocess.call(["mv", TEMPLATE_FILE, gdcc_conf.WWW_ROOT])

