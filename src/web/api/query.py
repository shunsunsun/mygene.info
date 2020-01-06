# -*- coding: utf-8 -*-
from biothings.web.api.es.query import ESQuery


class ESQuery(ESQuery):
    def _metadata_query(self, query_kwargs):
        del query_kwargs['rest_total_hits_as_int']
        return self.client.indices.get_mapping(**query_kwargs)
