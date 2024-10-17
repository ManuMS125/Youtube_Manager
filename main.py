import sqlite3

con = sqlite3.connect('youtube_videos.db')




cursor = con.cursor()



cursor.execute("""
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )

""")

def list_videos():
    cursor.execute('SELECT * FROM videos')
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute('INSERT INTO videos (name, time) VALUES (?, ?)', (name, time))
    con.commit()

def update_video(vid_ID, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, vid_ID))
    con.commit()

def delete_video(vid_ID):
    cursor.execute('DELETE FROM videos WHERE id = ?', (vid_ID,))
    con.commit()


def main():
    while True:
        print('\n Youtube Manager app with DB')
        print('1. List videos')
        print('2. ADD videOs')
        print('3. update videos')
        print('4. Delete videos')
        print('5. Exit')

        choice = input('Enter your choice : ')

        match choice:
            case '1':
                list_videos()
            case '2':
                name = input ('Enter the video name')
                time = input('Enter the video time')
                add_video(name, time)
            case '3':
                vid_ID = input('Enter video id to update : ')
                name = input ('Enter the video name')
                time = input('Enter the video time')
                update_video(vid_ID, name, time)

            case '4':
                vid_ID = input('Enter video id to delete : ')
                delete_video(vid_ID)

            case '5':
                break
            case _:
                print('Invalid Choice.')
    con.close()


if __name__ == '__main__':
    main()