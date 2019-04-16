from mutagen.mp4 import MP4
import os


class MetaTag(object):
    def __init__(self, file):
        self.meta_tag = file

    @property
    def meta_tag(self):
        return self._meta_tag

    @meta_tag.setter
    def meta_tag(self, value):
        if not os.path.isfile(value):
            raise FileNotFoundError('File must exist.')
        self._meta_tag = MP4(value)

    @meta_tag.deleter
    def meta_tag(self):
        del self._meta_tag

    def delete_meta_tags(self):
        """
        Preserve encoding tool info.
        :return:
        """
        encoding_tool = self.meta_tag['\xa9too']
        self.meta_tag.delete()
        self.meta_tag['\xa9too'] = encoding_tool

    def save_meta_tags(self):
        """

        :return:
        """
        self.meta_tag.save()


class FilmMetaTag(MetaTag):
    def __init__(self, file):
        """

        :param file:
        """
        MetaTag.__init__(self, file)

        # set tags
        # TODO: add image cover
        self.meta_tag['stik'] = [9]

    def set_title(self, value):
        self.meta_tag['\xa9nam'] = [value]

    def set_description(self, value):
        self.meta_tag['desc'] = [value]
        self.meta_tag['ldes'] = [value]

    def set_date(self, value):
        self.meta_tag['\xa9day'] = [value]

    def set_genre(self, value):
        self.meta_tag['\xa9gen'] = [value]


class ShowMetaTag(MetaTag):
    def __init__(self, file):
        """

        :param file:
        """
        MetaTag.__init__(self, file)

        # set tags
        # TODO: add image cover
        self.meta_tag['stik'] = [10]

    def set_episode_title(self, value):
        """

        :param value: Episode title
        :return:
        """
        self.meta_tag['\xa9nam'] = [value]

    def set_description(self, value):
        """

        :param value: Description
        :return:
        """
        self.meta_tag['desc'] = [value]
        self.meta_tag['ldes'] = [value]

    def set_date(self, value):
        """

        :param value: Date
        :return:
        """
        self.meta_tag['\xa9day'] = [value]

    def set_genre(self, value):
        """

        :param value: Genre
        :return:
        """
        self.meta_tag['\xa9gen'] = [value]

    def set_network(self, value):
        """

        :param value: Network
        :return:
        """
        self.meta_tag['tvnn'] = [value]

    def set_show_title(self, value):
        """

        :param value: Show title
        :return:
        """
        self.meta_tag['tvsh'] = [value]

    def set_season(self, value):
        """

        :param value: Disk # (Season #)
        :return:
        """
        if not isinstance(value, int):
            raise TypeError('Value passed must be an integer.')
        self.meta_tag['tvsn'] = [value]
        self.meta_tag['disk'] = [(value, 0)]

    def set_episode(self, value):
        """

        :param value: Track # (Episode #)
        :return:
        """
        if not isinstance(value, int):
            raise TypeError('Value passed must be an integer.')
        self.meta_tag['tves'] = [value]
        self.meta_tag['trkn'] = [(value, 0)]
