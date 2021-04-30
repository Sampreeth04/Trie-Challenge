import argparse
import requests

# Create the parser
my_parser = argparse.ArgumentParser(description='Perform operations on on-line TRIE')

# Add the arguments
my_parser.add_argument('Operation',
                       metavar='op',
                       type=str,
                       help='operation to perform on the TRIE',
		       choices=['insert','delete','search','suggest','print'])
my_parser.add_argument('Keyword',
                       metavar='keyword',
                       type=str,
                       help='input keyword or keywords for the operation')


# Execute the parse_args() method
args = my_parser.parse_args()

op = args.Operation
word = args.Keyword

cloud_url="https://my-trie.herokuapp.com/"
cloud_op_url=cloud_url+op+"?word="+word
#print(cloud_op_url);
resp = requests.get(cloud_op_url);
print(resp.text);
