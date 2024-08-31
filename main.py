from data_seeder.mongo_db_seeder import load_confluence_data
from graph.graph import app

from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    print('Hello World!')

    while True:
        user_prompt = input('--> ')
        if user_prompt == 'exit':
            break
        elif user_prompt == 'load_data':
            load_confluence_data()
        else:
            result = app.invoke({'question': user_prompt})
            print(result)