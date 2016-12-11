from livereload import Server, shell

server = Server()

# run a shell command
server.watch('*')
server.serve()