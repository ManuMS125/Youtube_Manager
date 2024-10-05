import json

def load_data():
    try:
        with open('youtube.txt','r') as f:
            test= json.load(f)   #json loads in list format
            
            return test
    except FileNotFoundError:
        return []

def save_data(videos):
    with open('youtube.txt', 'w') as f:
        json.dump(videos, f)   #json dumps in list type


    

def list_all_videos(videos):
    print('\n','*'*89)
    if(len(videos)==0):
        print('There are no videos currently, please add them')
    for index, vid in enumerate(videos, start=1):
        print(index,vid['name'],vid['time'])
    print('\n','*'*89)


def add_videos(videos):
    name=input("Entaer name of the video :")
    time=input('Enter time length of the video :')
    videos.append({'name':name,'time':time})
    save_data(videos)

def update_videos(videos):
    list_all_videos(videos)
    index=int(input('Enter the index of the video you wants to update : '))
    if (1<=index<=len(videos)):
        name=input('Enter the name of the video : ')
        time=input('Enter the tital length : ')
        videos[index-1]={'name':name, 'time':time}
        save_data(videos)      
    else:
        print('invalid')

def delete_videos(videos):
    list_all_videos(videos)
    index=int(input("Enter the index of the video to be deleted : "))
    if (1<=index<=len(videos)):
        del videos[index-1]
        save_data(videos)
    else:
        print("invalid index")


def main():
    videos=load_data()

    while True:
        print("Welcome\nYoutube Manager\n Select an option:")
        print("1.List all youtube videos")
        print("2.Add  youtube videos")
        print("3.update a youtube video details")
        print("4.Delete a video")
        print('5.Exit')

        choice=input("Enter your choice:")

        

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                print('Thank You!!')
                break
            case _:
                print('Invalid Choiceesssghghgjhgg')
        










if __name__=='__main__':
    main()





