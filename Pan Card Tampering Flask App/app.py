from app import app

app.config['ENV'] = 'development'

if __name__ == '__main__':
   app.run()