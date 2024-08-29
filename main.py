from dotenv import load_dotenv

from data_seeder.mongo_db_seeder import load_confluence_data

load_dotenv()

if __name__ == '__main__':
    print('Hello World!')
    while True:
        user_prompt = input('--> ')
        if user_prompt == 'exit':
            break
        elif user_prompt == 'load_data':
            load_confluence_data()