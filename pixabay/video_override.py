##
# Pixabay API (unofficial)
# @author Gatin<gtindram@gmail.com>
# @date 8.5.2023


from .video import video


class video_o(video):
    ##
    # Init video object
    # @param data data of video in JSON format
    # @return video obj
    def __init__(self, data):
        self._raw_data = data

    ##
    # Get width of Large Video
    def getLargeVideoWidth(self):
        return self._raw_data['videos']['large']['width']

    ##
    # Get Height of Large Video
    def getLargeVideoHeight(self):
        return self._raw_data['videos']['large']['height']

    ##
    # Get Size of Large Video
    def getLargeVideoSize(self):
        return self._raw_data['videos']['large']['size']

    ##
    # Get width of medium Video
    def getmediumVideoWidth(self):
        return self._raw_data['videos']['medium']['width']

    ##
    # Get Height of medium Video
    def getmediumVideoHeight(self):
        return self._raw_data['videos']['medium']['height']

    ##
    # Get Size of medium Video
    def getmediumVideoSize(self):
        return self._raw_data['videos']['medium']['size']

    ##
    # Get width of small Video
    def getsmallVideoWidth(self):
        return self._raw_data['videos']['small']['width']

    ##
    # Get Height of small Video
    def getsmallVideoHeight(self):
        return self._raw_data['videos']['small']['height']

    ##
    # Get Size of small Video
    def getsmallVideoSize(self):
        return self._raw_data['videos']['small']['size']

    ##
    # Get width of tiny Video
    def gettinyVideoWidth(self):
        return self._raw_data['videos']['tiny']['width']

    ##
    # Get Height of tiny Video
    def gettinyVideoHeight(self):
        return self._raw_data['videos']['tiny']['height']

    ##
    # Get Size of tiny Video
    def gettinyVideoSize(self):
        return self._raw_data['videos']['tiny']['size']
    
    ##
    # Get url of image of author of video
    def getUserImageURL(self):
        return self._raw_data['userImageURL']