import re

class CleanSong(object):
    def __init__(self, raw_song):
        self.raw_song = raw_song

    def clean_song(self):
        self.remove_special_characters_keep_hyphen()
        self.remove_concatenated_digits_larger_than_four()
        self.remove_string_the()
        self.remove_string_edit()
        self.remove_string_remastered()
        self.remove_string_remaster()
        self.remove_string_radio()
        return self.organize_song()

    def organize_song(self):
        clean_song = self.remove_empty_strings_from(self.raw_song)
        if '-' not in clean_song:
            return {
                    'artist': '',
                    'song': '',
                    'full_song': clean_song.strip()
            }
        else:
            split_song = clean_song.split('-')
            return {
                    'artist': split_song[0].strip(),
                    'song': split_song[1].strip(),
                    'full_song': clean_song.strip()
            }

    def remove_empty_strings_from(self, raw_string):
        raw_list = raw_string.split(' ')
        clean_list = list(filter(None, raw_list))
        return ' '.join(clean_list)

    def remove_string_radio(self):
        self.raw_song = self.raw_song.replace('radio', '')

    def remove_string_remaster(self):
        self.raw_song = self.raw_song.replace('remaster', '')

    def remove_string_remastered(self):
        self.raw_song = self.raw_song.replace('remastered', '')

    def remove_string_edit(self):
        self.raw_song = self.raw_song.replace('edit', '')

    def remove_string_the(self):
        self.raw_song = self.raw_song.replace('the','')

    def remove_concatenated_digits_larger_than_four(self):
        split_string_list = self.raw_song.split(' ')
        for string in split_string_list:
            if string.isdigit() and len(string) > 4:
                split_string_list.remove(string)
        self.raw_song = ' '.join(split_string_list)

    def remove_special_characters_keep_hyphen(self):
        pattern = re.compile('[^0-9A-Za-z\s\-]')
        self.raw_song =  pattern.sub('', self.raw_song)
