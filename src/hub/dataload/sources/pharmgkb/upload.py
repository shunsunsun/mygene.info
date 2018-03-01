from .parser import load_pharmgkb
import biothings.hub.dataload.uploader as uploader

class PharmgkbUploader(uploader.MergerSourceUploader):

    name = "pharmgkb"

    def load_data(self, data_folder):
        return load_pharmgkb(data_folder)

    @classmethod
    def get_mapping(klass):
        mapping = {
            "pharmgkb": {
                "type": "text",
                "analyzer": "string_lowercase",
                'copy_to': ['all'],
            }
        }
        return mapping
