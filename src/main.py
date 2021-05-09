from base import MongoServer
from gui import PostMan, PrimitiveApi

def main() -> None:
	PostMan()
	# api = PrimitiveApi()
	# api.initializeServer(servername='mongodb+srv://AdminUser:bX2ZqWc2Ajh4rp5j@emsdatabase.xq0im.mongodb.net/PostMan?retryWrites=true&w=majority')

	# api.sendMessage({
	# 	'content': 'Hello, World!',
	# 	'author': 'Em'
	# })

if __name__ == '__main__':
    main()
