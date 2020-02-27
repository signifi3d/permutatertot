import argparse
import sys

final_set = set()
char_map = {}

parser = argparse.ArgumentParser()
parser.add_argument("-w","--wordlist", required=True, help="wordlist to permutate")
parser.add_argument("-o","--output", help="output filepath")
parser.add_argument("-m", "--map", required=True, metavar='MAPFROM:MAPTO', help="character map for permutations")
args = parser.parse_args()

if args.wordlist:
    global inf
    inf = open(args.wordlist, "r")

if args.output:
    global out
    out = open(args.output, "w")  

if args.map:
    map_strings = args.map.split(":")
    if len(map_strings) <= 1 or len(map_strings) > 2:
        sys.exit("Map must be in the format XX..XX:YY..YY where the number of Xs and Ys is equal and separated by a :")
    if len(map_strings[0]) != len(map_strings[1]):
        sys.exit("Map must be in the format XX..XX:YY..YY where the number of Xs and Ys is equal and separated by a :")
    for i in range(0, len(map_strings[0])):
        if map_strings[0][i] in char_map:
            char_map[map_strings[0][i]] = char_map[map_strings[0][i]] + map_strings[1][i]
        else:
            char_map[map_strings[0][i]] = map_strings[1][i]


def rule_perms(perm, pos):
    if pos == len(perm):
        return
    final_set.add(perm)
    rule_perms(perm, pos+1)
    if perm[pos].lower() in char_map:
        for i in char_map[perm[pos]]:
            perm = perm[0:pos] + i + perm[pos+1:len(perm)]
            final_set.add(perm)
            rule_perms(perm, pos+1)

for lines in inf.read().split('\n'):
    rule_perms(lines, 0)

for i in final_set:
    if args.output:
    	out.write(i + '\n')
    else:
        print(i)

if args.output:
	out.close()
inf.close()
