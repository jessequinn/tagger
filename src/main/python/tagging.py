from mutagen.mp4 import MP4


class MetaTag(object):
    def __init__(self, file):
        self.meta_tag = MP4(file)

    def get_meta_tags(self):
        return self.meta_tag

    def delete_meta_tags(self):
        """
        Preserver encoding tool info.
        :return:
        """
        encoding_tool = self.meta_tag['\xa9too']
        self.meta_tag.delete()
        self.meta_tag['\xa9too'] = encoding_tool

    def save_meta_tags(self):
        self.meta_tag.save()


class MovieMetaTag(MetaTag):
    def __init__(self, file, nam, desc, ldes, day, gen):
        """

        :param file:
        :param nam:
        :param des:
        :param ldes:
        :param day:
        :param gen:
        """
        MetaTag.__init__(self, file)

        # set tags
        # TODO: add image cover
        self.meta_tag['\xa9nam'] = [nam]
        self.meta_tag['desc'] = [desc]
        self.meta_tag['ldes'] = [ldes]
        self.meta_tag['\xa9day'] = [day]
        self.meta_tag['\xa9gen'] = [gen]
        self.meta_tag['stik'] = [9]


class ShowMetaTag(MetaTag):
    def __init__(self, file, nam, tvsh, tvsn, tves, tvnn, desc, ldes, day, gen, trkn, disk):
        """

        :param file:
        :param nam:
        :param tvsh:
        :param tvsn:
        :param tves:
        :param tvnn:
        :param desc:
        :param ldesc:
        :param day:
        :param gen:
        :param trkn:
        :param disk:
        """
        MetaTag.__init__(self, file)

        # set tags
        # TODO: add image cover
        self.meta_tag['\xa9nam'] = [nam]
        self.meta_tag['tvsh'] = [tvsh]
        self.meta_tag['tvsn'] = [tvsn]
        self.meta_tag['tves'] = [tves]
        self.meta_tag['tvnn'] = [tvnn]
        self.meta_tag['desc'] = [desc]
        self.meta_tag['ldes'] = [ldes]
        self.meta_tag['\xa9day'] = [day]
        self.meta_tag['\xa9gen'] = [gen]
        self.meta_tag['trkn'] = [(trkn, 0)]
        self.meta_tag['disk'] = [(disk, 0)]
        self.meta_tag['stik'] = [10]
