from youtube_transcript_api import YouTubeTranscriptApi

class YoutubeTranscricao:
    
    def __init__(self, url):
        self.url = url
        self.idioma = 'pt'

    
    def video_id(self):
        return self.url.split('watch?v=')[1]

    def transcricao(sefl):
        tanscricao = YouTubeTranscriptApi.get_transcript("CIC_5xusogM&t=45s", languages=['pt'])
        print(transcricao[0]['text'])
        print(transcricao[1]['text'])
        print(transcricao[2]['text'])
        print(transcricao[3]['text'])
        print(transcricao[4]['text'])

trans = YoutubeTranscricao('https://www.youtube.com/watch?v=CIC_5xusogM&t=45s')
print(trans.video_id())