from lib.grammar.cfgtocnf import readGrammarFile, convertGrammar
from lib.tokenizer import createToken
from lib.parser import verdictCYK
import re, os, sys, argparse

def bannerCompiler() :
  print()
  print("              ____        __  __                 ")
  print("             / __ \__  __/ /_/ /_  ____  ____    ")         
  print("            / /_/ / / / / __/ __ \/ __ \/ __ \   ")        
  print("           / ____/ /_/ / /_/ / / / /_/ / / / /   ")         
  print("        __///_   \__, /\__/_/ /_/\__/_/// /_/    ")         
  print("       / ____/__/__///_ ___  ____  (_) /__  _____")                 
  print("      / /   / __ \/ __ `__ \/ __ \/ / / _ \/ ___/")                                                                  
  print("     / /___/ /_/ / / / / / / /_/ / / /  __/ /    ") 
  print("     \____/\____/_/ /_/ /_/ .___/_/_/\___/_/     ") 
  print("                         /_/                     ")  
  print()

if __name__ == "__main__":
  # Argparse
  parser = argparse.ArgumentParser()
  parser.add_argument('file', type = argparse.FileType('r'))
  args = parser.parse_args()

  # Banner
  bannerCompiler()

  # Token & CNF
  token = createToken(args.file.name)
  CNFgrammar = convertGrammar((readGrammarFile("lib/grammar/cnf.txt")))
  print(token)
  print(CNFgrammar)

  # Verdict
  print(verdictCYK(token, CNFgrammar))
  # verdictCYK(token, CNFgrammar)

     